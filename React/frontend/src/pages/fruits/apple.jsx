import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function Apple() {
  const nav = useNavigate();
  return (
    <div><button onClick={() => nav('/')}>Apple</button></div>
  )
}
