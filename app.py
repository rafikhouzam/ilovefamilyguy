from flask import Flask, jsonify, request, render_template
import json
import random
import os

app = Flask(__name__)

episodes = {
    "S3E18": {
        "season": 3,
        "episode": 18,
        "name": "From Method to Madness",
        "description": "Stewie signs up for an acting class, where he's paired up with a stuck-up child star named Olivia. They become a hit, though the fame quickly sets in and they soon start bickering. Meanwhile, Peter and Lois object to Meg dating a nudist, though later have second thoughts after seeing her upset."
    },
    "S3E19": {
        "season": 3,
        "episode": 19,
        "name": "Stuck Together, Torn Apart",
        "description": "Peter and Lois are advised to go through a trial separation after Peter becomes jealous over Lois reuniting with an old boyfriend, and he hooks up with Jennifer Love Hewitt. Meanwhile, Stewie and Brian get stuck together after Stewie plays around with industrial-strength glue."
    },
    "S6E04": {
        "season": 6,
        "episode": 4,
        "name": "Stewie Kills Lois (1)",
        "description": "Lois and Peter go on a cruise, leaving Stewie and the family behind. Upset with Lois for leaving him at home, Stewie vows to carry out a diabolical plan."
    },
    "S6E05": {
        "season": 6,
        "episode": 5,
        "name": "Lois Kills Stewie (2)",
        "description": "Just as Lois was presumed dead by Peter's hand, with Peter about to be jailed for life, she makes a miraculous return from the wilderness and names Stewie as her killer. From there, Stewie escapes the law, where he ties up the family and reveals his true nature. He forces Brian into helping him fulfill his lifelong goal of taking over the world, and succeeds when Stan Smith and the CIA submit to his threats. After suffering several days under Stewie's reign, Lois decides she has no choice but to arm herself to kill Stewie and save the world."
    },
    "S8E01": {
        "season": 8,
        "episode": 1,
        "name": "Road to the Multiverse",
        "description": "Stewie shows Brian a remote control that allows him to access parallel universes depicting Quahog in the same time and place, but under different conditions."
    },
    "S8E17": {
        "season": 8,
        "episode": 17,
        "name": "Brian and Stewie",
        "description": "Brian and Stewie get locked in a bank vault and become trapped. Brian wakes up in the middle of the night and opens a bottle of scotch. When he accidentally wakes up Stewie, they share the scotch and get really emotional."
    },
    "S9E01": {
        "season": 9,
        "episode": 1,
        "name": "And Then There Were Fewer",
        "description": "The residents of Quahog are invited over to a honorary dinner at James Woods' mansion, a mystery episode."
    },
    "S9E14": { 
        "season": 9,
        "episode": 14,
        "name": "Tiegs for Two",
        "description": "Brian tries to score on a date with a new friend, Denise, but ends up striking out. Instead of throwing in the towel, he decides to enlist Quagmire’s help through the latter's new class on how to score women."
    },
    "S9E17": {
        "season": 9,
        "episode": 17,
        "name": "Foreign Affairs",
        "description": "Bonnie and Lois go to Paris, but Lois finds out that Bonnie only wants to go there to have an affair. After Joe discovers Bonnie's plans, he travels to Paris to try to get her back."
    },
    "S10E17": {
        "season": 10,
        "episode": 17,
        "name": "Forget-Me-Not",
        "description": "Basically, Lois claims that Brian is just taking Peter's side because they hang out and would never have met if it wasn't for circumstance."
    },
    "S11E15": {
        "season": 11,
        "episode": 15,
        "name": "Turban Cowboy",
        "description": "After a skydiving accident, Peter becomes friends with a Muslim man who convinces Peter to convert to Islam, leaving Joe and Quagmire with suspicions about this new friend."
    },
    "S15E08": {
        "season": 15,
        "episode": 8,
        "name": "Carter and Tricia",
        "description": "Peter tells Tricia Takanawa about Carter's plan to use toxic chemicals in Pawtucket Patriot when Carter buys the brewery. Meanwhile, Brian's driver's license expires, and he gets help from Stewie to renew it."
    },
    "S15E09": {
        "season": 15,
        "episode": 9,
        "name": "How the Griffin Stole Christmas",
        "description": "Peter becomes a mall Santa, and he becomes drunk with power when he learns that he can get away with anything, but the real Santa is mad about this and takes direct action to stop Peter. Meanwhile, Stewie and Brian crash Christmas parties for free food, drama, and women."
    },
    "S15E20": {
        "season": 15,
        "episode": 20,
        "name": "A House Full of Peters",
        "description": "After Lois discovers that Peter was a sperm donor in his youth, Peter's past comes back to him when many of his children unexpectedly come to his house – one of whom wants to usurp his place as Lois' husband."
    },
    "S16E12": {
        "season": 16,
        "episode": 12,
        "name": "Send in Stewie, Please",
        "description": "Stewie sees a therapist."
    },
    "S17E11": {
        "season": 17,
        "episode": 11,
        "name": "Trump Guy",
        "description": "Peter's fake news career advances and he moves the family to Washington, D.C. to become Donald Trump's new White House Press Secretary. Things go south when Peter finds Donald sexually harassing Meg as she earlier claimed, following her encounter with Ivanka Trump."
    },
    "S21E04": {
        "season": 21,
        "episode": 4,
        "name": "The Munchurian Candidate",
        "description": "Lois hypnotizes Peter into satisfying her sexual proclivities. Meanwhile, Stewie renovates his treehouse in an attempt to win over Brian and Chris."
    }
}

def load_episodes_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

episodes = load_episodes_from_json('episodes.json')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/episodes/display', methods=['GET'])
def get_episodes():
    return jsonify(episodes)

@app.route('/episodes/add', methods=['POST'])
def add_episode():
    data = request.json
    key = f"S{data['season']}E{data['episode']}"
    episodes[key] = {
        "season": data['season'],
        "episode": data['episode'],
        "name": data['name'],
        "description": data['description']
    }
    save_episodes_to_json('episodes.json', episodes)
    return jsonify({"success": True, "message": "Episode added"})

@app.route('/episodes/random', methods=['GET'])
def random_suggestion():
    random_key = random.choice(list(episodes.keys()))
    random_episode = episodes[random_key]
    return jsonify(random_episode)

def save_episodes_to_json(file_path, episodes_data):
    with open(file_path, 'w') as file:
        json.dump(episodes_data, file, indent=4)

save_episodes_to_json('episodes.json', episodes)

if __name__ == '__main__':
    app.run(debug=True)