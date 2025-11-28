from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aditya Jha - Resume</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eaeaea;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
        }
        h1 {
            color: #222;
            margin-bottom: 5px;
        }
        h3 {
            color: #444;
            margin-top: 0;
        }
        .section {
            margin-top: 30px;
        }
        .section h2 {
            color: #333;
            margin-bottom: 10px;
        }
        .line {
            height: 2px;
            background: #222;
            width: 60px;
            margin-bottom: 15px;
        }
        ul {
            line-height: 1.7em;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Aditya Jha</h1>
        <h3>B.Tech (CSE - AI/ML), Vivekananda Global University</h3>

        <div class="section">
            <h2>About Me</h2>
            <div class="line"></div>
            <p>I am a passionate B.Tech CSE (AI/ML) student at VGU, interested in Python development, web development, machine learning, projects, and problem-solving.</p>
        </div>

        <div class="section">
            <h2>Skills</h2>
            <div class="line"></div>
            <ul>
                <li>Python (Flask, Projects, DSA Basics)</li>
                <li>HTML, CSS, JavaScript</li>
                <li>Machine Learning Basics</li>
                <li>Git & GitHub</li>
                <li>Problem Solving</li>
            </ul>
        </div>

        <div class="section">
            <h2>Education</h2>
            <div class="line"></div>
            <p><strong>Bachelor of Technology (B.Tech)</strong><br>
            Vivekananda Global University (VGU), Jaipur<br>
            CSE – AI/ML (2024 - 2028)</p>
        </div>

        <div class="section">
            <h2>Projects</h2>
            <div class="line"></div>
            <ul>
                <li>Python Calculator with Exception Handling</li>
                <li>ATM Program with Password Blocking</li>
                <li>Student Grade Management System</li>
                <li>Voice Assistant (Bixby-style)</li>
            </ul>
        </div>

        <div class="section">
            <h2>Contact</h2>
            <div class="line"></div>
            <p>Email: adityajha@example.com</p>
            <p>Phone: +91 9876543210</p>
        </div>

    </div>

</body>
</html>

    """

if __name__ == '__main__':
    app.run(debug=True)


         
