def
jdocs = {
    "customcards": {
        "options": {"search_enabled": True, "save_position": True},
        "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
                {
                    "type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "match_parent",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [
                        {
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "1",
                            "Elements": [
                                {
                                    "type": "TextView",
                                    "TextBold": True,
                                    "show_by_condition": "",
                                    "Value": "@name",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": "",
                                    "TextSize": 16,
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@code",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": "",
                                    "TextSize": 16,
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@GTIN",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": "",
                                    "TextSize": 16,
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@type_name",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": "",
                                    "TextSize": 20,
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@unit_name",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": "",
                                    "TextSize": 20,
                                },
                            ],
                        }
                    ],
                }
            ],
        },
    }
}
