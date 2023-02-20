import React, { useState } from 'react';
import axios from 'axios';

function CRMForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [address, setAddress] = useState('');


  const handleSubmit = (event) => {
    event.preventDefault();

    axios.post('/api/crm', {
      name,
      email,
      phone,
      address
    })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={event => setName(event.target.value)} />
      </label>
      <br />
      <label>
        Email:
        <input type="email" value={email} onChange={event => setEmail(event.target.value)} />
      </label>
      <br />
      <label>
        Phone:
        <input type="tel" value={phone} onChange={event => setPhone(event.target.value)} />
      </label>
      <br />
      <label>
        Address:
        <input type="address" value={address} onChange={event => setAddress(event.target.value)} />
      </label>
      <br />
      <button type="submit">Save</button>
    </form>
  );
}
