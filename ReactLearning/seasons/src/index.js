import React from 'react';
import ReactDOM from 'react-dom';

/*
 * Component Lifecycle
 * 1) Constructor (constructor)
 *   a) Good place for one-time setup
 * 
 * 2) Render (render)
 *   a) Avoid doing anything besides returning JSX
 *   <Content visible on screen>
 * 
 * 3) ComponentDidMount (componentDidMount)
 *   a) Good place to do data-loading
 *   <Sit and wait for updates>
 * 4) ComponentDidUpdate (componentDidUpdate)
 *   a) Good place to do more more data-loading when
 *      state/props change
 *   b) If called, render will be invoked
 *   <Sit and wait until component no longer shown>
 * 5) ComponentWillUnmount (componentWillUnmount)
 *   a) Good place to do cleanup (especially for 
 *      non-React stuff)
 * 
 * Other lifecycle methods (Rarely used)
 *   1) shouldComponentUpdate
 *   2) getDerivedStateFromProps
 *   3) getSnapshotBeforeUpdate
 * 
 */

// Functional Component Implementation
/*
const App = () => {
  // Grab location of browser
  window.navigator.geolocation.getCurrentPosition(
    (position) => console.log(position),
    (err) => console.log(err)
  );

  return (
    <div>Latitude: </div>
  );
}
*/

// Class Component Implementation
class App extends React.Component {
  // Constructor function to initialize state
  // and using parent constuctor
  constructor(props) {
    super(props);

    // This is the only time to use direct assignment of state.
    this.state = {lat: null, errorMessage: '' };
  }

  render() {
    if (this.state.errorMessage && !this.state.lat) {
      return <div>Error: {this.state.errorMessage}</div>;
    }

    if (!this.state.errorMessage && this.state.lat) {
      return <div>Latitude: {this.state.lat}</div>;
    }
      
    return <div>Loading!</div>
  }

  componentDidMount() {
    window.navigator.geolocation.getCurrentPosition(
      (position) => {
        // Called setState (inherited by React.Component)
        this.setState({lat: position.coords.latitude});

        // Should not do direct access of attribute
        //this.state.late = position.coords.latitude;
      },
      err => {
        this.setState({errorMessage: err.message});
      }
    );
  }
}



ReactDOM.render(
  <App />,
  document.querySelector('#root')
);