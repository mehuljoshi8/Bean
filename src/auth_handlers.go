package main

import (
	"encoding/json"
	"net/http"
)

// This strcut models the structure of a user in both the request body
// and the DB
type Credentials struct {
	Password string `json: "password", db:password"`
	Username string `json: "username", db:"username"`
}

func signup(w http.ResponseWriter, r *http.Request) {
	//Parse and decode the request body into a new Credentials instance
	creds := &Credentials{}
	err := json.NewDecoder(r.Body).Decode(creds)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

}

//todo: add a session based signin route with session-based-auth
