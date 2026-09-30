from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "AI Recap Backend is running"
    })


@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({
        "success": True,
        "message": "Backend connection OK"
    })


@app.route("/api/recap", methods=["POST"])
def recap():
    data = request.get_json(silent=True) or {}

    video_url = data.get("video_url")
    recap_length = data.get("recap_length", "normal")
    ai_voice = data.get("ai_voice", True)
    original_audio = data.get("original_audio", False)
    myanmar_subtitle = data.get("myanmar_subtitle", True)
    clean_video = data.get("clean_video", False)
    mirror_video = data.get("mirror_video", False)

    if not video_url:
        return jsonify({
            "success": False,
            "error": "Video link is required"
        }), 400

    return jsonify({
        "success": True,
        "message": "Request received",
        "settings": {
            "video_url": video_url,
            "recap_length": recap_length,
            "ai_voice": ai_voice,
            "original_audio": original_audio,
            "myanmar_subtitle": myanmar_subtitle,
            "clean_video": clean_video,
            "mirror_video": mirror_video
        }
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )