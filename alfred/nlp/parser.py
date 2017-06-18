class Parser:
    def __init__(self, entities_list, text):
        self.duckling_list = []
        self.spacy_list = []

        self.parse_list(entities_list)

    def parse_list(self, entities_list):
        spacy_entities_list = []
        duckling_entities_list = []

        for entity in entities_list:
            if entity in self.duckling_list:
                duckling_entities_list.append(entity)
            elif entity in self.spacy_list:
                spacy_entities_list.append(entity)
