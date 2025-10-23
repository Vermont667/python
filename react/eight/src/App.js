import { Routes, Route, Navigate } from 'react-router-dom';
import './App.css';
import Home from './DZ/Home';
import About from './About';
import Articles from './Articles';
import Layout from './components/Layout';
import AboutInfo from './AboutInfo';
import NotFoundPage from './NotFoundPage';

function App() {
  return (
    <div>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<Home />} />
          <Route path='about' element={<About />} />
          <Route path='about/:id' element={<AboutInfo />} />
          <Route path='articles' element={<Articles />} />
          <Route path='articles-us' element={<Navigate to='/articles' replace />} />
          <Route path='*' element={<NotFoundPage />} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
