import React from 'react';

const Welcome = function({startChat}) {

  return (
        <div>
        <div className="introduction">
            <p>Welcome to my undergraduate capstone project! This project was to design a query platform where users can ask natural
            language questions which are then transformed into SQL. This project has a backend MySQL database from Zomato,
             a restaurant search and discovery service (view the dataset <a href="https://www.kaggle.com/shrutimehta/zomato-restaurants-data">here</a>).
            You can read all about my project <a href="https://docs.google.com/document/d/1QkAHASgwy4FDjfv_ayqTMMU3lFfY0fvXD_mBXJDqVaE/edit?usp=sharing">here</a>.</p>

             <p>Click the chat button below to ask my database a question!</p>
             <p><u>Some good questions to ask are:</u><br/>
             &quot;What are the Italian restaurants?&quot; <br/>
             &quot;What are the restaurants in Athens?&quot; <br/>
             &quot;Which Chinese restaurants are in Mumbai?&quot; <br/>
             &quot;Which restaurants have an excellent rating?&quot; <br/>
             &quot;What are the cities in Canada?&quot; <br/>
             &quot;What restaurants are in Australia?&quot;</p>
        </div>
             <div className="chat-button" onClick={startChat}>
              <svg style={{width: "30px", height: "30px"}} viewBox="0 0 24 24">
                <path fill="#FFFFFF" d="M12,3C17.5,3 22,6.58 22,11C22,15.42 17.5,19 12,19C10.76,19 9.57,18.82 8.47,18.5C5.55,21 2,21 2,21C4.33,18.67 4.7,17.1 4.75,16.5C3.05,15.07 2,13.13 2,11C2,6.58 6.5,3 12,3Z" />
              </svg>
            </div>
            <p id="icon-credit">chat icon by @<a href="http://twitter.com/templarian">templarian</a>, send icon by @<a href="https://twitter.com/Google">Google</a></p>
        </div>
      );
}

export default Welcome;