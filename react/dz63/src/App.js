import Albom from './Albom';
import './App.css';
import music from './mus.json'
import im from './ab67616d0000b273c929527eb03eaf1cd9e990a5.jpg'


let mus = music.music;

function App() {
  return (
    <header>
      <div className='d'>
        <img src={im} alt="" />
        <h2>Психотерапия. Байки на кушетке</h2>
        <h3>2rbina 2rista</h3>
        <h4>2024</h4>
      </div>
      <div className="App">
        <Albom music={mus} />
      </div>
    </header>
  );
}

export default App;
