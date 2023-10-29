@echo off
echo "running original program for %1"
clang++ -O0 %1
.\a.exe
rm .\a.exe
echo ""

echo "running optimized program for %1"
python3 skeleton.py %1 > opt.cpp
clang++ -O0 opt.cpp
.\a.exe
rm .\a.exe

