import React from 'react'
import CatBox from '../components/cat-box';

export default function Home() {
    
    return (
        <div className='App'>
            <CatBox catName="fruits" />
            <CatBox catName="labaniat" />
            <CatBox catName="shoyande" />
        </div>
);
}