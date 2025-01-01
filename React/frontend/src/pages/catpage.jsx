import React from 'react';
import { categories } from '../data';

const ThePage = ({ specific_category }) => {
  const filteredItems = categories.filter((item) => item.categorie === specific_category);

  return (
    <div>
      <h1>{specific_category}</h1>
      {filteredItems.length > 0 ? (
        <ul>
          {filteredItems.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      ) : (
        <p>No items found for this category.</p>
      )}
    </div>
  );
};

export default ThePage;
