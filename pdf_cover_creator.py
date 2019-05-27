from fpdf import FPDF


def create_pdf_cover(row):
    # Create instance of FPDF class
    pdf = FPDF(format='Letter', unit='in')

    # Set margin sizes
    pdf.l_margin = 1
    pdf.r_margin = 1
    pdf.t_margin = .25
    pdf.b_margin = .25

    # Create first page
    pdf.add_page()

    # Effective page width and height (for centering purposes)
    epw = pdf.w - 2*pdf.l_margin
    #eph = pdf.h = 2*pdf.t_margin

    # Font declaration
    pdf.set_font('Helvetica', '', 14)

    # Text height
    th = pdf.font_size

    # Initial line break needed for unknown reasons.
    pdf.ln(2*th)

    # Images
    # Use absolute positioning. Specify image dimension or it will revert to 72dpi.
    pdf.image('zuckbox.png', x=.39, y=.535, h=9.93, type='PNG')
    pdf.image('zucklogo.png', x=1, y=1, h=1.133, type='PNG')

    # Zuck Files URL
    pdf.set_xy(4.86, 1.43)     # Absolute positioning
    pdf.cell(0, th, 'www.zuckerbergfiles.org')  # Content cell (width, height, content)
    pdf.ln(1.2)                # Line break

    # Title
    pdf.set_font('Helvetica','B', 20)
    pdf.multi_cell(epw, th*1.5, row['title'], align='C')
    pdf.ln(.10)

    # ID
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(epw, th, row['record_id'], align='C')
    pdf.ln(.72)

    # Date
    pdf.set_xy(1.25, 3.6)
    pdf.set_font('Helvetica', 'B')
    pdf.cell(1.1, th, 'Date: ', align='R')
    pdf.set_font('Helvetica', style = '')
    pdf.multi_cell(4.93, th, row['date'], align='L')
    pdf.ln(.25)

    # Description
    pdf.set_x(1.25)                                         # Absolute positioning
    pdf.set_font('Helvetica', 'B')                          # Bold font for label
    pdf.cell(1.1, th, 'Description: ', align='R')           # Metadata field label
    pdf.set_font('Helvetica', style = '')                   # Unbold font for contents
    pdf.multi_cell(4.93, th, row['description'], align='L') # Metadata value contents
    pdf.ln(.25)

    # Participants
    pdf.set_x(1.25)
    pdf.set_font('Helvetica', 'B')
    pdf.cell(1.1, th, 'Participants: ', align='R')
    pdf.set_font('Helvetica', style = '')
    pdf.multi_cell(4.93, th, row['participants'], align='L')
    pdf.ln(.25)

    # Source
    pdf.set_x(1.25)  # Reset L-R position
    pdf.set_font('Helvetica', 'B')
    pdf.cell(1.1, th, 'Source: ', align='R')
    pdf.set_font('Helvetica', style = '')
    pdf.multi_cell(4.93, th, row['source'], align='L')
    pdf.ln(.25)

    # Type
    pdf.set_x(1.25)
    pdf.set_font('Helvetica', 'B')
    pdf.cell(1.1, th, 'Type: ', align='R')
    pdf.set_font('Helvetica', style = '')
    pdf.multi_cell(4.93, th, row['type'], align='L')
    pdf.ln(.25)

    # URL
    pdf.set_x(1.25)
    pdf.set_font('Helvetica', 'B')
    pdf.cell(1.1, th, 'URL: ', align='R')
    pdf.set_font('Helvetica', style = '')
    pdf.multi_cell(4.93, th, row['url'], align='L')

    # Write file
    pdf.output('pdf/' + row['record_id'] + '_cover' + '.pdf', 'F')


# def main():
#     filenames = create_filenames()
#     for row in create_metadata():
#         if row['record_id'] in filenames:
#             try:
#                 create_pdf(row)
#             except UnicodeEncodeError:
#                 print('UnicodeEncodeError: ' + row['record_id'])
#
#
# main()