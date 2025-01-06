import React from 'react'
import { useNavigate } from 'react-router-dom';

export default function Admin() {
    const nav = useNavigate(); 
    function handleSubmit (e) {
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);
        const formJson = Object.fromEntries(formData.entries());
        console.log(formJson);

      fetch('http://localhost:8000/api/create/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // Set the content type to JSON
      },
      body: JSON.stringify(formJson), // Convert the form data to JSON
    })
    .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json(); // Parse the JSON response
      })
      .then((data) => {
        console.log('Item added successfully:', data);
        alert('Item added successfully!');
        nav('/'); // Navigate back to the home page after successful submission
      })
      .catch((error) => {
        console.error('Error:', error);
        alert('Failed to add item.');
      });
    }
  return (
    <form method='post' onSubmit={handleSubmit}>
        <button onClick={() => nav('/')}>BACK</button>
        <p>ID</p>
        <input name='id' />
        <p>Item name</p>
        <input name='name' />
         <p>Category</p>
         <input name='category' />
         <button type="submit">Submit</button>
    </form>
  )
}
