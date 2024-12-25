const express = require("express");
const { spawn } = require("child_process");
const cors = require("cors");

const app = express();

app.use(express.json());
app.use(cors());

// API endpoint for handling the search request
app.post("/api/search", (req, res) => {
  const query = req.body.query; // Get the query from the request body

  // Execute the Python script with the provided query
  const pythonProcess = spawn("python", ["../../TF-IDF/query.py", query]);

  let outputData = "";

  pythonProcess.stdout.on("data", (data) => {
    outputData += data.toString();
  });

  // Handle the completion of the Python script execution
  pythonProcess.on("close", (code) => {
    if (code === 0) {
      try {
        const resultList = JSON.parse(outputData);
        res.json(resultList);
      } catch (error) {
        console.error("Error parsing JSON:", error);
        res.status(500).json({ error: "Error parsing JSON" });
      }
    } else {
      console.error("Python script execution failed");
      res.status(500).json({ error: "Python script execution failed" });
    }
  });
});

// show success message on / route
app.get("/", (req, res) => {
  res.send("Server is running successfully");
});

app.listen(5000 || process.env.PORT, () => {
  console.log("Backend server is running on http://localhost:5000");
});
