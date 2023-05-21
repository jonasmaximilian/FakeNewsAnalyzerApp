import { useState } from 'react'

function App() {

  const [inputField, setInputField] = useState<string>("");
  const [output, setOutput] = useState<string>("Initializer");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    console.log(inputField);

    // setOutput("Loading...")

    // send inputField to Flask backend
    // const response = await fetch("http://127.0.0.1:5000/predict", {
    //   mode: "no-cors",
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify({ inputField }),
    //   });

    //   // get response from Flask backend
    //   const data = await response.json();
    //   setOutput(data.output);

    // fetch ("http://127.0.0.1:5000/predict", {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify({ inputField }),
    //   })
    //   .then(response => response.json())
    //   .then(data => setOutput(data.output))
    //   .catch(error => console.log(error))

    const response = fetch ("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify({ inputField }),
      })
      const data = await response.then(response => response.json());
      console.log(data);
      console.log("calling setOutput");
      console.log(data.error);
      if (data.error) {
        setOutput(data.error);
      }
      else {
        setOutput(data.prediction);
      }



      // setInputField("");


  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputField}
          onChange={(e) => setInputField(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      <p>{output}</p>
    </div>
  );
}

export default App
