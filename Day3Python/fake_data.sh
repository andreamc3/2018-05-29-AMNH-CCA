# This script will generate a two colum data file comprising of 1 through 10 in one column, and twice that in another column.

# Creating a header
echo 'xaxis yaxis' > data/linear_data.dat

# A 'for' loop in order to create the columns
for xdat in {1..10};
do
    echo $xdat  $((xdat*2)) >> data/linear_data.dat
done


