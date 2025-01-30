app.get('/events', (req, res) => {
    const events = [
        { name: "SOLOCODEX", image: "/images/solocodex.jpg", participants: 7 },
        { name: "CODESPRINT", image: "/images/codesprint.jpg", participants: 3 },
        { name: "VIT FRESHERS 2K24", image: "/images/freshers.jpg", participants: 5 },
        { name: "Coffee With Alumni", image: "/images/alumni.jpg", participants: 2 },
        { name: "Viksit Bharat", image: "/images/viksit.jpg", participants: 4 },
        { name: "Vortexa", image: "/images/vortexa.jpg", participants: 1 }
    ];
    res.render('events', { events });
});
