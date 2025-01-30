const mongoose = require("mongoose");
const DB_NAME = require("../constants.js");

// console.log(DB_NAME);

const connectDB = async () => {
    try {
        const connectionInstance = await mongoose.connect(
            
            `${process.env.MONGODB_URL}/${DB_NAME}`
        );
        console.log(
            `MongoDB connected successfully !! DB HOST: ${connectionInstance.connection.host}`
        );
    } catch (error) {
        console.log("MONGODB connection failed !!!", error);
        process.exit(1);
    }
};

module.exports = connectDB;
