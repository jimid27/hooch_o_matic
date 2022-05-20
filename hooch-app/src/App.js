import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <img src="/hooch.png" alt="hooch" width="1000" height="400" />
      <form>
        <label>
          How many days from now are you shooting the Hooch?
          <input type="text" name="days-till-hooch" />
        </label>
        < br/>
        <label>
          What time (military) are you lookin to start Hooching?
          <input type="text" name="start-time" />
        </label>
        < br/>
        <label>
          What time (military) are you planning on getting off the Hooch? (If ever)
          <input type="text" name="end-time" />
        </label>
        < br/>
        <label>
          How many people are annihilating the Chattahoochie? 
          <input type="text" name="num-people" />
        </label>
        < br/>
        <label>
          Is Jake bringing a Date for Real?
          <input type="text" name="jakes-date" />
        </label>
        < br/>
        <label>
          How many canned Bevvies do you have?
          <input type="text" name="bevvies" />
        </label>
        < br/>
        <label>
          Bringing any Franzia with you?
          <input type="text" name="franzia" />
        </label>
        < br/>
        <label>
          True or False - The Vibes are High this weekend
          <input type="text" name="jakes-date" />
        </label>
        < br/>
        < br/>
        <input type="submit" value="Submit" />
      </form>
      </header>
    </div>
  );
}

export default App;
