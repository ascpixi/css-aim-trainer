import os
import random
from inspect import cleandoc

if not os.path.isdir("generated"):
    os.mkdir("generated")

CIRCLE_COUNT = 200

stylesheet = "/* This stylesheet was generated using generate_css.py */\n"

for i in range(1, CIRCLE_COUNT + 1):
    stylesheet += f".circle:nth-child({i}) {{ top: {random.randint(10, 90)}%; left: {random.randint(10, 90)}% }}\n"

open("generated/circles.css", "w").write(stylesheet);

stylesheet = "/* This stylesheet was generated using generate_css.py */\n"

for i in range(1, CIRCLE_COUNT + 1):
    hue = random.randint(0, 360)

    stylesheet += cleandoc(f"""
    .circle:nth-child({i}) {{
        border-color: hsl({hue}, 100%, 50%);
        animation-delay: {i * 250}ms;
        box-shadow: 0 0 16px hsl({hue}, 100%, 50%);
    }}
    """) + "\n\n";

open("generated/circle-props.css", "w").write(stylesheet);