# bashreduceTestingOS
Testing bashreduce in linux

Lineas de comando para la ejecución de parseString.py:

	1 Nucleos

	time ./br -m "localhost" -r /home/hirobreak/Documents/git/bashreduce/parseString.py -i /home/hirobreak/Downloads/dataset/Comments.xml -o salidaNew1.txt

	2 Nucleos

	time ./br -m "localhost localhost" -r /home/hirobreak/Documents/git/bashreduce/parseString.py -i /home/hirobreak/Downloads/dataset/Comments.xml -o salidaNew2.txt

	4 Nucleos

	time ./br -m "localhost localhost localhost localhost" -r /home/hirobreak/Documents/git/bashreduce/parseString.py -i /home/hirobreak/Downloads/dataset/Comments.xml -o salidaNew4.txt
