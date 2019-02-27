title batcycle
color a
for /l %%x in (1, 1, 36) do "D:\ProgramFiles\OpenSCAD\openscad" -o 0%%x.png -D t=%%x 09anim.scad --render
pause