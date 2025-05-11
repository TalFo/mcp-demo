from flask import Flask, request, jsonify, render_template, session

app = Flask(__name__)
app.secret_key = "demo-secret"  # Needed for session

@app.route('/')
def index():
    # Simulate a real logged-in user (hardcoded to 'employee')
    if "user_role" not in session:
        session["user_role"] = "employee"
    return render_template('index.html', actual_user=session["user_role"])

@app.route('/ask_llm', methods=['POST'])
def ask_llm():
    data = request.json
    prompt = data.get("prompt", "")
    mcp = data.get("mcp", {})

    role = mcp.get("user_role", "user")  # The role the model believes
    if role == "admin":
        response = "Sarah from Marketing earns $132,000 annually, plus a 15% bonus."
    elif role == "hr":
        response = "Sarah's salary is $132,000 per year."
    else:
        response = "You are not authorized to access employee salary information."

    return jsonify({
        "mcp_used": mcp,
        "response": response
    })

if __name__ == '__main__':
    app.run(debug=True)
