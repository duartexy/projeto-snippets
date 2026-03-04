import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [snippets, setSnippets] = useState([])

  // Função para buscar os códigos lá no nosso Backend Django
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/snippets/')
      .then(response => response.json())
      .then(data => setSnippets(data))
      .catch(error => console.error('Erro ao buscar snippets:', error))
  }, [])

  return (
    <div className="App">
      <h1>VibeCode 💻</h1>
      <p>Meus trechos de código favoritos:</p>
      
      <div className="snippets-list">
        {snippets.map(snippet => (
          <div key={snippet.id} className="snippet-card">
            <h3>{snippet.titulo}</h3>
            <pre><code>{snippet.codigo}</code></pre>
            <small>Linguagem: {snippet.linguagem}</small>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App