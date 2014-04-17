#! /bin/sh

mongo ops --eval "db.dropDatabase()"
mongoimport --db ops --collection participants --type json --file participants.json --jsonArray