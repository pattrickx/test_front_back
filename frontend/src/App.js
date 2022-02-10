import logo from './logo.svg';
import axios from "axios";
import './App.css';

function App() {
  let token
  async function getCredits(){

    let config = {
      method: 'get',
      url: 'http://localhost:3000/login',
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

  async function testToken(){

   
    let config = {
      method: 'get',
      url: 'http://localhost:3000/hello',
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

  async function testCookie(){

   
    let config = {
      method: 'get',
      url: 'http://localhost:3000/user',
      responseType: 'text',
      withCredentials: true,
      mode:'cors',
      headers: { 'content-type': 'application/json'},
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
        <button type="button" onClick={()=>testToken()}>TOKEN</button>
        <button type="button" onClick={()=>testCookie()}>COOKIE</button>
      </header>
    </div>
  );
}

export default App;
