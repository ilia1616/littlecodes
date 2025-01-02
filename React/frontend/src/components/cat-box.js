import React from "react";
import { categories } from "../data";
import ItemButton from "./item-button";

const CatBox = ({ catName }) => {
    // Filter items by the provided category name
    const grouped = categories.filter((item) => item.categorie === catName);

    return (
        <div className="category-box">
            <h1>{catName}</h1>
            <ul>
                {grouped.map((item) => (
                    <ItemButton
                        key={item.id}
                        id={item.id}
                        category={item.category}
                        name={item.name}
                    />
                ))}
            </ul>
        </div>
    );
};

export default CatBox;