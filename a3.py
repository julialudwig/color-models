"""
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

Julia Ludwig (jal545) and Jackson Stone (jls596)
10/16/2020
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    return introcs.RGB(255-rgb.red,255-rgb.green,255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.

    The decimal point counts as one of the five characters.

    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.

    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending
    # on how big value is. Look at the examples in the specification.

    value_str=str(round(float(value),5))
    length=len(value_str)
    decimal=value_str.find('.')

    if length == 5:
        return value_str
    elif length < 5:
        value_str=str(round(float(value_str),5-length))
    else:
        value_str=str(round(float(value_str),4-decimal))

    if len(value_str)==3:
        value_str=value_str+'00'
    elif len(value_str)==4:
        value_str=value_str+'0'

    return value_str



def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".

    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)

    Example: if str(cmyk) is

          '(0.0,31.3725490196,31.3725490196,0.0)'

    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.

    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    #CMYK attributes are float values from 0.0-100.0
    c=str5(cmyk.cyan)
    m=str5(cmyk.magenta)
    y=str5(cmyk.yellow)
    k=str5(cmyk.black)
    str_cmyk = '('+c+', '+m+', '+y+', '+k+')'
    return str_cmyk


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".

    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)

    Example: if str(hsv) is

          '(0.0,0.313725490196,1.0)'

    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.

    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    #H takes values [0,360), S and V:[0.0,1.0]

    h=str5(hsv.hue)
    s=str5(hsv.saturation)
    v=str5(hsv.value)
    str_hsv = '('+h+', '+s+', '+v+')'
    return str_hsv


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    r=rgb.red/255
    g=rgb.green/255
    b=rgb.blue/255
    k=1-max(r,g,b)

    if k == 1:
        c=0
        m=0
        y=0
    else:
        c=(1-r-k)/(1-k)*100
        m=(1-g-k)/(1-k)*100
        y=(1-b-k)/(1-k)*100

    k=k*100
    cmyk=introcs.CMYK(c,m,y,k)
    return cmyk

def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    c=cmyk.cyan/100
    m=cmyk.magenta/100
    y=cmyk.yellow/100
    k=cmyk.black/100

    r=round((1-c)*(1-k)*255)
    g=round((1-m)*(1-k)*255)
    b=round((1-y)*(1-k)*255)

    rgb=introcs.RGB(r,g,b)
    return rgb


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    r=rgb.red/255
    g=rgb.green/255
    b=rgb.blue/255
    maxi=max(r,g,b)
    mini=min(r,g,b)

    v=maxi

    if maxi == 0:
        s=0
    else:
        s=1-(mini/maxi)

    if maxi==mini:
        h=0
    elif maxi==r and g>=b:
        h=60.0*(g-b)/(maxi-mini)
    elif maxi==r and g<b:
        h=60.0*(g-b)/(maxi-mini)+360.0
    elif maxi==g:
        h=60.0*(b-r)/(maxi-mini)+120.0
    elif maxi==b:
        h=60.0*(r-g)/(maxi-mini)+240.0

    hsv=introcs.HSV(h,s,v)
    return hsv

def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    #Assign hsv attributes to variable to simplify
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value

    #Calculate values
    h_i = math.floor(h/60)
    f = h/60 - h_i
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)

    #Assign values to r,g,b in range 0.0..1.0 based on h_i
    if h_i == 0:
        r=v
        g=t
        b=p
    elif h_i == 1:
        r=q
        g=v
        b=p
    elif h_i == 2:
        r=p
        g=v
        b=t
    elif h_i == 3:
        r=p
        g=q
        b=v
    elif h_i == 4:
        r=t
        g=p
        b=v
    elif h_i == 5:
        r=v
        g=p
        b=q

    #Convert r,g,b values to ints in range of 0..255
    r=round(r*255)
    g=round(g*255)
    b=round(b*255)

    return introcs.RGB(r,g,b)


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast

    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart,
    with all values becoming 0 or 1 when contrast = 1.

    Parameter value: the value to adjust
    Precondition: value is a float in 0..1

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    if contrast==1:
        if value >= 0.5:
            y=1
        else:
            y=0
    elif value < 0.25 + 0.25*contrast:
        y = ((1-contrast)/(1+contrast))*value
    elif value > 0.75 - 0.25*contrast:
        y = ((1-contrast)/(1+contrast))*(value-(3-contrast)/4)+(3+contrast)/4
    else:
        y = ((1+contrast)/(1-contrast))*(value-(1+contrast)/4)+(1-contrast)/4
    return y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb

    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.

    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    r=rgb.red/255
    g=rgb.green/255
    b=rgb.blue/255

    r=contrast_value(r,contrast)
    g=contrast_value(g,contrast)
    b=contrast_value(b,contrast)

    r=round(r*255)
    g=round(g*255)
    b=round(b*255)

    rgb.red=r
    rgb.green=g
    rgb.blue=b
