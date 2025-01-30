const express = require("express"); // Import express
const app = express(); // Create express app
const cors = require("cors");

// Middlewares
app.use(express.json({ limit: "16kb" }));
app.use(express.urlencoded({ extended: true, limit: "16kb" }));
app.use(express.static("public"));
app.set("view engine", "ejs");
app.set("views",path.join(__dirname,"../Frontend/ejsPages"));
app.use(express.static(path.join(__dirname,"../Frontend/CSS")));
app.use(express.static(path.join(__dirname,"../Frontend/images")));
app.use(express.static(path.join(__dirname,"../../Frontend/JS")));

// import routes
const homeRoute = require("./routes/home.routes.js");


// home routes declaration
app.use("/", homeRoute);

module.exports = app; // Export app