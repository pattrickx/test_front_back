import logo from './logo.svg';
import axios from "axios";
import './App.css';

function App() {

  async function getCredits(){
    let config = {
      method: 'get',
      url: 'http://localhost:5000/hello',
      responseType: 'text',
      headers: { 'content-type': 'application/x-www-form-urlencoded' },
    };
    await axios(config)
    .then(function (response) {
        console.log(response)
    })
    .catch(function (error) {
      console.log(error);
    });
     
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button type="button" onClick={()=>getCredits()}>API!!!!!</button>
      </header>
    </div>
  );
}

export default App;
