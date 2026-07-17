import './App.css'

function App() {
  return (
    <main className="about-page">
      <section className="hero-card">
        <p className="eyebrow">Hello, I’m</p>
        <h1>Your Name</h1>
        <p className="subtitle">Frontend developer • Lifelong learner • Problem solver</p>
        <p className="description">
          I build thoughtful web experiences that are clean, modern, and easy to use.
          I enjoy turning ideas into polished interfaces and learning new tools along the way.
        </p>
        <div className="actions">
          <a href="mailto:you@example.com">Contact Me</a>
          <a href="https://github.com" target="_blank" rel="noreferrer">
            View GitHub
          </a>
        </div>
      </section>

      <section className="info-grid">
        <article>
          <h2>About Me</h2>
          <p>
            I’m passionate about creating user-friendly products and bringing creativity
            into every project I touch.
          </p>
        </article>
        <article>
          <h2>Skills</h2>
          <ul>
            <li>React</li>
            <li>JavaScript</li>
            <li>CSS & UI Design</li>
            <li>Git & GitHub</li>
          </ul>
        </article>
        <article>
          <h2>Interests</h2>
          <p>Design systems, photography, travel, and building things that make life easier.</p>
        </article>
      </section>
    </main>
  )
}

export default App
