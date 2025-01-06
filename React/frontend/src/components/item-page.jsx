import React from 'react'
import { useNavigate } from 'react-router-dom'

export default function ItemPage({itemName}) {
  const nav = useNavigate();
  return (
    <div><button onClick={() => nav('/')}>{itemName}</button></div>
  )
}
