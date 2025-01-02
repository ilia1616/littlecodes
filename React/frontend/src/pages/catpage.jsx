import React from 'react';
import { categories } from '../data';
import { useNavigate } from 'react-router-dom';

const ThePage = ({ specific_category }) => {
  const filteredItems = categories.filter((item) => item.categorie === specific_category);
  const nav = useNavigate(); 

  return (
    <div>
      <button onClick={() => nav('/')}>BACK</button>
      <h1>{specific_category}</h1>
      {filteredItems.length > 0 ? (
        <ul>
          {filteredItems.map((item) => (
            <li key={item.id}><button onClick={() => nav(`/${specific_category}/${item.name}`)}>
              {item.name}
            </button></li>
          ))}
        </ul>
      ) : (
        <p>No items found for this category.</p>
      )}
    </div>
  );
};

export default ThePage;
