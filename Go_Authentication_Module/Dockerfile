FROM golang:1.20-alpine

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY *.go ./

RUN go mod tidy
RUN go build -o /authentication
EXPOSE 5002

CMD ["/authentication"]