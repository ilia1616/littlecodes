import React, {useState, useEffect} from "react";
import ItemButton from "./item-button";
import { itemsData,fetchItemsByCategory } from "./data";


const CatBox = ({ catName }) => {
    // Filter items by the provided category name
    const [loading, setLoading] = useState(true); // State to handle loading
    const [error, setError] = useState(null); // State to handle errors
    // const grouped = categories.filter((item) => item.categorie === catName);
    useEffect(() => {
    const fetchData = async () => {
      try {
        await fetchItemsByCategory(catName);
        setLoading(false);
      } catch(error) {
        console.error('Error: ', error);
        setError(error);
        setLoading(false);
      }
    };
    fetchData();

  } , [catName]);
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    return (
        <div className="category-box">
            <h1>{catName}</h1>
            <ul>
                {itemsData.map((item) => (
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