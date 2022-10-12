def queryEntity(item) -> dict:
    return {
     "id": str(item["_id"]),
     "title" : str(item["title"]),
     "description" : str(item["description"]),
     "tags" : list(item["tags"]),
     "posted_by" : str(item["posted_by"]),
     "priority" : str(item["priority"]),
     "posted_on": str(item["posted_on"]),
     "status" : str(item["status"])
    }


def queriesEntity(items) -> list:
    return [queryEntity(item) for item in items]