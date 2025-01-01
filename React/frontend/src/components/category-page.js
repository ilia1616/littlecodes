import React from "react";
import { useNavigate } from "react-router-dom";

const CatPage = ({id,name}) => {
    const nav = useNavigate();

    return (
        <div className="category-box">
            <ul>
                <li key={id}>
                    <button onClick={() => nav(`/${name}`)}>{name}</button>
                </li>
            </ul>
        </div>
    );
};

export default CatPage;