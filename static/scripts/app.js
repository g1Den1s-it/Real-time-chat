const items = document.querySelectorAll("#item")
const userImage = document.getElementById("user-image")

items.forEach(item => {
    item.addEventListener('click', () =>{
        items.forEach(i => {
            i.classList.remove('active')
        })
        item.classList.add('active')

    })
})

function randomColor() {
  return `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;
}

userImage.style.border = `2px solid ${randomColor()}`