def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "username" : item["username"],
        "email" : item["email"],
        "password": item["password"],
        "skills": list(item["skills"]),
        "is_available" : item["is_available"],
        "posts": item["posts"],
        "following":item["following"],
        "rec_skills" : item["rec_skills"],
        "high" : item["high"],
        "mid" : item["mid"],
        "low" : item["low"],
        "last_active" : item["last_active"]
    }

def latest_userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "username" : item["username"],
        "email" : item["email"],
        "is_available": item["is_available"],
        "skills": list(item["skills"]),
        "experiance" : item["experiance"],
        "gender": item["gender"],
        "response_time":item["response_time"],
        "high" : item["high"],
        "mid" : item["mid"],
        "low" : item["low"],
        "last_active" : item["last_active"],
    }


def usersEntity(users)-> list:
    return [userEntity(user) for user in users]


def latest_usersEntity(users) -> list:
    return [latest_userEntity(user) for user in users]