#! /bin/sh

mongo ops --eval "db.dropDatabase()"
mongoimport --db ops --collection participants --type json --file participants.json --jsonArray
mongoimport --db ops --collection news --type json --file news.json --jsonArray
