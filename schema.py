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

podcast_segment_schema = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "The title of the podcast segment"
        },
        "content": {
            "type": "string",
            "description": "The content of the podcast segment"
        },
        "duration": {
            "type": "string",
            "pattern": r"^\d{1,2}:\d{2}:\d{2}$",
            "description": "The duration of the segment in HH:MM:SS format"
        }
    },
    "required": ["title", "content", "duration"]
}