import PySimpleGUI as SG

fonts = (
    ('Axial', str(100), 'bold'),
)

fonts2 = (
    ('Axial', str(19), 'bold'),
)

def make_window1():
    layout_column = [
              [SG.Text('Vul je studentnummer in:', font=font) for font in fonts2],
              [SG.Input(size=(20,0), font=font) for font in fonts2],
              [SG.Button('Volgende', size=(10, 0), font=font) for font in fonts2],
              [SG.Button('Stop')]
              ]
    layout = [[SG.Column(layout_column, vertical_alignment='center', justification='center')]]
    return SG.Window('Stembus', layout, finalize=True)


def make_window2(candidates):
    layout_column = []

    for candidate in candidates:
        candidate = str(candidate)
        line = [SG.Text(candidate, font=font) for font in fonts2]
        layout_column.append(line)

    layout_column.append([SG.Input(size=(20,0), font=font) for font in fonts2])
    layout_column.append([SG.Button('Stem', size=(10, 0), font=font) for font in fonts2])

    #layout_column2 = [
    #          [SG.Text('', font=font) for font in fonts2],
    #          [SG.Input(size=(20,0), font=font) for font in fonts2],
    #          [SG.Button('Stem', size=(10, 0), font=font) for font in fonts2]
    #          ]
    layout = [[SG.Column(layout_column, vertical_alignment='center', justification='center')]]
    return SG.Window('Stembus', layout, finalize=True)




def make_window3():
    layout_column = [
              [SG.Text('U mag niet stemmen', justification='center', font=font) for font in fonts],
              [SG.Button('Terug', size=(16, 0), font=font) for font in fonts]
              ]
    layout = [[SG.Column(layout_column, vertical_alignment='center', justification='center')]]

    return SG.Window('Stembus', layout, finalize=True)


def make_window4():
    layout_column = [
              [SG.Text('Dit is geen kandidaat', justification='center', font=font) for font in fonts],
              [SG.Button('Terug', size=(16, 0), font=font) for font in fonts]
              ]
    layout = [[SG.Column(layout_column, vertical_alignment='center', justification='center')]]

    return SG.Window('Stembus', layout, finalize=True)

def make_window5(error):
    layout_column = [
        [SG.Text(error, justification='center', font=font) for font in fonts],
        [SG.Button('Terug', size=(16, 0), font=font) for font in fonts]
    ]
    layout = [[SG.Column(layout_column, vertical_alignment='center', justification='center')]]

    return SG.Window('Stembus', layout, finalize=True)
