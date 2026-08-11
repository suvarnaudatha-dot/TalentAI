import { useState } from "react";
import "./App.css";

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobFile, setJobFile] = useState(null);

  const [resumeData, setResumeData] = useState(null);
  const [jobData, setJobData] = useState(null);
  const [matchData, setMatchData] = useState(null);

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const API_URL = "http://127.0.0.1:8000";

  const uploadResume = async () => {
    if (!resumeFile) {
      setMessage("Please select a resume.");
      return null;
    }

    const formData = new FormData();
    formData.append("file", resumeFile);

    const response = await fetch(`${API_URL}/resume/upload`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Resume upload failed.");
    }

    return await response.json();
  };

  const uploadJobDescription = async () => {
    if (!jobFile) {
      setMessage("Please select a job description.");
      return null;
    }

    const formData = new FormData();
    formData.append("file", jobFile);

    const response = await fetch(`${API_URL}/job-description/upload`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Job description upload failed.");
    }

    return await response.json();
  };

  const analyzeAndMatch = async () => {
    if (!resumeFile || !jobFile) {
      setMessage("Please upload both Resume and Job Description.");
      return;
    }

    try {
      setLoading(true);
      setMessage("");

      const resume = await uploadResume();
      const job = await uploadJobDescription();

      setResumeData(resume);
      setJobData(job);

      const params = new URLSearchParams({
        resume_text: resume.extracted_text,
        job_description_text: job.job_description_text,
      });

      const response = await fetch(`${API_URL}/match/?${params}`, {
        method: "POST",
      });

      if (!response.ok) {
        throw new Error("Matching failed.");
      }

      const match = await response.json();
      setMatchData(match);

      setMessage("Analysis completed successfully!");
    } catch (error) {
      setMessage(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>TalentAI</h1>
          <p>Intelligent Recruitment & Resume Analysis Platform</p>
        </div>
      </header>

      <main className="container">
        <section className="hero">
          <h2>Resume & Job Matching</h2>
          <p>
            Upload a candidate resume and job description to analyze skills
            and calculate the matching score.
          </p>
        </section>

        <section className="upload-grid">
          <div className="upload-card">
            <div className="icon">📄</div>

            <h3>Upload Resume</h3>

            <p>Upload PDF or DOCX resume</p>

            <input
              type="file"
              accept=".pdf,.docx"
              onChange={(e) => setResumeFile(e.target.files[0])}
            />

            {resumeFile && (
              <div className="selected-file">
                Selected: {resumeFile.name}
              </div>
            )}
          </div>

          <div className="upload-card">
            <div className="icon">📋</div>

            <h3>Upload Job Description</h3>

            <p>Upload PDF or DOCX job description</p>

            <input
              type="file"
              accept=".pdf,.docx"
              onChange={(e) => setJobFile(e.target.files[0])}
            />

            {jobFile && (
              <div className="selected-file">
                Selected: {jobFile.name}
              </div>
            )}
          </div>
        </section>

        <div className="action-section">
          <button
            className="analyze-button"
            onClick={analyzeAndMatch}
            disabled={loading}
          >
            {loading ? "Analyzing..." : "Analyze & Match"}
          </button>

          {message && <p className="message">{message}</p>}
        </div>

        {matchData && (
          <section className="results">
            <h2>Analysis Results</h2>

            <div className="score-grid">
              {resumeData?.resume_score && (
                <div className="result-card">
                  <h3>Resume Score</h3>
                  <div className="score">
                    {resumeData.resume_score.score}
                    <span>/100</span>
                  </div>
                </div>
              )}

              <div className="result-card">
                <h3>Match Score</h3>
                <div className="score">
                  {matchData.match_score}
                  <span>/100</span>
                </div>
              </div>

              <div className="result-card">
                <h3>Recommendation</h3>
                <div className="recommendation">
                  {matchData.recommendation}
                </div>
              </div>
            </div>

            <div className="skills-section">
              <div className="skills-card">
                <h3>✅ Matched Skills</h3>

                {matchData.matched_skills.length > 0 ? (
                  <div className="skills-list">
                    {matchData.matched_skills.map((skill) => (
                      <span className="skill matched" key={skill}>
                        {skill}
                      </span>
                    ))}
                  </div>
                ) : (
                  <p>No matched skills found.</p>
                )}
              </div>

              <div className="skills-card">
                <h3>❌ Missing Skills</h3>

                {matchData.missing_skills.length > 0 ? (
                  <div className="skills-list">
                    {matchData.missing_skills.map((skill) => (
                      <span className="skill missing" key={skill}>
                        {skill}
                      </span>
                    ))}
                  </div>
                ) : (
                  <p>No missing skills.</p>
                )}
              </div>
            </div>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;