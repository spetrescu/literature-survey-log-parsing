sed '/^Processed/d' raw_results.txt > 1.txt
sed '/^mv/d' 1.txt > 2.txt
sed '/^100/d' 2.txt > 3.txt
sed '/^Epoch/d' 3.txt > 4.txt
sed '/^\ \ \ \ (/d' 4.txt > 5.txt
sed '/^\ \ F/d' 5.txt > 6.txt
sed '/^AttributeError/d' 6.txt > 7.txt
sed '/^\ \ \ \ a/d' 7.txt > 8.txt
sed '/^\ \ \ \ r/d' 8.txt > 9.txt
sed '/^2022/d' 9.txt > 10.txt
sed '/^\ \ nn/d' 10.txt > 11.txt
sed '/^\/home/d' 11.txt > 12.txt
sed '/^Traceback/d' 12.txt > raw_results.txt



rm 1.txt
rm 2.txt
rm 3.txt
rm 4.txt
rm 5.txt
rm 6.txt
rm 7.txt
rm 8.txt
rm 9.txt
rm 10.txt
rm 11.txt
rm 12.txt