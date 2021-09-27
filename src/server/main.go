package main

import (
	"database/sql"
	"log"
	"net/http"

	_ "github.com/lib/pq"
)

var db *sql.DB

func main() {
	//auth_handlers
	http.HandleFunc("/signup", signup)
	http.HandleFunc("/signin", signin)

	initDB()
	log.Fatal(http.ListenAndServe(":8000", nil))
}

func initDB() {
	var err error
	db, err = sql.Open("postgres", "dbname=db sslmode=disable")
	if err != nil {
		panic(err)
	}
}
