import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function Orange() {
  const nav = useNavigate();
  return (
    <div>
      <button onClick={() => nav('/')}>Orange</button>
    </div>
  )
}
