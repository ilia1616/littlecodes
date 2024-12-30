import React from 'react'
import CategoryBox from '../components/category-box';

export default function Home() {
    const categories = [{
        categorie: 'Fruits',
        items: ['banana','apple','orange']
    },
    {
        categorie: 'moz',
        items: ['banana1','banana2','banana3']
    }    
];
    return (
        <div className='App'>
            <h1>Categories</h1>
            {categories.map((cat, index) => 
            (<CategoryBox key={index} category={cat.categorie} items={cat.items} />))}
        </div>
);
}