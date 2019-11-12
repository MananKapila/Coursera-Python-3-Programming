import image

win = image.ImageWin(480, 640, "Image Processing")
original_image = image.Image('cy.png')
original_image.set_delay(1, 10)

width = original_image.get_width()
height = original_image.get_height()
print(width, height)

original_image.draw(win)
my_image = original_image.copy()

for row in range(height):
    for col in range(width):
        v = my_image.get_pixel(col, row)
        v.red = 255 - v.red
        v.green = 255 - v.green
        v.blue = 255 - v.blue
        my_image.set_pixel(col, row, v)

my_image.draw(win)
print(win.get_mouse())
my_image.save('lcastle-inverted.gif')
print(my_image.to_list())
win.exit_on_click()
