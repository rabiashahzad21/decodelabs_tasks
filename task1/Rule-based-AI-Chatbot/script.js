const chatBox = document.getElementById("chatBox");
const input = document.getElementById("userInput");
const newChat = document.getElementById("newChat");

function currentTime() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}

function addUserMessage(text) {

    chatBox.innerHTML += `
        <div class="user">
            <div class="message">
                ${text}
                <br>
                <small>${currentTime()}</small>
            </div>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}

function addBotMessage(text) {

    chatBox.innerHTML += `
        <div class="bot">
            <div class="avatar">🤖</div>
            <div class="message">
                ${text}
                <br>
                <small>${currentTime()}</small>
            </div>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}

function botReply(message){

message=message.toLowerCase().trim();

if(message=="hi"||message=="hello"||message=="hey"){

return "👋 Hello! Welcome to SmartAssist AI.<br><br>How can I assist you today?";

}

else if(message=="how are you"){

return "😊 I'm functioning perfectly and ready to help you.";

}

else if(message=="what is ai"){

return "🤖 Artificial Intelligence (AI) is the simulation of human intelligence by machines. It enables computers to think, learn, and solve problems.";

}

else if(message=="what is machine learning"){

return "📚 Machine Learning is a branch of AI that allows computers to improve their performance by learning from data.";

}

else if(message=="who made you"){

return "💻 I was developed as a professional rule-based chatbot using HTML, CSS, and JavaScript.";

}

else if(message=="help"){

return "📌 Available Commands:<br><br>• Hi<br>• Hello<br>• What is AI<br>• What is Machine Learning<br>• Thanks<br>• Bye";

}

else if(message=="thanks"||message=="thank you"){

return "❤️ You're welcome. Happy coding!";

}

else if(message=="bye"||message=="exit"){

return "👋 Goodbye! Have a wonderful day.";

}

else{

return "⚠ Sorry, I don't recognize that command.<br><br>Type <b>Help</b> to see available commands.";

}

}

function sendMessage(){

    const message=input.value.trim();

    if(message=="") return;

    addUserMessage(message);

    input.value="";

    const typing=document.createElement("div");

    typing.className="typing";

    typing.innerHTML=`
        <span></span>
        <span></span>
        <span></span>
    `;

    chatBox.appendChild(typing);

    chatBox.scrollTop=chatBox.scrollHeight;

    setTimeout(function(){

        typing.remove();

        addBotMessage(botReply(message));

    },1200);

}

input.addEventListener("keypress",function(e){

    if(e.key==="Enter"){
        sendMessage();
    }

});

newChat.onclick=function(){

    chatBox.innerHTML=`

<div class="bot">

<div class="avatar">🤖</div>

<div class="message">

Hello 👋<br><br>

I am <b>SmartAssist AI</b>.<br><br>

Start a new conversation.

</div>

</div>

`;

};