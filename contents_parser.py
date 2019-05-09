import re


class Contents():

    def __init__(self, file):
        self.file = file + '-contents.txt'

    def open_file_create_reader_object_instance(self):
        with open(self.file, 'r', encoding='utf-8')as infile:
            reader = infile.read()
            return reader

    def get_contents_index(self, reader):

        content_pos = reader.find('##content##') + "##content##".__len__()
        print(content_pos)

        # if content_pos == 10:
        #     print('check transcript - content not found for %s' % self.file)
        #     return None

        return reader[content_pos:]

    def isolate_utterances(self,contents):

        regex = re.compile(r'^##.+?##', flags=re.DOTALL and re.MULTILINE)
        names = regex.findall(contents) #list of names with hashtag symbols

#iterate through list and replaces index with no hashtag name
        for index, name in enumerate(names):
            names[index] = re.sub('[##]*','', name)

        utterances = [split for split in re.split(regex, contents) if not split.isspace()]

        return names, utterances

    def assign_key_and_value(self, names, utterances):
        list_of_participants = []

        if len(names) != len(utterances):
            print('names and utterance entries are not syncing up for file: %s' % self.file)

        else:
            for i in range(len(names)):
                participant = {}
                participant[names[i]] = utterances[i].strip()
                list_of_participants.append(participant)

            return list_of_participants

    def content_creator(self):
        try:
            reader = self.open_file_create_reader_object_instance()
            contents = self.get_contents_index(reader)
            sep_names, sep_utterances = self.isolate_utterances(contents)
            list_of_participants = self.assign_key_and_value(sep_names, sep_utterances)
        except Exception as e:
            print('something wrong with ' + self.file, e)
            return None

        return list_of_participants












