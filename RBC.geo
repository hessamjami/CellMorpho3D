//****************
//** Parameters **
//****************
R=10e-6; // Radius of border of the RBC
Lcent=100e-6; // Length of the central part of the RBC
depr=R/4; //magnitude of the depression of central part of the RBC
th=R/5; //Thickness of the cell
lcm=R/8; //Characteristic length of the mesh
//**************
//** Geometry **
//**************
//First iteration for outer lines, second for inner lines
For inout In {0:1}
np=newp;
//Left circle
Point(np)={0,-R+inout*th,0,lcm};
Point(np+1)={0,0,0,lcm};
Point(np+2)={0,R-inout*th,0,lcm};
Point(np+3)={-(R-inout*th),0,0,lcm};
nl=newl;
Circle(nl)={3+(np-1),2+(np-1),4+(np-1)};
Circle(nl+1)={4+(np-1),2+(np-1),1+(np-1)};
//Top central line (with Spline)
Point(np+4)={Lcent/4,R-inout*th*0.7-depr,0,lcm};
Point(np+5)={Lcent/2,R-inout*th-depr,0,lcm};
Spline(nl+2)={3+(np-1),5+(np-1),6+(np-1)};
//Bottom central line
Point(np+6)={Lcent/4,-(R-inout*th*0.7-depr),0,lcm};
Point(np+7)={Lcent/2,-(R-inout*th-depr),0,lcm};
Spline(nl+3)={1+(np-1),7+(np-1),8+(np-1)};
EndFor
Line(nl+5)={6,np+5};
Line(nl+6)={np+7,8};
Line Loop(1)={-2,-1,3,nl+5,-(nl+2),nl,nl+1,nl+3,nl+6,-4};
Plane Surface(1)={1};
//**********
//** Mesh **
//**********
//Number of divisions on the circular lines
Transfinite Line {1,2}=Pi*R/(2*lcm);
Transfinite Line {nl,nl+1}=Pi*R/(2*lcm);
Recombine Surface {1};
//Extrussions by 90º each
ss[]=Extrude {{0,1,0},{Lcent/2,0,0},Pi/2} {Surface {1}; Layers{10}; Recombine;};
Printf("Generated first top area = %g", ss[0]);
ss1[]=Extrude {{0,1,0},{Lcent/2,0,0},Pi/2} {Surface {ss[0]}; Layers{10}; Recombine;};
Printf("Generated second top area = %g", ss1[0]);
ss2[]=Extrude {{0,1,0},{Lcent/2,0,0},Pi/2} {Surface {ss1[0]}; Layers{10}; Recombine;};
Printf("Generated third top area = %g", ss2[0]);
ss3[]=Extrude {{0,1,0},{Lcent/2,0,0},Pi/2} {Surface {ss2[0]}; Layers{10}; Recombine;};
Printf("Generated fourth top area = %g", ss3[0]);
reyhaneh's mess
