 
%prepare binary heap data:
binaryHeap = fullfile('performanceData','performancebinaryHeapEdges.txt');
binaryID = fopen(binaryHeap);
binaryScan = textscan(binaryID, '%d %f');

%prepare d-heap data:
dHeap = fullfile('performanceData','performancedHeapEdges.txt');
dID = fopen(dHeap);
dScan = textscan(dID, '%d %f');

%prepare binomial heap data:
binomialHeap = fullfile('performanceData', 'performancebinomialHeapEdges.txt');
binomialID = fopen(binomialHeap);
binomialScan = textscan(binomialID, '%d %f');

%close files:
fclose(binaryID);
fclose(binomialID);
fclose(dID);

%create new figure
figure
hold on;
legend();
plot(binaryScan{1},binaryScan{2},'DisplayName', 'Binary Heap')
plot(binomialScan{1},binomialScan{2},'DisplayName','Binomial Heap')
plot(dScan{1},dScan{2},'DisplayName','D-Heap')
title('Priority Queue Implementation Comparison:');
xlabel('Number of Edges.');
ylabel('Time in seconds.')
pbaspect([2 1 1]);
hold off;