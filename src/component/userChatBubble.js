import React from 'react';

const UserChatBubble = function({text}) {
  return (
        <div className="bubble user">
        	<div className="text-bubble">
          		<p>{text}</p>
          	</div>
        </div>
      );
}

export default UserChatBubble;