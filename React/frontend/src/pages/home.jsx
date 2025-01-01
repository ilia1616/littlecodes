import React from 'react'
import CategoryBox from '../components/category-box';
import { categories } from '../data';

export default function Home() {

    return (
        <div className='App'>
            <h1>Categories</h1>
            {categories.map((cat) => 
            // (<CategoryBox key={index} category={cat.categorie} items={cat.items} />))}
            (<CategoryBox key={cat.id} category={cat.categorie} name={cat.name} />))}
        </div>
);
}