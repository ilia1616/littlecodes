import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { fetchItemsByCategory, itemsData } from '../components/data';

const ThePage = ({ specific_category }) => {
  const [loading, setLoading] = useState(true); // State to handle loading
  const [error, setError] = useState(null); // State to handle errors
  const nav = useNavigate();

  // Fetch items by category when the component mounts or the category changes
  useEffect(() => {
    const fetchData = async () => {
      try {
        await fetchItemsByCategory(specific_category);
        setLoading(false);
      } catch(error) {
        console.error('Error: ', error);
        setError(error);
        setLoading(false);
      }
    };
    fetchData();

  } , [specific_category]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <button onClick={() => nav('/')}>BACK</button>
      <h1>{specific_category}</h1>
      {itemsData.length > 0 ? (
        <ul>
          {itemsData.map((item) => (
            <li key={item.id}>
              <button onClick={() => nav(`/${specific_category}/${item.name}`)}>
                {item.name}
              </button>
            </li>
          ))}
        </ul>
      ) : (
        <p>No items found for this category.</p>
      )}
    </div>
  );
};

export default ThePage;