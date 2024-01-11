import sys
from PIL import Image, ImageOps

def main():

    input, output = check_args(sys.argv)

    try:

        shirt = Image.open("shirt.png")
        size = shirt.size
        
        input_image = Image.open(sys.argv[1])
        input_image  = ImageOps.fit(input_image, size)
        input_image.paste(shirt, shirt)
        input_image.save(sys.argv[2])



    except FileNotFoundError:
        sys.exit("Input does not exist")
    

def check_args(args):

    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:

            in_file = args[1].split(".")
            out_file = args[2].split(".")

            if len(in_file) > 1 and len(out_file) > 1 and check_image(in_file[1]) == True and check_image(out_file[1]) == True:
                if in_file[1] != out_file[1]:
                    sys.exit("Input and output have different extensions")
                else:
                    in_file = in_file[0] + "." + in_file[1]
                    out_file = out_file[0] + "." + out_file[1]
                    return in_file, out_file
            else:
                sys.exit("Invalid output")
        except (IndexError, ValueError):
            sys.exit("Invalid output")

def check_image(ext):

    if ext.lower() == "jpg" or ext.lower() == "png" or ext.lower() == "jpeg":
        return True
    else:
        False



if __name__ == "__main__":
    main()