import cv2

vidcap = cv2.VideoCapture('2018-06-28-16-30-35_2018-04-30-13-11-58_1.avi') ###### cambiar el archiu aqui
success, image = vidcap.read()
count = 0
height, width = image.shape[:2]
video = cv2.VideoWriter('db0.wmv',cv2.VideoWriter_fourcc(*'mp4v'),25,(width,height))
while success:
    #if count == 25 or count == 50 or count == 75 or count == 100:
    cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file

    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
avgminint = []
avgmaxint = []

avgminext = []
avgmaxext = []

avgminint2 = []
avgmaxint2 = []

avgminext2 = []
avgmaxext2 = []
for a in range(0, count-1):
    image = cv2.imread(r"frame%d.jpg" % a)

    y = 15
    x = 208
    h = 130
    w = 390
    crop_image = image[x:w, y:h]

    #cv2.imwrite("Cropped%d.jpg" % a, crop_image)
    #cv2.imshow("frame%d.jpg" % a,image)
    cv2.waitKey(0)


    def Average(lst):
        return sum(lst) / len(lst)


    # Driver Code

    from PIL import Image

    # creating a image object
    im = Image.open(r"frame%d.jpg" % a)

    px = im.load()


    maxDaltGruixut = 0
    maxDaltPrim = 0
    maxBaixPrim = 0
    maxBaixGruixut = 0
    minDaltGruixut = 0
    minDaltPrim = 0
    minBaixPrim = 0
    minBaixGruixut = 0
    paretprimaBaix = True
    i = 0
    j = 0
    for i in range(16, 528):
        for j in range(208, 388):
            # print(px[i, j])
            if j < 298 and j > 220:
                r, g, b = px[i, j]
                if r > 140:
                    im.putpixel((i, j), (0, 250, 0))
                    if j > maxDaltGruixut:
                        maxDaltGruixut = j

    prev = 0
    prevprev = 0
    for i in range(16, 528):
        for j in range(298, 388):
            r, g, b = px[i, j]
            if r > 30 and paretprimaBaix:

                im.putpixel((i, j), (250, 0, 0))
                im.putpixel((i, j + 1), (250, 0, 0))
                paretprimaBaix = False

        paretprimaBaix = True

    paretprimaBaix = True
    for i in range(16, 528):
        for j in range(298, 208, -1):
            r, g, b = px[i, j]
            if r > 30 and paretprimaBaix:
                im.putpixel((i, j), (250, 0, 0))
                im.putpixel((i, j + 1), (250, 0, 0))
                paretprimaBaix = False

        paretprimaBaix = True

    list = []
    paretprimaBaix = True
    for i in range(16, 528):
        for j in range(360, 298, -1):
            r, g, b = px[i, j]
            if b > 55 and paretprimaBaix:
                list.append(j)
                average = Average(list)
                average = int(average)
                b = 0

                """
                if average < j:
                    b = average - j
                    b = b / 2
                    b = int(b)
                    """
                im.putpixel((i, j), (0, 250, 0))
                im.putpixel((i, j + 1 - b), (0, 250, 0))
                paretprimaBaix = False
        paretprimaBaix = True

    if maxDaltGruixut == 0:
        maxDaltGruixut = 7
    im = im.save("frame-color%d.jpg" % a)
    imag = cv2.imread(r"frame-color%d.jpg" % a)
    video.write(imag)
    im2 = Image.open(r"frame-color%d.jpg" % a)
    px2 = im2.load()
    listminint =[]
    listmaxint= []

    listminext = []
    listmaxext = []

    listminint2 = []
    listmaxint2 = []

    listminext2 = []
    listmaxext2 = []
    for i in range(16,528, 32):
        minparetinterior = 0
        maxparetinterior = 0

        minparetexterior = 0
        maxparetexterior = 0

        minparetinterior2 = 0
        maxparetinterior2 = 0

        minparetexterior2 = 0
        maxparetexterior2 = 0

        for j in range(298, 208, -1):
            r, g, b =px[i,j]
            if r > 210 and i < 40 or minparetinterior == 0 or maxparetinterior == 0:
                minparetinterior = j
                maxparetinterior = j
            elif r > 210 and j > minparetinterior:
                minparetinterior = j
            elif r > 210 and j < maxparetinterior:
                maxparetexterior = j

            if g > 210 and i < 40 or minparetexterior == 0 or maxparetexterior == 0:
                minparetexterior = j
                maxparetexterior= j
            elif g > 210 and j > minparetexterior:
                minparetexterior = j
            elif g > 210 and j < maxparetexterior:
                maxparetexterior = j

        for j in range(298, 388):
            r, g, b = px[i, j]
            if r > 210 and i < 40 or minparetinterior2 == 0 or maxparetinterior2 == 0:
                minparetinterior2 = j
                maxparetinterior2 = j
            elif r > 210 and j < minparetinterior2:
                minparetinterior2 = j
            elif r > 210 and j > maxparetinterior2:
                maxparetexterior2 = j

            if g > 210 and i < 40 or minparetexterior2 == 0 or maxparetexterior2 == 0:
                minparetexterior2 = j
                maxparetexterior2 = j
            elif g > 210 and j < minparetexterior2:
                minparetexterior2 = j
            elif g > 210 and j > maxparetexterior2:
                maxparetexterior2 = j

        listminint.append(minparetinterior)
        listmaxint.append(maxparetinterior)

        listminext.append(minparetexterior)
        listmaxext.append(maxparetexterior)

        listminint2.append(minparetinterior2)
        listmaxint2.append(maxparetinterior2)

        listminext2.append(minparetexterior2)
        listmaxext2.append(maxparetexterior2)

    avgminint.append(Average(listminint))
    avgmaxint.append(Average(listmaxint))

    avgminext.append(Average(listminext))
    avgmaxext.append(Average(listmaxext))

    avgminint2.append(Average(listminint2))
    avgmaxint2.append(Average(listmaxint2))

    avgminext2.append(Average(listminext2))
    avgmaxext2.append(Average(listmaxext2))

