include <data.scad>
for(i=[0:len(data)-1]){
    translate(data[i]){
        circle(10);
    };
};