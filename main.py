import cv2

# Insert "train", "test" or val depending on the dataset you want to convert
NAME_DIR = "val"
OLD_CSV = "gt_one.csv"

if __name__ == '__main__':
    f = open(OLD_CSV, "r")
    f1 = open(NAME_DIR + ".csv", "w")

    l = f.readlines()

    for x in l:

        words = x.split("/")[2].split()
        length = len(words)

        filepath = NAME_DIR + "/" + words[0]
        im = cv2.imread(filepath)

        h, w, c, = im.shape

        hh = str(h)
        ww = str(w)

        if (length - 2) == 4:

            path = words[0]
            mystery_val = int(words[1])

            if mystery_val == 1:
                mystery_valx = "varroa_clear" # "varroa" if single classification
            elif mystery_val == 3:
                mystery_valx = "varroa_cover" # "varroa" if single classification

            xmin = words[2]
            ymin = words[3]
            xmax = words[4]
            ymax = words[5]
            new_line = path + ", " + ww + ", " + hh + ", " + mystery_valx + ", " + xmin + ", " + ymin + ", " + xmax + ", " + ymax + "\n"
            f1.write(new_line)

        elif (length - 2) == 8:
            path = words[0]
            mystery_val = int(words[1])

            if mystery_val == 1:
                mystery_valx = "varroa_clear" # "varroa" if single classification
            elif mystery_val == 3:
                mystery_valx = "varroa_cover" # "varroa" if single classification

            xmin = words[2]
            ymin = words[3]
            xmax = words[4]
            ymax = words[5]
            new_line = path + ", " + ww + ", " + hh + ", " + mystery_valx + ", " + xmin + ", " + ymin + ", " + xmax + ", " + ymax + "\n"
            f1.write(new_line)

            path = words[0]
            mystery_val = int(words[1])

            if mystery_val == 1:
                mystery_valx = "varroa_clear" # "varroa" if single classification
            elif mystery_val == 3:
                mystery_valx = "varroa_cover" # "varroa" if single classification

            xmin = words[6]
            ymin = words[7]
            xmax = words[8]
            ymax = words[9]
            new_line = path + ", " + ww + ", " + hh + ", " + mystery_valx + ", " + xmin + ", " + ymin + ", " + xmax + ", " + ymax + "\n"
            f1.write(new_line)