puntminparetinteriordalt = Average(avgminint)
puntmaxparetinteriordalt = Average(avgmaxint)

puntminparetexteriordalt = Average(avgminext)
puntmaxparetexteriordalt = Average(avgmaxext)

puntminparetinteriorbaix = Average(avgminint2)
puntmaxparetinteriorbaix = Average(avgmaxint2)

puntminparetexteriorbaix = Average(avgminext2)
puntmaxparetexteriorbaix = Average(avgmaxext2)

IVSd = puntmaxparetinteriordalt - puntmaxparetexteriordalt
IVSs = puntminparetinteriordalt - puntminparetexteriordalt

LVIDd = puntmaxparetinteriorbaix - puntmaxparetinteriordalt
LVIDs = puntminparetinteriorbaix - puntminparetinteriordalt

LVPWd = puntmaxparetexteriorbaix - puntmaxparetinteriorbaix
LVPWs = puntminparetexteriorbaix - puntminparetinteriorbaix

IVSd = (IVSd * 9)/180
IVSs = (IVSs * 9)/180

LVIDd = (LVIDd * 9)/180
LVIDs = (LVIDs * 9)/180

LVPWd = (LVPWd * 9)/180
LVPWs = (LVPWs * 9)/180

LVESV = (7/(2.4+LVIDs))*(LVIDs**3)
print("LVESV: %d" % LVESV)
LVEDV = (7/(2.4+LVIDd))*(LVIDd**3)
print("LVEDV: %d" % LVEDV)
FS = (LVIDd-LVIDs)/LVIDd*100
print("FS: %d" % FS)
EF = (LVEDV-LVESV)/LVEDV*100
print("EF: %d" % EF)
LV = 0
SV = (LVEDV-LVESV)
print("SV: %d" % SV)
CO = SV*470
print("CO: %d" % CO)
RWT = (LVPWd + LVIDs)/(LVIDd)
print("RWT: %d" % RWT)


video.release()
print()