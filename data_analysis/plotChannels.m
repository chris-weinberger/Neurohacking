[n,p] = size(rawdatanew); %rawdatanew is a loaded text file created using python program firstRead

t = 1:n; %creates the time vector


column1 = rawdatanew{:,1};
column2 = rawdatanew{:,2};
column3 = rawdatanew{:,3};
column4 = rawdatanew{:,4};
column5 = rawdatanew{:,5};
column6 = rawdatanew{:,6};
column7 = rawdatanew{:,7};
column8 = rawdatanew{:,8};

columns = {column1, column2, column3, column4, column5, column6, column7, column8};

plot(t,column1);
hold on;
plot(t,column2);
plot(t,column3);
plot(t,column4);
plot(t,column5);
plot(t,column6);
plot(t,column7);
plot(t,column8);

%for col = 1:length(columns)
%    plot(t,columns(col))
%end
    

