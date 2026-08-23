import { useRef, useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");

  const fileInputRef = useRef(null);

  const handleChooseFile = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please choose a PDF first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post(
        "https://redvault-ai-backend.onrender.com/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log(response.data);
      setUploadStatus("✅ PDF uploaded successfully!");
    } catch (error) {
      console.error(error);
      setUploadStatus("❌ Upload failed.");
    }
  };

  const handleAskAI = async () => {
    if (!question.trim()) {
      alert("Please enter a question.");
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post(
        "https://redvault-ai-backend.onrender.com/chat",
        {
          question: question,
        }
      );

      setAnswer(response.data.answer);

    } catch (error) {
      console.error(error);
      setAnswer("❌ Something went wrong.");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-black text-white flex justify-center p-10">
      <div className="w-full max-w-4xl">

        <h1 className="text-5xl font-bold text-center text-red-600 mb-10">
          RedVault AI
        </h1>

        {/* Upload */}

        <div className="bg-zinc-900 rounded-xl p-8 shadow-lg mb-8">

          <h2 className="text-2xl mb-6">
            Upload PDF
          </h2>

          <input
            ref={fileInputRef}
            type="file"
            accept=".pdf"
            onChange={handleFileChange}
            className="hidden"
          />

          <button
            onClick={handleChooseFile}
            className="bg-red-600 hover:bg-red-700 px-6 py-3 rounded-lg font-semibold"
          >
            Choose PDF
          </button>

          {selectedFile && (
            <p className="mt-4 text-green-400">
              📄 {selectedFile.name}
            </p>
          )}

          <button
            onClick={handleUpload}
            className="mt-6 bg-red-600 hover:bg-red-700 px-6 py-3 rounded-lg font-semibold"
          >
            Upload
          </button>

          {uploadStatus && (
            <p className="mt-4 text-green-400">
              {uploadStatus}
            </p>
          )}

        </div>

        {/* Chat */}

        <div className="bg-zinc-900 rounded-xl p-8 shadow-lg">

          <h2 className="text-2xl mb-4">
            Ask AI
          </h2>

          <input
            type="text"
            placeholder="Ask something about your document..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            className="w-full p-4 rounded-lg bg-zinc-800 border border-zinc-700 mb-5"
          />

          <button
            onClick={handleAskAI}
            className="bg-red-600 hover:bg-red-700 px-6 py-3 rounded-lg font-semibold"
          >
            Send
          </button>

          <div className="mt-8 bg-zinc-800 rounded-lg p-6">

            <h3 className="text-red-500 font-bold mb-3">
              AI Response
            </h3>

            {loading ? (
              <p>🤖 Thinking...</p>
            ) : (
              <p className="whitespace-pre-wrap">
                {answer || "Your answer will appear here..."}
              </p>
            )}

          </div>

        </div>

      </div>
    </div>
  );
}

export default App;