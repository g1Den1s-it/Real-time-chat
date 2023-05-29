function unvisible(){
    let div = document.getElementById("content")
    let dropdown = document.getElementById("dropdown")

    div.classList.remove("show")
    dropdown.onclick = visible
}
function visible(){
    let content = document.getElementById("content")
    let dropdown = document.getElementById("dropdown")

    content.classList.add("show")
    dropdown.onclick = unvisible
}
