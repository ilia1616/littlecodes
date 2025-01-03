import React from 'react'
import CatBox from '../components/cat-box';
import CategoryButton from '../components/categoryButton';
import { useNavigate } from 'react-router-dom';

export default function Home() {
    const nav = useNavigate();

    return (
        <div className='App'>
            <button onClick={() => nav('/admin')}>Admin</button>
            <CategoryButton categoryName={"fruits"} />
            <CategoryButton categoryName={"labaniat"} />
            <CategoryButton categoryName={"shoyande"} />
            <CatBox catName="fruits" />
            <CatBox catName="labaniat" />
            <CatBox catName="shoyande" />
        </div>
);
}