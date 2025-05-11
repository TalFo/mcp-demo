from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask_llm', methods=['POST'])
def ask_llm():
    data = request.json
    prompt = data.get("prompt", "")
    mcp = data.get("mcp", {})

    role = mcp.get("user_role", "user")
    if role == "admin":
        response = "🚨 Salary: $180,000 plus bonus access."
    elif role == "manager":
        response = "📊 Salary: $120,000 (view-only)."
    else:
        response = "⛔ Access denied. You are not allowed to view this information."

    return jsonify({
        "mcp_used": mcp,
        "response": response
    })

if __name__ == '__main__':
    app.run(debug=True)
