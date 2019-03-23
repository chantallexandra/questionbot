import React, { Component } from 'react';
import ChatBlock from './component/chatBlock';
import Welcome from './component/welcome';
import './static/styles/App.css';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      chatState: "active", // chat state can be 'suspended' or 'active'
      chatnodes: ""
    }
  }

  exit = () =>{
    // remove any saved chat nodes
    this.setState({chatnodes: [], chatState: "suspended"});
  }

  minimize = (nodes) => {
    // save the state of the nodes when minimizing the chat
    this.setState({chatnodes: nodes, chatState: "suspended"});
  }

  startChat = () => {
    this.setState({chatState: "active"})
  }

  render() {

    var display = this.state.chatState === "active" ? <ChatBlock nodes={this.state.chatnodes} minimize={this.minimize} exit={this.exit}/> : 
                                                      <Welcome startChat={this.startChat}/>

    return (
      <div className="content">
        {display}
      </div>
    );
  }
}

export default App;
