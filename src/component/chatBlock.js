import React, { Component } from 'react';
import UserChatBubble from './userChatBubble';
import BotChatBubble from './botChatBubble';
import LoadingBubbles from './loadingBubbles'
import '../static/styles/Chat.css'

class ChatBlock extends Component {
  constructor(props){
    super(props);
    this.state = {
      question: "", 
      chatnodes: props.nodes,
      responseState: "question", // the state should either be 'question' or 'spell response'
      questionForms: []
    }
  }

  // check the spalling of a users question
  checkSpelling = (text) => {
    this.setBotAnswer(<LoadingBubbles />, "load");
    fetch(`http://localhost:5000/spellcheck?spell=${text}`)
    .then(response => response.json())
    .then(response => {
      this.setState(function(prevState){
            let chatnodes = prevState.chatnodes;
            chatnodes.pop();
            return {chatnodes: chatnodes, questionForms: [response.input, response.output]}
      });
      // check if the spelling is okay or not
      if(response.input === response.output){
        // if there are no spelling mistakes, we can look for an answer
        this.getResponse(response.input);
      }else{
        this.setBotAnswer(response, "spellcheck");
        // if there is spelling mistakes, we are going to look for a spell response
        this.setState({responseState: "spell response"});
      }
    })
    .catch(err => {
      this.setState(function(prevState){
          let chatnodes = prevState.chatnodes;
          chatnodes.pop();
          return {chatnodes: chatnodes}
      })
      this.setBotAnswer("Sorry, an error occured while trying to answer your question.", "text");
    })
  }

  // check if text is a positive (yes) or negative (no) statement
  checkYesOrNo = (text) => {
    this.setBotAnswer(<LoadingBubbles />, "load");
    setTimeout(()=>{
      fetch(`http://localhost:5000/yesorno?text=${text}`)
      .then(response => response.json())
      .then(response => {
        var original = this.state.questionForms[0];
        var corrected = this.state.questionForms[1];
        this.setState(function(prevState){
            let chatnodes = prevState.chatnodes;
            chatnodes.pop();
            return {chatnodes: chatnodes, responseState: "question", questionForms: []}
        })
        console.log(response)
        // the user said yes - use the corrected form
        if( response.response === "pos"){
          this.getResponse(corrected);
        }
        // the user said no - use their original question
        else{
          this.getResponse(original);
        }
      })
      .catch(err => {
          this.setState(function(prevState){
            let chatnodes = prevState.chatnodes;
            chatnodes.pop();
            return {chatnodes: chatnodes, responseState: "question"}
          })
          setTimeout(()=>{
            this.setBotAnswer("Sorry, an error occured while trying to answer your question.", "text");
          }, 200)
      })
      }, 1000);
  }

  getResponse = (question) => {
    this.setBotAnswer(<LoadingBubbles />, "load");
    // First check spelling
    fetch(`http://localhost:5000/question?question=${question}`)
    .then(response => response.json())
    .then(response => {
        this.setState(function(prevState){
          let chatnodes = prevState.chatnodes;
          chatnodes.pop();
          return {chatnodes: chatnodes}
        });
        this.setBotAnswer(response, "response");
    }).catch((err) => {
        this.setState(function(prevState){
          let chatnodes = prevState.chatnodes;
          chatnodes.pop();
          return {chatnodes: chatnodes}
        })
        this.setBotAnswer("Sorry, an error occured while trying to answer your question.", "text");
    })
    
  }

  setBotAnswer = (response, dataType) => {
      //Output bot's answer to the screen
      var botAnswer = <BotChatBubble response={response} dataType={dataType}/>;

      this.setState(prevState => ({chatnodes: prevState.chatnodes.concat(botAnswer)}));

      // Scroll down to answer
      this.scrollToBottom();
  }

  // Gets called when the input in the question box is changed
  typeQuestion = (e) => {
    this.setState({question: e.target.value})
  }

  submitMessage = () => {
    // If there is no text typed in the input box, do nothing
    if(this.state.question === ""){
      return
    }

    var question = this.state.question;
    // Reset the input box to nothing
    this.setState({question: ""});
    //Output user's question to the screen
    var userQuestion = <UserChatBubble text={question}/>;
    this.setState(prevState => ({chatnodes: prevState.chatnodes.concat(userQuestion)}));

    // Scroll down to question
    this.scrollToBottom();

    // wait one second before starting to respond
    setTimeout(()=>{
      // check if the bot is looking for a question or a response to a spelling correction
      // UNCOMMENT THE LINES BELOW TO CHECK FOR SPELLING 
      // if(this.state.responseState === "question"){
      //   // Call function to check spelling
      //   this.checkSpelling(question);
      // }else{
      //   this.checkYesOrNo(question);
      // }

      // COMMENT THE LINE BELOW AND UNCOMMENT THE LINES ABOVE TO CHECK FOR SPELLING
      this.getResponse(question);
      
    }, 1000);

  }

  keyPressHandler = (e) => {
    if(e.charCode === 13){
      this.submitMessage();
      e.preventDefault();
    }
  }

  scrollToBottom = () => {
    this.chatEnd.scrollIntoView();
  }

  componentDidMount(){
    // display "ask me a question" if the chat hasn't been opened from a minimized state
    console.log(this.state.chatnodes)
    if(this.state.chatnodes.length === 0){
      setTimeout(()=>{
        this.setState({chatnodes: [<BotChatBubble response={"Ask me a question!"} dataType={"text"}/>]}) 
      }, 1000)
    }
  }

  render() {

    // If there is text in the input box, the submit button will be active
    var arrowClasses = this.state.question === "" ? "" : "active";

    return (
      <div className="content">
        <div className="chat-widget">
        <div className="top">
          <div className="buttons">
            <div id="minimize" onClick={() => {this.props.minimize(this.state.chatnodes)}}>
            </div>
            <div id="exit" onClick={this.props.exit}>
            </div>
          </div>
        </div>
        <div className="chat">

          {this.state.chatnodes}


          <div style={{ width: "100%", height: "1px" }} ref={(el) => { this.chatEnd = el; }}></div>
        </div>
        <div className="bottom">
          <input type="text" placeholder="Type question..." autoComplete="off" onKeyPress={this.keyPressHandler} onChange={this.typeQuestion} value={this.state.question}/>
          <button onClick={this.submitMessage}>
            <svg style={{width:"24px", height:"24px"}} viewBox="0 0 24 24">
              <path fill="#d4d4d4" d="M2,21L23,12L2,3V10L17,12L2,14V21Z" className={arrowClasses}/>
            </svg>
          </button>
        </div>
      </div>
      </div>
    );
  }
}

export default ChatBlock;