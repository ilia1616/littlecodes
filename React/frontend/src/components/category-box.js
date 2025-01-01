import React from "react";
import { useNavigate } from "react-router-dom";

const CategoryBox = ({id, category, name}) => {
    const nav = useNavigate();

    return(
        <div className="category-box">
            <h2>{category}</h2>
            <ul>
                {/* {items.map((item,id) =>  */}
                <li key={id}>
                    <button onClick={() => nav(`/${category}/${name}`)}>
                    {name}
                    </button>
                    </li>
                {/* )} */}
            </ul>
        </div>
    );
};

export default CategoryBox;