import './App.css';
import Home from './pages/home'
import Banana from './pages/fruits/banana'
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import Apple from './pages/fruits/apple';
import Orange from './pages/fruits/orange';
import ThePage from './pages/catpage';

function App() {
    return (
        <Router>
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/fruits/banana" element={<Banana />} />
                <Route path="/fruits/apple" element={<Apple />} />
                <Route path="/fruits/orange" element={<Orange />} />
                <Route path="/fruits" element={<ThePage specific_category="fruits" /> } />
            </Routes>
        </Router>
    );
}

export default App;
