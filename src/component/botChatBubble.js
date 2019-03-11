import React from 'react';

// compares two texts and returns a string of the second text where
// words different from text1 are surrounded by span tags
const compareTexts = (text1, text2) => {
  text1 = text1.split(" ");
  text2 = text2.split(" ");
  if( text1.length !== text2.length ){
    return -1;
  }
  var rslt = [];
  for( let i = 0; i < text1.length; i++){
    if(text1[i] === text2[i]){
      rslt.push(text1[i]);
    }else{
      // if the text is changed, add a span tag around it
      rslt.push(<span className="changed">{text2[i]}</span>);
    }
    // push a space if we are not at the end of the string
    if(i + 1 < text1.length){
      rslt.push(" ");
    }
  }
  return rslt;
}

const BotChatBubble = function({response, dataType}) {
  var styledText = [];
  var question = "";

  if(dataType === "text"){
    styledText = [<p>{response}</p>];
  }else if(dataType === "load"){
    styledText = response;
  }else if( dataType === "spellcheck"){
    styledText = <p>Did you mean &quot;{compareTexts(response.input, response.output)}&quot;?</p>;
  }else{
    (response.answer).forEach((element) => {styledText.push(<p className="table-response">{element}</p>)});
    question = <div className="question-box">
                  <p className="format-question">{response.question}</p>
               </div>
  }
 
  return (
        <div className="bubble bot">
          <div className="image"></div>
          <div className="text-bubble">
            {question}
            {styledText}
          </div>
        </div>
      );
}

export default BotChatBubble;