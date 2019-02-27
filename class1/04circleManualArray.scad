data=[[0,0],[0,30],[18,30],
      [18,15],[30,15],[30,0]];
for(i=[0:len(data)-1]){
    echo(i,data[i]);
    translate(data[i]){
        circle(4);
    };
};

