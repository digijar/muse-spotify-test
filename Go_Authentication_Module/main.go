package main

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/gorilla/mux"
	"github.com/joho/godotenv"
)

type ResponseData struct {
	AuthToken    string  `json:"auth_token"`
	RefreshToken string  `json:"refresh_token"`
	ExpiryTime   float64 `json:"expiry_time"`
	Email        string  `json:"email"`
}

func getAuthToken(code string) (string, string, int) {
	clientID := os.Getenv("SPOTIFY_CLIENT_ID")
	clientSecret := os.Getenv("SPOTIFY_CLIENT_SECRET")
	redirectURI := os.Getenv("SPOTIFY_REDIRECT_URI")

	clientCreds := fmt.Sprintf("%s:%s", clientID, clientSecret)
	clientCreds64 := base64.StdEncoding.EncodeToString([]byte(clientCreds))

	headers := map[string][]string{
		"Authorization": {fmt.Sprintf("Basic %s", clientCreds64)},
		"Content-Type":  {"application/x-www-form-urlencoded"},
	}

	data := url.Values{
		"grant_type":    {"authorization_code"},
		"code":          {code},
		"redirect_uri":  {redirectURI},
		"client_id":     {clientID},
		"client_secret": {clientSecret},
	}

	req, _ := http.NewRequest("POST", "https://accounts.spotify.com/api/token", strings.NewReader(data.Encode()))
	req.Header = headers
	resp, _ := http.DefaultClient.Do(req)

	defer resp.Body.Close()

	var responseJSON map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&responseJSON)

	accessToken := responseJSON["access_token"].(string)
	refreshToken := responseJSON["refresh_token"].(string)
	expiresIn := int(responseJSON["expires_in"].(float64))

	return accessToken, refreshToken, expiresIn
}

func refreshAuthToken(refreshToken string) (string, int) {
	clientID := os.Getenv("SPOTIFY_CLIENT_ID")
	clientSecret := os.Getenv("SPOTIFY_CLIENT_SECRET")

	headers := map[string][]string{
		"Content-Type": {"application/x-www-form-urlencoded"},
	}

	data := url.Values{
		"grant_type":    {"refresh_token"},
		"refresh_token": {refreshToken},
		"client_id":     {clientID},
		"client_secret": {clientSecret},
	}

	req, _ := http.NewRequest("POST", "https://accounts.spotify.com/api/token", strings.NewReader(data.Encode()))
	req.Header = headers
	resp, _ := http.DefaultClient.Do(req)
	defer resp.Body.Close()

	var responseJSON map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&responseJSON)

	accessToken := responseJSON["access_token"].(string)
	expiresIn := int(responseJSON["expires_in"].(float64))

	return accessToken, expiresIn
}

func authenticateLogin(w http.ResponseWriter, r *http.Request) {
	code := r.URL.Query().Get("code")

	if code == "" {
		http.Error(w, "Missing authorization code", http.StatusBadRequest)
		return
	}

	accessToken, refreshToken, expiresIn := getAuthToken(code)
	expiryTime := time.Now().Add(time.Duration(expiresIn) * time.Second).Unix()

	responseData := ResponseData{
		AuthToken:    accessToken,
		RefreshToken: refreshToken,
		ExpiryTime:   float64(expiryTime),
	}

	json.NewEncoder(w).Encode(responseData)
}

func authenticateRefresh(w http.ResponseWriter, r *http.Request) {
	refreshToken := r.PostFormValue("refresh_token")

	if refreshToken == "" {
		http.Error(w, "Missing refresh token", http.StatusBadRequest)
		return
	}

	accessToken, expiresIn := refreshAuthToken(refreshToken)
	expiryTime := time.Now().Add(time.Duration(expiresIn) * time.Second).Unix()

	responseData := ResponseData{
		AuthToken:  accessToken,
		ExpiryTime: float64(expiryTime),
	}

	json.NewEncoder(w).Encode(responseData)
}

func authenticateEmail(w http.ResponseWriter, r *http.Request) {
	accessToken := r.URL.Query().Get("access_token")

	if accessToken == "" {
		http.Error(w, "Bad request. Missing access token.", http.StatusBadRequest)
		return
	}

	client := &http.Client{}
	req, _ := http.NewRequest("GET", "https://api.spotify.com/v1/me", nil)
	req.Header.Set("Authorization", fmt.Sprintf("Bearer %s", accessToken))
	req.Header.Set("Content-Type", "application/json")

	resp, _ := client.Do(req)
	defer resp.Body.Close()

	var userProfile map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&userProfile)

	userEmail := userProfile["email"].(string)
	responseData := ResponseData{
		Email: userEmail,
	}

	json.NewEncoder(w).Encode(responseData)
}

func main() {
	dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		log.Fatal("Error loading .env file")
	}
	environmentPath := filepath.Join(dir, "spotify_api_keys.env")
	err = godotenv.Load(environmentPath)

	r := mux.NewRouter()
	r.HandleFunc("/authenticate/login", authenticateLogin)
	r.HandleFunc("/authenticate/refresh", authenticateRefresh).Methods("POST")
	r.HandleFunc("/authenticate/email", authenticateEmail)

	log.Printf("Starting server on :5002")
	log.Fatal(http.ListenAndServe(":5002", r))
}
