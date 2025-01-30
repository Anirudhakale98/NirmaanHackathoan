const app = require("./app"); // Import app
require("dotenv").config();

const PORT = process.env.PORT || 3000; // Define port

const connectDB = require("./db/index.js"); // Import connectDB

connectDB()
.then(()=>{
    app.on("error",(error)=>{
        console.log("ERROR: app.on - ", error);
        throw error;
    });

    app.listen(process.env.PORT, () => {
        console.log(`Server is running on port ${process.env.PORT}`);
    });
})
.catch((err) =>{
    console.log("MONGO db connection failed !!!", err);
});
