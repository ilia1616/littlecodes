import React from "react";

const CategoryBox = ({category, items}) => {
    return(
        <div className="category-box">
            <h2>{category}</h2>
            <ul>
                {items.map((item,index) => 
                <li key={index}>{item}</li>
                )}
            </ul>
        </div>
    );
};

export default CategoryBox;