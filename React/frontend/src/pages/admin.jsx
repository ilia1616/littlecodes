import React from 'react'
import { useNavigate } from 'react-router-dom';

export default function Admin() {
    const nav = useNavigate(); 
    function handleSubmit (e) {
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);

        //   fetch('/some-api', { method: form.method, body: formData }); از این برای فرستادن http req استفاده کن
        const formJson = Object.fromEntries(formData.entries());
        console.log(formJson);
    }
  return (
    <form method='post' onSubmit={handleSubmit}>
        <button onClick={() => nav('/')}>BACK</button>
        <p>Item name</p>
        <input name='item name' />
         <p>Category</p>
         <input name='item category' />
         <button type="submit">Submit</button>
    </form>
  )
}
