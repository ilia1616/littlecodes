import React from 'react'
import CatPage from '../../components/category-page'
import { categories } from '../../data'

export default function the_page(specific_category) {
  return (
   <div className='App'>
      {categories.map((cat) =>
        cat.name === specific_category ? (
          <CatPage key={cat.id} name={cat.name} />
        ) : null
      )}
    </div>
  )
}
