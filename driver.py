import os
import glob
import contents_parser
from xml_builder import XmlBuilder
from get_spreadseet import build_dict
import re


metadata = build_dict()
PATH = ""


def set_directory():
    """
    set working directory where txt files live
    """
    global PATH
    PATH = input("Enter the full file path to the txt files to be converted: ").strip()
    os.chdir(PATH)


def get_files():
    for filenames in glob.iglob('*.txt'):
        yield filenames


def find_metadata(single_file):
    if single_file.strip() in metadata['record_id']:
        # get index of record id
        rid_index = metadata['record_id'].index(single_file)
        m = {k : metadata[k][rid_index] for k in metadata.keys()}
        print(m)
        return m


def write_xml_file(single_file, xml_transcript):
    # check that xml folder exists
    if not os.path.exists(PATH+'/xml'):
        os.makedirs(PATH+'/xml')

    with open('{}/xml/{}.xml'.format(PATH, single_file), 'w') \
            as transcript_file:
        transcript_file.write(xml_transcript)


if __name__ == '__main__':
    set_directory()
    files_no_ext = [re.match(r'\d\d\d\d-\d\d\d', file).group(0) for file in get_files()]
    print(files_no_ext)
    for single_file in files_no_ext:
        # calling methods within
        m = find_metadata(single_file)
        content_instance = contents_parser.Contents(single_file)
        contents = content_instance.content_creator()
        if contents is not None and m is not None:
            xml_builder = XmlBuilder(m, contents)
            xml_transcript = xml_builder.build_xml_transcript()
            write_xml_file(single_file, xml_transcript)
        elif contents is None:                                          # muddling about...
            print('problem with {0} contents'.format(single_file))      # problem transcripts will be
        elif metadata is None:                                           # printed to console
            print('problem with {0} metadata'.format(single_file))







        



















