import React from 'react'
import './Card.css'
const Card = () => {
    let name="vasavi";
    let email="gvasi123@gmail.com";
    let phno="1234567890";
  return (
    <div className='Parent'>
      <h1>name: {name}</h1>
      <h1>Email: {email}</h1>
      <h1>Phone: {phno}</h1>
    </div>
  )
}

export default Card