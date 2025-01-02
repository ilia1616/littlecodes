import React from 'react'
import CatBox from '../components/cat-box';
import CategoryButton from '../components/categoryButton';

export default function Home() {
    
    return (
        <div className='App'>
            <CatBox catName="fruits" />
            <CatBox catName="labaniat" />
            <CatBox catName="shoyande" />
            <CategoryButton categoryName={"fruits"} />
            <CategoryButton categoryName={"labaniat"} />
            <CategoryButton categoryName={"shoyande"} />
        </div>
);
}