
class DataFormat:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._tags_with_desc = {tag: desc for tag, desc in kwargs.items()}

    def add_tag(self, tag, description):
        self._tags_with_desc[tag] = description
        return self._tags_with_desc

    def delete_tag(self, tag):
        try:
            self._tags_with_desc.pop(tag)
            return self._tags_with_desc
        except KeyError:
            return self._tags_with_desc

    def get_description(self, tag):
        return self._tags_with_desc[tag]

    def get_tags_with_description(self):
        return self._tags_with_desc

    def get_tags(self):
        return list(self.get_tags_with_description().keys())

