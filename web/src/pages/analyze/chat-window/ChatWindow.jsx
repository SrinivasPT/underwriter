import React, { useState } from "react";
import styles from "./ChatWindow.module.css"; // Import custom CSS

const ChatWindow = () => {
    const [messages, setMessages] = useState([]);
    const [inputText, setInputText] = useState("");

    const handleSendMessage = () => {
        if (inputText.trim()) {
            setMessages([...messages, { text: inputText, sender: "user" }]);
            setInputText("");

            // Simulate a bot response
            setTimeout(() => {
                setMessages((prevMessages) => [...prevMessages, { text: "This is a bot response.", sender: "bot" }]);
            }, 1000);
        }
    };

    return (
        <div className={styles.chatWindow}>
            {/* Chat Messages */}
            <div className={styles.messages}>
                {messages.map((message, index) => (
                    <div key={index} className={`${styles.messageContainer} ${message.sender === "user" ? styles.user : styles.bot}`}>
                        <div className={styles.message}>{message.text}</div>
                    </div>
                ))}
            </div>

            {/* Chat Input */}
            <div className={styles.inputContainer}>
                <textarea
                    type="text"
                    className={styles.input}
                    placeholder="Type a message..."
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                    onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
                />
                <button className={styles.sendButton} onClick={handleSendMessage}>
                    Send
                </button>
            </div>
        </div>
    );
};

export default ChatWindow;
