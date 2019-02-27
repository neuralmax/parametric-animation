include <data.scad>
for(i=[0:len(data)-1]){
    translate([data[i][0],data[i][1]]){
        circle(data[i][2]/400,$fn=10);
    };
};