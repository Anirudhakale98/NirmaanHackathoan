const { Router } = require("express");
const { home, aboutUs, contactUs } = require("../controllers/home.controllers.js");


const router = Router();

// routes declartion
router.route("/").get(home);
router.route("/home").get(home);



module.exports = router; // Export router 