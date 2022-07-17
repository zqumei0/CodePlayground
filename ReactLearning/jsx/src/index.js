// Step 1: Import React and ReactDOM libraries
// ReactDom = Show components in a Browser
// ReactNative = Show components in a Mobile Device
import React from 'react';
import ReactDOM from 'react-dom/client';

// Step 2: Get a reference to the div with ID root
const el = document.getElementById('root');

// Step 3: Tell React to take control of the element
const root = ReactDOM.createRoot(el);

// Step 4: Create a component
function App() {
  return <h1>Hello, World!</h1>;
}

function ExerciseOne() {
  // Generate values to show JSX
  const name = 'Alice';

  // Return content of component
  return (
    <div>
      <h1>
        Hello, {name}
      </h1>
    </div>
  );
}

function ExerciseTwo() {
  return (
    <div className="wrapper">
      <textarea
        readOnly
        maxLength={3}
        spellCheck
        style={{backgroundColor: 'gray'}}
      />
    </div>
  )
}
// Step 5: Show the component on the screen
root.render(<App />);
// root.render(<ExerciseOne />);
// root.render(<ExerciseTwo />);