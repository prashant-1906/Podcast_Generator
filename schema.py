from jsonschema import Draft7Validator

podcast_outline_schema = {
    "type": "object",
    "properties": {
        "episodes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the podcast episode"
                    },
                    "discussion_points": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "An array of discussion points/topics for the episode"
                    }
                },
                "required": ["title", "discussion_points"]
            }
        }
    },
    "required": ["episodes"]
}

outline_validator = Draft7Validator(podcast_outline_schema)