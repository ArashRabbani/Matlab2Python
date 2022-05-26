% 1
for I=1:5
    disp(I)
end
% 2
I=1;
while I<=5
    disp(I)
    I=I+1;
end
% 3
for I=1:5
    disp(I)
    if I==3
        break
    end
end
% 4
for I=1:5
    if I==3
        continue
    end
        disp(I)
end
% 5
for I=1:5
    if I==3 && I<4
        continue
    end
    disp(I)
end
% 6
for I=1:5
    if I==3 || I==4
        continue
    end
    disp(I)
end
% 7
for I=1:5
    if I~=3 
        disp(I)
    end
end



