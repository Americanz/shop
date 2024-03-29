import json
from pysimplebase import SimpleBase
from ru.travelfood.simple_ui import SimpleUtilites as suClass

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
                                # {
                                #     "type": "TextView",
                                #     "show_by_condition": "",
                                #     "Value": "@type_name",
                                #     "NoRefresh": False,
                                #     "document_type": "",
                                #     "mask": "",
                                #     "Variable": "",
                                #     "TextSize": 20,
                                # },
                                # {
                                #     "type": "TextView",
                                #     "show_by_condition": "",
                                #     "Value": "@unit_name",
                                #     "NoRefresh": False,
                                #     "document_type": "",
                                #     "mask": "",
                                #     "Variable": "",
                                #     "TextSize": 20,
                                # },
                            ],
                        }
                    ],
                }
            ],
        },
    }
}

db = SimpleBase("test_1c", path=suClass.get_simplebase_dir(), timeout=200)


def inventory_list_open(hashMap, _files=None, _data=None):

    jdocs["customcards"]["cardsdata"] = []
    documents = db["inventory"].all()

    for doc in documents:
        card = {
            "key": doc.get("_id"),
            "name": doc.get("name"),
            "code": doc.get("warehouse"),
            "GTIN": doc.get("shopName"),
        }

        jdocs["customcards"]["cardsdata"].append(card)

    hashMap.put("cards", json.dumps(jdocs, ensure_ascii=False))

    return hashMap


document = None


def inventory_list_click(hashMap, _files=None, _data=None):
    global document

    document = db["inventory"].get(hashMap.get("selected_card_key"))

    hashMap.put("ShowScreen", "Инвентаризация")

    return hashMap


def inventory_open(hashMap, _files=None, _data=None):

    j = {
        "customtable": {
            "options": {"search_enabled": True, "save_position": True},
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
                    {
                        "type": "LinearLayout",
                        "orientation": "horizontal",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "Padding": "0",
                        "StrokeWidth": "1",
                        "weight": "1",
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
                                        "show_by_condition": "",
                                        "Value": "@index",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "margin": "0,15,0,0",
                                        "TextSize": "16",
                                        "weight": "1",
                                        "TextBold": True,
                                        "gravity_horizontal": "left",
                                    }
                                ],
                            },
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "3",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@sku",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "TextSize": "16",
                                        "weight": "1",
                                        "TextBold": True,
                                        "gravity_horizontal": "left",
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@barcode",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "TextSize": "12",
                                        "weight": "1",
                                        "TextBold": False,
                                        "gravity_horizontal": "left",
                                    },
                                ],
                            },
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "1",
                                "StrokeWidth": "1",
                                "BackgroundColor": "#F0F8FF",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "План",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "1",
                                        "gravity_horizontal": "center",
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@qty",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "1",
                                        "TextBold": True,
                                        "gravity_horizontal": "center",
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "Факт",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "1",
                                        "gravity_horizontal": "center",
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@qty_fact",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "1",
                                        "TextBold": True,
                                        "gravity_horizontal": "center",
                                    },
                                ],
                            },
                        ],
                    }
                ],
            },
        }
    }

    j["customtable"]["tabledata"] = []

    for line in document["goods"]:
        l = {
            "index": document["goods"].index(line) + 1,
            "sku": line.get("nom"),
            "barcode": line.get("barcode"),
            "qty": line.get("qty_plan"),
            "qty_fact": line.get("qty"),
        }
        j["customtable"]["tabledata"].append(l)

    hashMap.put("table", json.dumps(j, ensure_ascii=False))

    return hashMap


pos = -1


def inventory_input(hashMap, _files=None, _data=None):
    global document
    global pos, name, qty_plan

    # hashMap.put("toast",hashMap.get("listener"))

    if hashMap.get("listener") == "barcode":

        for line in document["goods"]:
            if line["barcode"] == hashMap.get("barcode"):
                pos = document["goods"].index(line) + 1
                name = line.get("nom")
                qty_plan = line.get("qty_plan")
                break

        if pos == -1:
            hashMap.put("toast", "Штрихкод не найден")
            return hashMap

        layout = {
            "Value": "",
            "Variable": "",
            "type": "LinearLayout",
            "weight": "0",
            "height": "match_parent",
            "width": "match_parent",
            "orientation": "vertical",
            "Elements": [
                {
                    "type": "TextView",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "По плану: " + str(qty_plan),
                    "Variable": "",
                },
                {
                    "type": "EditTextText",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Value": "",
                    "Variable": "qty",
                },
            ],
            "BackgroundColor": "",
            "StrokeWidth": "",
            "Padding": "",
        }

        hashMap.put("ShowDialogLayout", json.dumps(layout, ensure_ascii=False))
        hashMap.put("ShowDialog", "")
        hashMap.put(
            "ShowDialogStyle",
            json.dumps(
                {"title": "" + name, "yes": "Сохранить", "no": "Отмена"},
                ensure_ascii=False,
            ),
        )

    elif hashMap.get("event") == "onResultPositive":
        hashMap.put("toast", "Рядок: " + str(pos))
        if pos > -1:
            document["goods"][pos - 1]["qty"] = hashMap.get("qty")
            db["inventory"].insert(document, upsert=True)

    return hashMap
