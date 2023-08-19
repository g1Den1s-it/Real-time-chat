const items = document.querySelectorAll(".item")
const userImage = document.getElementById("user-image")
const chatBtn = document.getElementById("chat")
const videoChatBtn = document.getElementById("video-chat")
const settingBtn = document.getElementById("setting")
const windowDiv = document.getElementById('window')
const wrapperDiv = document.getElementById("window-wrapper")
const infoEl = document.getElementById('message')
const nameDiv = document.getElementById('name')

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

if (userImage != null){
    userImage.style.border = `2px solid ${randomColor()}`
}

let activeSocket = false
chatBtn.addEventListener('click', async () => {
    if (activeSocket) {
        return
    }

    window.history.pushState({}, '', '/chat/')
    infoEl.classList.add('deactive')
    const socket = new WebSocket('ws://' + window.location.host + '/ws/chat/')
    socket.addEventListener('open', ()=>{
        console.log('WebSocket connection opened')
        activeSocket = true
    })
    let currentUser = null
    socket.addEventListener('message', (event)=>{

        const dataEvent = JSON.parse(event.data)
        nameDiv.textContent = 'Chat'

        if(dataEvent['user']){
            currentUser = dataEvent['user']
            console.log(currentUser)
        }

        if(dataEvent['list_chat'] && Object.keys(dataEvent['list_chat']).length > 0){
            const data = dataEvent['list_chat']
            data.forEach(chatData =>{
                const newDiv = document.createElement('div')
                newDiv.className = "window-wrapper-chat"
                newDiv.setAttribute('custom-id', chatData['custom_id'])
                newDiv.textContent = chatData['name']
                wrapperDiv.appendChild(newDiv)
            })
            const chatsDiv = document.querySelectorAll(".window-wrapper-chat")
            chatsDiv.forEach(chat => {
                chat.addEventListener('click', () => {
                    if(chat.classList.contains('open')){
                        return
                    }
                    chatsDiv.forEach(chat => {
                        chat.classList.remove('open')
                    })

                    chat.classList.add('open')

                    socket.send(JSON.stringify({
                        'chat': chat.getAttribute('custom-id')
                    }))
                    const room = document.querySelector('.window-room')
                    if (room !== null){
                        room.remove()
                    }
                })
            })
        }else if(dataEvent['list_message']){
            const messageData = dataEvent['list_message']

            const newDiv = document.createElement('div')
            newDiv.className = 'window-room'
            windowDiv.appendChild(newDiv)

            messageData.forEach(message =>{
                const messageDiv = document.createElement('div')
                const userImage = document.createElement('img')
                const userText = document.createElement('div')
                const username = document.createElement('div')
                const time = document.createElement('div')
                const info = document.createElement('div')

                messageDiv.className = 'window-room-message'
                info.className = 'window-room-info'
                userImage.className = 'window-room-info-image'
                userText.className = 'window-room-message-text'
                username.className = 'window-room-info-username'
                time.className = 'window-room-info-time'

                userImage.src = message.owner_image
                userText.textContent = message.text
                username.textContent = message.owner
                time.textContent = message.date

                newDiv.appendChild(messageDiv)
                messageDiv.appendChild(userText)
                newDiv.appendChild(info)
                info.appendChild(userImage)
                info.appendChild(username)
                info.appendChild(time)
            })
        }
    })

    socket.addEventListener('error', (e)=>{
        console.log(e)
    })

    socket.addEventListener('close', (e)=>{
        console.log(e)
        activeSocket = false
    })


})








