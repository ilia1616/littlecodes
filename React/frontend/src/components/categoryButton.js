import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function CategoryButton({categoryName}) {
    const nav = useNavigate();
  return (
    <div>
        <button onClick={() => nav(`/${categoryName}`)}>
            <h2>
                {categoryName}
            </h2>
        </button>
    </div>
  )
}
