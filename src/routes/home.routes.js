const { Router } = require("express");
const { home } = require("../controllers/home.controller.js");


const router = Router();

// routes declartion
router.route("/").get(home);
router.route("/home").get(home);



module.exports = router; // Export router 