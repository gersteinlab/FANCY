function [ypred rare1 rare2 alert]= fancy(X)
    load('FANCY.mat');
    [ypred,ysd,yci] = predict(gprMdl,X);
    rare1=ypred*0.19;
    rare2=ypred*0.23;
    if ypred<100
        alert='green';
    elseif ypred>100 && ypred<1000
        alert='yellow';
    else
        alert='red';
    end        
end
