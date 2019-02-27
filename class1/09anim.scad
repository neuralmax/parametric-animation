data=[[0,0],[0,30],[18,30],
      [18,15],[30,15],[30,0]];
a=90;
echo(sin(a*10)*10+20,
    cos(a*10)*10+20);
rotate([0,0,180]){
test(sin(a*10)*10+20,
    cos(a*10)*10+20);
};
//scan();
module scan(){      
    for(i=[0:2]){
        for(j=[0:2]){
            translate([i*50,j*50]){
               echo(i*10+10,j*10+10);
               test(i*10+10,j*10+10);
            };
        };
    };
};
module test(a,b){
    difference(){
        assembly(a,b);
        translate([10,10,-30]){
            cube([100,100,100]);
        };
    };
};
module assembly(a,b){
    box(3,1,a);
    translate([0,0,2+a-b]){
        box(5,-1,b);
    };
};

module box(r,t,h){
    difference(){
        linear_extrude(h){
            shape(r);
        };
        translate([0,0,t]){
            linear_extrude(h){
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
