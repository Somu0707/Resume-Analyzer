import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const [score, setScore] = useState(0);
  const [skills, setSkills] = useState([]);
  const [missing, setMissing] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [resumeText, setResumeText] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a PDF Resume");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const res = await axios.post(
        "http://127.0.0.1:5000/upload",
        formData
      );

      setMessage(res.data.message);
      setScore(res.data.score);
      setSkills(res.data.skills);
      setMissing(res.data.missing);
      setSuggestions(res.data.suggestions);
      setResumeText(res.data.text);

    } catch (err) {
      if (err.response)
        setMessage(err.response.data.error);
      else
        setMessage("Server Error");
    }
  };

  return (
    <div className="container">

      <h1>Resume Analyzer</h1>

      <div className="uploadCard">

        <input
          type="file"
          accept=".pdf"
          onChange={(e)=>setFile(e.target.files[0])}
        />

        <button onClick={handleUpload}>
          Analyze Resume
        </button>

        <p className="message">{message}</p>

      </div>

      {score>0 && (

      <>

      <div className="scoreCard">

          <h2>ATS SCORE</h2>

          <div className="circle">

              {score}%

          </div>

      </div>

      <div className="grid">

      <div className="card">

      <h2>Skills Found</h2>

      {skills.map((skill,index)=>(

      <span className="greenTag" key={index}>
      {skill}
      </span>

      ))}

      </div>

      <div className="card">

      <h2>Missing Skills</h2>

      {missing.map((skill,index)=>(

      <span className="redTag" key={index}>
      {skill}
      </span>

      ))}

      </div>

      </div>

      <div className="card">

      <h2>Suggestions</h2>

      <ul>

      {suggestions.map((s,index)=>(

      <li key={index}>{s}</li>

      ))}

      </ul>

      </div>

      <div className="card">

      <h2>Extracted Resume</h2>

      <pre>{resumeText}</pre>

      </div>

      </>

      )}

    </div>
  );
}

export default App;

