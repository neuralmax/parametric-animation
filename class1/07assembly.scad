data=[[0,0],[0,30],[18,30],
      [18,15],[30,15],[30,0]];

difference(){
    assembly();
    translate([10,10,-10]){
        cube([100,100,100]);
    };
};

module assembly(){
    box(3,1);
    translate([0,0,2]){
        box(5,-1);
    };
};

module box(r,h){
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
};
module shape(r){
    minkowski(){
        polygon(data);
        circle(r);
    };
};
