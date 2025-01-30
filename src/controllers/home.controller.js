const home = (req, res) => {
    res.render("groups.ejs");
};

module.exports = { home }; // Export home function