
echo "running original program for $1"
clang++ -O0 -std=c++11 $1
./a.out
rm ./a.out
echo ""

echo "running optimized program for $1"
python3 skeleton.py $1 > opt.cpp
clang++ -O0 -std=c++11 opt.cpp
./a.out
rm ./a.out
rm opt.cpp
