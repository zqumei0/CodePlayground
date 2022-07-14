import React from 'react';
import ReactDOM from 'react-dom';
import CommentDetail from './CommentDetail';
import ApprovalCard from './ApprovalCard';

const App = () => {
  return (
    <div className="ui container comments">
      <ApprovalCard>
        <CommentDetail 
          avatar='./logo192.png'
          author="Amantha"
          content="Nice blog post"
          timeAgo= "Today at 4:45PM"
        />
      </ApprovalCard>
      <ApprovalCard>
        <CommentDetail 
          avatar='./logo192.png'
          author="Teven"
          content="Funny name"
          timeAgo= "Today at 3:51PM"
        />
      </ApprovalCard>
      <ApprovalCard>
        <CommentDetail 
          avatar='./logo192.png'
          author="Tephanie"
          content="Hello World"
          timeAgo= "Yesterday at 4:45PM"
        />
      </ApprovalCard>
    </div>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));

