import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function Banana() {
  const nav = useNavigate();
  return (
    <div><button onClick={() => nav('/')}>Banana</button></div>
  )
}
