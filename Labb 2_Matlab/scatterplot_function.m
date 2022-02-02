[file,path] = uigetfile('*.csv');
d =readtable(file);

 
  T1 = table2array(d(:,1));
  T2 = table2array(d(:,2));
  T3 = table2array(d(:,3));
  
  A = null(300,2);
  B = null(300,2);
  C = null(300,2);
  D = null(300,2);
  
  counter1 = 1;
  counter2 = 1;
  counter3 = 1;
  counter4 = 1;
  
for i=1:size(T3(:,1))
    
    str = convertCharsToStrings(T3{i}); 
    
    if(ismember(str, {'foo', 'a'}))
         A(counter1, 1) = (T1(i));
         A(counter1, 2) = (T2(i));
         counter1 = counter1 + 1;
    elseif(ismember(str, {'b', 'bar'}))
         B(counter2, 1) = (T1(i));
         B(counter2, 2) = (T2(i));
         counter2 = counter2 + 1;
    elseif(ismember(str, {'c', 'baz'}))
         C(counter3, 1) = (T1(i));
         C(counter3, 2) = (T2(i));
         counter3 = counter3 + 1;
    else
         D(counter4, 1) = (T1(i));
         D(counter4, 2) = (T2(i));
         counter4 = counter4 + 1;
    end
    
    
end

xhigh = ceil(max(table2array(d(:,1))) *1.1); % highest x value with marigin
xlow = floor(min(table2array(d(:,1))) *1.1); % lowest x value with marigin

yhigh = ceil(max(table2array(d(:,2))) *1.1); % highest y value with marigin
ylow = floor(min(table2array(d(:,2))) *1.1); % lowest y value with marigin

axis([xlow xhigh ylow yhigh]) % set canvas dimensions



hold on
if isempty(A)
else
scatter(A(:,1),A(:,2),'filled', 'red');
end

hold on
if isempty(B)
else
scatter(B(:,1),B(:,2),'filled', 'green');
end

hold on
if isempty(C)
else
scatter(C(:,1),C(:,2),'filled', 'blue');
end

hold on
if isempty(D)
else
scatter(D(:,1),D(:,2),'filled', 'yellow');
end

xlabel('X values');
ylabel('Y values');

legend('a/foo','b/baz','c/bar')

title('TNM048 Lab 2','FontSize',14);
