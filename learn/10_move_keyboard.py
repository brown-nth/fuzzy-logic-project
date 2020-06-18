 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PI = 3.141592653


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
def draw_snowman(screen, x, y):
    # Draw a circle for the head
    pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
    # Draw the middle snowman circle
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    # Draw the bottom snowman circle
    pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK,[96+x,83+y,10,10],0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [100+x,100+y], [105+x,110+y], 2)
    pygame.draw.line(screen, BLACK, [100+x,100+y], [95+x,110+y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [100+x,100+y], [100+x,90+y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [100+x,90+y], [104+x,100+y], 2)
    pygame.draw.line(screen, RED, [100+x,90+y], [96+x,100+y], 2)

# -------- Main Program Loop -----------
while not done:
    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0
    
    # Current position
    x_coord = 10
    y_coord = 10
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
    
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    # --- Game logic should go here

    # pos = pygame.mouse.get_pos()
    # x = pos[0]
    # y = pos[1]

    x_coord += x_speed
    y_coord += y_speed
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 


    # --- Drawing code should go here
    # draw_snowman(screen, 300, 10)
    
    draw_stick_figure(screen, x_coord, y_coord)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()


# Pygame Code	ASCII	Common Name
# K_BACKSPACE	\b	backspace
# K_RETURN	\r	return
# K_TAB	\t	tab
# K_ESCAPE	^[	escape
# K_SPACE	 	space
# K_COMMA	,	comma sign
# K_MINUS	-	minus
# K_PERIOD	.	period slash
# K_SLASH	/	forward
# K_0	0	0
# K_1	1	1
# K_2	2	2
# K_3	3	3
# K_4	4	4
# K_5	5	5
# K_6	6	6
# K_7	7	7
# K_8	8	8
# K_9	9	9
# K_SEMICOLON	;	semicolon sign
# K_EQUALS	=	equals sign
# K_LEFTBRACKET	[	left
# K_RIGHTBRACKET	]	right
# K_BACKSLASH	\	backslash bracket
# K_BACKQUOTE	`	grave
# K_a	a	a
# K_b	b	b
# K_c	c	c
# K_d	d	d
# K_e	e	e
# K_f	f	f
# K_g	g	g
# K_h	h	h
# K_i	i	i
# K_j	j	j
# K_k	k	k
# K_l	l	l
# K_m	m	m
# K_n	n	n
# K_o	o	o
# K_p	p	p
# K_q	q	q
# K_r	r	r
# K_s	s	s
# K_t	t	t
# K_u	u	u
# K_v	v	v
# K_w	w	w
# K_x	x	x
# K_y	y	y
# K_z	z	z
# K_DELETE	delete	
# K_KP0	keypad	0
# K_KP1	keypad	1
# K_KP2	keypad	2
# K_KP3	keypad	3
# K_KP4	keypad	4
# K_KP5	keypad	5
# K_KP6	keypad	6
# K_KP7	keypad	7
# K_KP8	keypad	8
# K_KP9	keypad	9 period
# K_KP_PERIOD	.	keypad divide
# K_KP_DIVIDE	/	keypad multiply
# K_KP_MULTIPLY	*	keypad minus
# K_KP_MINUS	-	keypad plus
# K_KP_PLUS	+	keypad enter
# K_KP_ENTER	\r	keypad equals
# K_KP_EQUALS	=	keypad
# K_UP	up	arrow
# K_DOWN	down	arrow
# K_RIGHT	right	arrow
# K_LEFT	left	arrow
# K_INSERT	insert	
# K_HOME	home	
# K_END	end	
# K_PAGEUP	page	up
# K_PAGEDOWN	page	down
# K_F1	F1	
# K_F2	F2	
# K_F3	F3	
# K_F4	F4	
# K_F5	F5	
# K_F6	F6	
# K_F7	F7	
# K_F8	F8	
# K_F9	F9	
# K_F10	F10	
# K_F11	F11	
# K_F12	F12	
# K_NUMLOCK	numlock	
# K_CAPSLOCK	capslock	
# K_RSHIFT	right	shift
# K_LSHIFT	left	shift
# K_RCTRL	right	ctrl
# K_LCTRL	left	ctrl
# K_RALT	right	alt
# K_LALT	left	alt