import React from 'react'
import { useNavigate, useParams } from 'react-router-dom'

export default function ItemPage() {
  const nav = useNavigate();
  let {itemName} = useParams();
  return (
    <div><button onClick={() => nav('/')}>{itemName}</button></div>
  )
}
