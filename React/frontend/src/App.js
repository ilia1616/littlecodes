import './App.css';
import Home from './pages/home'
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import ThePage from './pages/catpage';
import Admin from './pages/admin';
import ItemPage from './components/item-page';


function App() {

    return (
        <Router>
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route path="/admin" element={<Admin />} />
                <Route path="/fruits" element={<ThePage specific_category="fruits" /> } />
                <Route path="/labaniat" element={<ThePage specific_category="labaniat" /> } />
                <Route path="/fruits/:itemName" element={<ItemPage />} />
                <Route path="/labaniat/:itemName" element={<ItemPage />} />
                <Route path="/shoyande/:itemName" element={<ItemPage />} />
                {/* <Route path="/fruits/" element={<ItemPage itemName="banana" />} />
                <Route path="/fruits/apple" element={<ItemPage itemName="apple" />} />
                <Route path="/fruits/orange" element={<ItemPage itemName="orange" />} />
                <Route path="/labaniat/shir" element={<ItemPage itemName="shir" />} />
                <Route path="/labaniat/kareh" element={<ItemPage itemName="kareh" />} /> */}
            </Routes>
        </Router>
    );
}

export default App;
