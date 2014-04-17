#! /bin/sh

mongo ops --eval "db.dropDatabase()"
mongoimport --db ops --collection participants --type json --file data/participants.json --jsonArray