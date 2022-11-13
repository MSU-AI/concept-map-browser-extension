import axios from "axios"
const api = "http://127.0.0.1:8000/"

const form = document.querySelector(".form-data")

const generateMap = async text => {
    if (text === "") { return }
    try {
        const response = await axios.get(`${api}`, { params: { bro: text } })
        document.getElementById('conceptMap').src += '';
        console.log("succeeded")
        } catch (error) {
        console.log("failed")
        }
};

const handleSubmit = async e => {
    e.preventDefault()
    generateMap(document.getElementById("text").value)
    console.log("submitted")
};

form.addEventListener("submit", e => handleSubmit(e))
