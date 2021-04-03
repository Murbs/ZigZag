# ZigZag 

A short python script to wow and amaze people who've never opened a terminal before. Using a short infinite loop, we can draw some neat patterns.

```Python

import time
import traceback
```

Time module is needed to dictate how fast or slow the loop iterates.
Traceback isn't necessary, but I like knowing exactly what went wrong if something breaks.

```Python

# Current space counter
spacing = 0 

# True = add to space counter, False = subtract from space counter
incrementSpacing = True 

# Forward pattern
forward = ' \\\\\\\\\\'

# Backward pattern
back = '/////' 
```

The 'spacing' variable dictates how many spaces precede the patterns. Our loop adjusts the spaces to make the patterns look like they are zigzag-ing.
'incrementSpacing' works in conjunction as a flag, that when we hit a certain number of spaces the conditions are reversed.

```Python

example = '\\'
print(example)

# Returns \
```

'forward' and 'back' store a string that we call based on 'incrementSpacing' being True/False. Since backslash is typically used to escape characters, we need to double up. The extra space at the start makes these strings line up while looping.

```Python

# Main loop
try:

    # While incrementSpacing is set to 'True'
    while True: 
        
        if incrementSpacing:
        
            # Multiply number of spaces by spacing variable
            print(' ' * spacing, end='')
            
            # Print forward pattern
            print(forward)
            
            # Pause for 1/10 of a second
            time.sleep(0.1) 
            
            # Increase the spacing counter by 1 every time the loop completes
            spacing = spacing + 1
            
            # If spacing counter is equal to 20..
            if spacing == 20:
            
                # Change direction
                incrementSpacing = False
                
        # While incrementSpacing is set to 'False'
        else:
            
            # Multiply number of spaces by spacing variable 
            print(' ' * spacing, end='')
            
            # Print backward pattern
            print(back)
            
            # Pause for 1/10 of a second
            time.sleep(0.1) # Pause for 1/10 of a second.
            
            # Decrease the spacing counter by 1 every time the loop completes
            spacing = spacing - 1
            
            # If spacing counter is equal to 0..
            if spacing == 0:
            
                # Change direction:
                incrementSpacing = True

# If something bad happens, print traceback to terminal so we can isolate the issue
except Exception:
    print(traceback.format.exec())
```

The 'Try' loop prints our 'forward' string every 0.1 second until it reaches 20 preceding spaces. The flag for 'incrementSpacing' then switches to 'False', where the exact same loop occurs in reverse printing the 'back' string instead until the 'spacing' variable returns to 0 and resets the loop. If an exception is raised for whatever reason, the traceback is printed.

![ZigZag Loop](https://cdn.discordapp.com/attachments/826109384093859879/827954192974217256/1.gif)
