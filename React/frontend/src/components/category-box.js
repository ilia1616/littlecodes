import React from "react";
import { useNavigate } from "react-router-dom";

const CategoryBox = ({category, items}) => {
    const nav = useNavigate();

    return(
        <div className="category-box">
            <h2>{category}</h2>
            <ul>
                {items.map((item,index) => 
                <li key={index}>
                    <button onClick={() => nav("http://localhost:3000/" + {item})}>

                    </button>
                    </li>
                )}
            </ul>
        </div>
    );
};

export default CategoryBox;