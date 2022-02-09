import logo from './logo.svg';
import axios from "axios";
import './App.css';

function App() {
  let token
  async function getCredits(){

    let config = {
      method: 'get',
      url: 'https://back.knowcode.app/login',
      responseType: 'text',
      headers: { 'content-type': 'application/x-www-form-urlencoded' },
    };
    await axios(config)
    .then(function (response) {
      token = response.data.token
        console.log(response)
    })
    .catch(function (error) {
      console.log(error.response);
    });

  }

  async function test(){

   
    let config = {
      method: 'get',
      url: 'http://localhost:5000/hello',
      responseType: 'text',
      headers: { 'content-type': 'application/x-www-form-urlencoded',
                  'x-access-token':token },
    };
    await axios(config)
    .then(function (response) {
        console.log(response)
    })
    .catch(function (error) {
      console.log(error.response.data.message);
    });

  }
  return (
    <div className="App">
      <header className="App-header">
        
        <button type="button" onClick={()=>getCredits()}>LOGIN</button>
        <button type="button" onClick={()=>test()}>TEST</button>
      </header>
    </div>
  );
}

export default App;
