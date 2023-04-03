### Hello! Welcome to müse, an automated playlist generator

müse directly links to your spotify account, so you don't have to worry about linking it personally!

A few pre-requisites for you to embark on your enjoy with müse:
1. Ensure that your have a Spotify account (our application also supports free users!)
    - if you do not have one, you can sign up for one here! https://www.spotify.com/ca-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F%3F
2. Have a few playlists in mind that you would love to add in already!
    - our application takes in your playlist link or id as an input, and helps you to generate a personalized, new playlist for you to explore more songs!
3. Have a few friends in mind!
    - müse also encourages the creation of groups!
    - with a group, you and all your invited friends are able to input your own playlists, and you can let müse do the rest!
    - we will take all the playlists as the input and generate a new playlist based on all of your listening preferences!

To start using müse:
- use `docker-compose up` to start running all the microservices
- `cd frontend`, `npm install`, `npm run build`, and `npm run dev` to run müse's GUI on your localhost!
- import the kong-snapshot.json file into your Kong configuration using the Konga Interface
