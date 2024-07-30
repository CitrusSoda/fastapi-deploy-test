from fastapi import FastAPI, HTTPException

app = FastAPI()

people = {
    "uk": "handsome",
    "hs": "artist",
    "jm": "godness"
}

@app.get("/")
def read_root():
    return "4 team server is running"

@app.get("/teams")
def get_teams():
    return list(people.keys())

@app.get("/teams/{team_name}")
def get_team(person: str):
    if person not in people:
        raise HTTPException(status_code=404, detail="Person not found")
    return people[person]