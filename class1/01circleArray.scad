for(j=[0:3]){
    for(i=[0:3]){
        translate([i*10,j*10]){
            rotate(j*10){
                circle(5,$fn=i+3);
            };
        };
    };
};