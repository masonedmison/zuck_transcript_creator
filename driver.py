import os
import glob
import contents_parser
from xml_builder import XmlBuilder
from get_spreadseet import build_dict
import re
from pdf_cover_creator import create_pdf_cover
from pdf_body_creator import create_pdf_body
from pdf_merger import pdf_merge


metadata = build_dict()
PATH = ""


def set_directory():
    """
    set working directory where txt files live
    """
    global PATH
    print('**Please make sure that the text files follow the double hashtag format as shown \n'
          'in the documentation**')
    print('#############################################################')
    while True:
        try:
            PATH = input("Enter the full file path to the txt files to be converted: ").strip()
            os.chdir(PATH)
            break
        except FileNotFoundError as fnf:
            print('File not found - invalid path at {}'.format(PATH))


def get_files():
    for filenames in glob.iglob('*.txt'):
        yield filenames


def find_metadata(single_file):
    if single_file.strip() in metadata['record_id']:
        # get index of record id
        rid_index = metadata['record_id'].index(single_file)
        # m = {k : metadata[k][rid_index] for k in metadata.keys()}
        m = {}
        for k in metadata.keys():
            if rid_index >= len(metadata[k]):
                m[k] = ""
            else:
                m[k] = metadata[k][rid_index]
        return m


def write_xml_file(single_file, xml_transcript):
    # check that xml folder exists
    if not os.path.exists(PATH+'/xml'):
        os.makedirs(PATH+'/xml')

    with open('{}/xml/{}.xml'.format(PATH, single_file), 'w') \
            as transcript_file:
        transcript_file.write(xml_transcript)


def delegate_pdf(m, single_file, r_id):
    if not os.path.exists(PATH+'/pdf'):
        os.makedirs(PATH+'/pdf')
    # append '-contents.txt' back to single file
    f = '{}-contents.txt'.format(single_file)
    create_pdf_cover(m)
    create_pdf_body(f, r_id)
    pdf_merge(single_file)
    os.remove('pdf/{}_cover.pdf'.format(r_id))


def main(pdfs=False):
    files_no_ext = [re.match(r'\d\d\d\d-\d\d\d', file).group(0) for file in get_files()]
    for single_file in files_no_ext:
        # calling methods within
        m = find_metadata(single_file)
        # take care of pdf stuff
        if pdfs:
            delegate_pdf(m, single_file, m['record_id'])
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


if __name__ == '__main__':
    print("this script creates xml transcripts for the Zuckerberg Transcript Collection. Pdf option is available, too.")
    pdfs_check = {'y': True, 'n': False}
    set_directory()
    while True:
        pdfs = input('Would you like pdf transcripts to be created? y or n')
        if pdfs == 'y' or pdfs == 'n':
            break
        print('incorrect value, please press y or n: ')
    main(pdfs_check[pdfs])








        



















