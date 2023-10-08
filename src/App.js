import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
function App() {
  const [img, setImg] = useState(null);

  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState(null);


  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent the default form submission behavior

    if (!file) {
      console.log('Please select a file');
      return;
    }

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post('http://127.0.0.1:5000/uploader', formData);
      console.log('Form submitted successfully');
      fetchImage()

      // Additional actions after successful form submission
    } catch (error) {
      console.error('Error submitting the form:', error);
      // Additional error handling if needed
    }
  };

  const handleFileChange = (event) => { 
    setFile(event.target.files[0]);
    setFileName(event.target.files[0].name);

  };

  const fetchImage = async () => {
    const res = await fetch("/photo/"+fileName);
    const imageBlob = await res.blob();
    const imageObjectURL = URL.createObjectURL(imageBlob);
    setImg(imageObjectURL);
  };
  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit} encType="multipart/form-data">
          <input type="file" name="file" onChange={handleFileChange} />
          <input type="submit" value="Submit" />
        </form>
        <img src={img} />
      </header>
    </div>
  );
}

export default App;
