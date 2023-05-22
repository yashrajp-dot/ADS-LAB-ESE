create user 'user2'@'localhost' identified by 'user';
GRANT ALL PRIVILEGES ON *.* TO 'user2'@'localhost' WITH GRANT OPTION;

flush PRIVILEGES;


RUN THE ABOVE QUERIES TO CREATE A NEW USER


change const mysql = require("mysql"); in server/index.js

to const mysql = require("mysql2");

also run npm install mysql2 in server terminal




client

cd client
npm install
npm start


server

cd server
npm install
node index.js