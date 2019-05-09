import xml.etree.ElementTree as ET
from xml.dom import minidom


class XmlBuilder(object):

    def __init__(self, metadata, contents):
        self.metadata = metadata
        self.contents = contents

    def build_xml_transcript(self):
        root = ET.Element('transcript')
        meta_tag = ET.SubElement(root, 'metadata')
        for key, value in self.metadata.items():
            key = ET.SubElement(meta_tag, key)
            key.text = value

        content_tag = ET.SubElement(root, 'contents')
        for participant in self.contents:
            for key, value in participant.items():
                speaker = ET.SubElement(content_tag, 'participant', attrib={'name': key})
                speaker.text = value
        xml_formatted = self.prettyprint(root)
        return xml_formatted

    def prettyprint(self, root):
        #helper method to print formatted xml document
        un_formatted = ET.tostring(root, 'utf-8')
        re_parse = minidom.parseString(un_formatted)
        return re_parse.toprettyxml(indent="    ")

