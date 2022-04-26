const express = require("express")
const path = require("path")
const app = express()

const publicDirectoryPath = path.join(__dirname, "../public")
app.use(express.static(publicDirectoryPath))

const port = process.env.PORT || 3000

print(__dirname)

app.get("/", (req, res)=>{
    res.render("index")
})
app.get("/heuristica", (req, res)=>{
    var options = {
        root: path.join(__dirname)
    };
    res.sendFile("index", options)
})
// app.get("/download", (req, res)=>{
//     res.sendFile("index")
// })
// app.get("/dev-logs", (req, res)=>{
//     res.sendFile("index")
// })

app.listen(port, ()=>{
    console.log("The server is up on http://localhost:3000/ mennnnn!")
})