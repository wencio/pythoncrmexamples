import React, { useState } from "react";
import axios from 'axios';

function PropertyInput(props) {
  const [street, setStreet] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [zip, setZip] = useState("");
  const [bedrooms, setBedrooms] = useState(0);
  const [bathrooms, setBathrooms] = useState(0);
  const [price, setPrice] = useState(0);

  const handleSubmit = (event) => {
    event.preventDefault();
   
    axios.post('/api/crm', {
      street,
      city,
      state,
      zip,
      bedrooms,
      bathrooms,
      price
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
        Street:
        <input type="text" value={street} onChange={(e) => setStreet(e.target.value)} />
      </label>
      <label>
        City:
        <input type="text" value={city} onChange={(e) => setCity(e.target.value)} />
      </label>
      <label>
        State:
        <input type="text" value={state} onChange={(e) => setState(e.target.value)} />
      </label>
      <label>
        Zip:
        <input type="text" value={zip} onChange={(e) => setZip(e.target.value)} />
      </label>
      <label>
        Bedrooms:
        <input type="number" value={bedrooms} onChange={(e) => setBedrooms(parseInt(e.target.value))} />
      </label>
      <label>
        Bathrooms:
        <input type="number" value={bathrooms} onChange={(e) => setBathrooms(parseInt(e.target.value))} />
      </label>
      <label>
        Price:
        <input type="number" value={price} onChange={(e) => setPrice(parseInt(e.target.value))} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}

