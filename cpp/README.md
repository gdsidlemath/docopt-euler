cd /usr/include

git clone https://github.com/docopt/docopt.cpp
cd docopt.cpp
cmake .
make install

cp /usr/include/docopt.cpp/*.h /usr/include
cp /usr/include/docopt.cpp/docopt.cpp include/
