%% Einfache Lineare Regression
close all; clear; clc;

THE_FILE = 'messung1.csv';
data = table2array(readtable(THE_FILE));
x = data(:,1);
y = data(:,2);

%% LIN. REG.

b = polyfit(x,y,1);
slrg = @(v) b(2) + v.*b(1);

f = slrg(x);

%% SHOW
figure;
plot(x,y, 'o');
hold on;
plot(x,f, '--x');
grid on;

title('Einfache Lin. Reg.');
xlabel('X');
ylabel('Y');
legend('Messwerte','Fit function','Location', 'southeast');
text(0.5*min(x),0.9*max(y),sprintf('b0 = %d, b1 = %d', b(2),  b(1)))

%% 

m = 0.00160175160267068; %[mV/g]

du = (y-f) ;
figure;
plot(x,du, 'o--');
grid on;
