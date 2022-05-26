function Main
% 1
z=calc_sum(3,5);
disp(z)
% 2
z=calc_sum2(3);
disp(z)
% 3
[z1,z2]=calc_sum_prod(3,5);
disp([z1,z2])
% 4
[z1,z2]=calc_sum_prod_nested(3,5);
disp([z1,z2])
end

% 1
function z=calc_sum(x,y)
z=x+y;
end

% 2
function z=calc_sum2(x,y)
if nargin==1
    y=5;
end
z=x+y;
end
% 3
function [z1,z2]=calc_sum_prod(x,y)
z1=x+y;
z2=x*y;
end
% 4
function [z1,z2]=calc_sum_prod_nested(x,y)
z1=calc_sum(x,y);
z2=calc_prod(x,y);
    function z=calc_sum(x,y)
        z=x+y;
    end
    function z=calc_prod(x,y)
        z=x*y;
    end
end






