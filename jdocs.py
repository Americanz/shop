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



{
   "customcards":{
      "options":{
         "search_enabled":true,
         "save_position":true
      },
      "layout":{
         "Value":"",
         "Variable":"",
         "type":"LinearLayout",
         "weight":"0",
         "height":"wrap_content",
         "width":"match_parent",
         "orientation":"vertical",
         "Elements":[
            {
               "type":"LinearLayout",
               "height":"wrap_content",
               "width":"match_parent",
               "weight":"0",
               "Value":"",
               "Variable":"",
               "orientation":"horizontal",
               "Elements":[
                  {
                     "type":"CheckBox",
                     "Value":"@cb1",
                     "Variable":"cb1",
                     "TextSize":"32",
                     "NoRefresh":false,
                     "document_type":"",
                     "mask":"",
                     "BackgroundColor":"#6750A4",
                     "width":"match_parent",
                     "height":"wrap_content",
                     "weight":2
                  },
                  {
                     "type":"TextView",
                     "height":"wrap_content",
                     "width":"wrap_content",
                     "weight":"0",
                     "Value":"@type",
                     "Variable":"",
                     "TextSize":18                  }

               ]

            {
               "type":"LinearLayout",
               "height":"wrap_content",
               "width":"wrap_content",
               "weight":"0",
               "Value":"",
               "Variable":"",
               "orientation":"horizontal",
               "Elements":[
                  {
                     "type":"TextView",
                     "height":"wrap_content",
                     "width":"wrap_content",
                     "weight":"0",
                     "Value":"@number",
                     "Variable":"",
                     "TextBold":true,
                     "TextSize":20
                  }
               ]
            },
            {
               "type":"LinearLayout",
               "height":"wrap_content",
               "width":"wrap_content",
               "weight":"0",
               "Value":"",
               "Variable":"",
               "orientation":"vertical",
               "Elements":[
                  {
                     "type":"TextView",
                     "height":"wrap_content",
                     "width":"wrap_content",
                     "weight":"0",
                     "Value":"@countragent",
                     "Variable":"",
                     "TextSize":16
                  },
                  {
                     "type":"TextView",
                     "height":"wrap_content",
                     "width":"wrap_content",
                     "weight":"0",
                     "Value":"@warehouse",
                     "Variable":"",
                     "TextSize":16
                  }
               ]
            }
         },
         ]
      }
   }
}
