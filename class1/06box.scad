data=[[0,0],[0,30],[18,30],
      [18,15],[30,15],[30,0]];

r=5;
h=5;
difference(){
    linear_extrude(20){
        shape(r);
    };
    translate([0,0,h]){
        linear_extrude(20){
            shape(r-1);
        };
    };
};

module shape(r){
    minkowski(){
        polygon(data);
        circle(r);
    };
};
