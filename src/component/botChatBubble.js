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
    if( response.answer !== null){
      // Push the generated Query
      styledText.push(<p className="query"><span className="query-title">Generated Query:</span> {response.query}</p>)

      var tableHead = []
      var columns = []
      console.log(response.columns);
      console.log("HERE")
      for (let column of response.columns){
          columns.push(<th className="table-response">{column}</th>)
      }
      tableHead.push(<tr>{columns}</tr>)
      var tableBody = []
      // Only show the first 25 responses
      for (let arr of (response.answer).slice(0,25)){
        let levelArr = []
        for (let element of arr){
          levelArr.push(<td className="table-response">{element}</td>);
        }
        tableBody.push(<tr>{levelArr}</tr>);
      }

      styledText.push(<table><thead>{tableHead}</thead><tbody>{tableBody}</tbody></table>)
    }else{
      styledText.push(<p>Sorry, there were no results for that!</p>)
    }

    // ((response.answer).slice(0,25)).forEach((element) => {styledText.push(<tr className="table-response">{element.for}</tr>)});
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