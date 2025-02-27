$(document).ready(() => {
    console.log('index.js')
    function initialize() {
        console.log('initialize');
        getModelsList();
        callChatCompletion();

    }

    function eventHandler() {

    }

    function getModelsList() {
        $.ajax({
            url:'/api/openai_list',
            method:'POST',
            contentType:'application/json',
            success: function(data) {
                if (data) {
                    console.log(data);
                }
            },
            error: function (error) {
                console.log(error);
            }
        })
    }

    function callChatCompletion() {
        $.ajax({
            url:'/api/chat_openai',
            method:'POST',
            contentType:'application/json',
            data: JSON.stringify({
                messages: 'TestMessages',
                model: 'gpt-3.5-turbo',
                temperature:0.8
            }),
            success: function (data) {
                if(data) {
                    console.log(data);
                }
            },
            error: function (error) {
                console.log(error);
            }
        })
    }

    async function sendMessage() {
        const userInput = document.getElementById("userMessage").value;
        const responseElement = document.getElementById("response");

        if (!userInput.trim()) {
            alert("메시지를 입력하세요!");
            return;
        }

        const requestBody = {
            messages: [{ role: "user", content: userInput }]
        };

        try {
            const response = await fetch("/api/model", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(requestBody)
            });

            const data = await response.json();

            if (data.response) {
                responseElement.innerText = data.response;
            } else {
                responseElement.innerText = "오류 발생: " + (data.error || "응답 없음");
            }

        } catch (error) {
            console.error("API 요청 실패:", error);
            responseElement.innerText = "서버 오류가 발생했습니다.";
        }
    }

    initialize();
});
