%{
Lomb-Scargle PSD script

Sandy H.S. Herho <herho@umd.edu>
05/28/2021
%}
clear, clc, close all
ds = get(0,'ScreenSize');

data = readtable('../data/prInterp.csv');
pr = data.precipitation;
t = 1:length(pr);

Pfa = [50 10 1 0.01]/100;
Pd = 1-Pfa;

[pxx,f,pth] = plomb(pr, t,...
    'normalized','Pd',Pd);

figure('Position',[50 ds(4)-800 800 300],...
    'Color','w')
axes('Position',[0.1 0.15 0.8 0.7],...
    'XLim',[0 0.15],...
    'YLim',[0 max(pxx(:))]); hold on
line(f,pxx)
line(f,pth*ones(size(f')))
text(0.151*[1 1 1 1],pth-.5, ...
    [repmat('P_{fa} = ',[4 1]) num2str(Pfa')])
xlabel('Frequency (1/day)')
ylabel('Power')
hold off


