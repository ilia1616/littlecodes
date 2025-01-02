import React from "react";
import { useNavigate } from "react-router-dom";

const ItemButton = ({ id, category, name }) => {
    const nav = useNavigate();

    return (
        <li key={id}>
            <button onClick={() => nav(`/${category}/${name}`)}>
                {name}
            </button>
        </li>
    );
};

export default ItemButton;