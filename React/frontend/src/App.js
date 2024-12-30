import './App.css';
import Home from './pages/home'
import Test from './pages/test1'
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";

function App() {
    return (
        <Router>
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/test" element={<Test />} />
            </Routes>
        </Router>
    );
}

export default App;
