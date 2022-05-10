import svgwrite

dwg = svgwrite.Drawing('test.svg', profile='tiny')
dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()

class Designer():

    def __init__(self) -> None:
        self.CompositionalStrategy = None

        

def main():
    pass

if __name__ == '__main__':
    main()