# bashreduceTestingOS
Testing bashreduce in linux
NOTA: se encontraron datasets de prueba en el siguiente enlace: https://archive.org/download/stackexchange

Líeas de comando para la ejecución de parseString.py:

	1 Núcleo

	time ./br -m "localhost" -r /home/hirobreak/Documents/git/bashreduce/parseString.py -i /home/hirobreak/Downloads/dataset/Comments.xml -o salidaNew1.txt

	2 Núcleos

	time ./br -m "localhost localhost" -r /home/hirobreak/Documents/git/bashreduce/parseString.py -i /home/hirobreak/Downloads/dataset/Comments.xml -o salidaNew2.txt

	4 Núcleos

	time ./br -m "localhost localhost localhost localhost" -r /home/hirobreak/Documents/git/bashreduce/parseString.py -i /home/hirobreak/Downloads/dataset/Comments.xml -o salidaNew4.txt

Líneas de comando para la ejecución de upperANDlower.py:

	1 Núcleo

	time ./br -h "localhost" -m /home/crobby/bashreduce-rcrowley/upperANDlower.py -i /home/crobby/bashreduce-rcrowley/PostHistory.xml -o /home/crobby/bashreduce-rcrowley/salida1.txt

	2 Núcleos

	time ./br -h "localhost localhost" -m /home/crobby/bashreduce-rcrowley/upperANDlower.py -i /home/crobby/bashreduce-rcrowley/PostHistory.xml -o /home/crobby/bashreduce-rcrowley/salida2.txt

	4 Núcleos

	time ./br -h "localhost localhost" -m /home/crobby/bashreduce-rcrowley/upperANDlower.py -i /home/crobby/bashreduce-rcrowley/PostHistory.xml -o /home/crobby/bashreduce-rcrowley/salida3.txt

Líneas de comando para la ejecución de encrypt.py:

	1 Núcleo

	 time ./br -r /home/ray/bashreduce/encrypt.py -i /home/ray/bashreduce/datasets/PostHistory.xml -o salida1core.txt -m "localhost"
	
	2 Núcleos

	 time ./br -r /home/ray/bashreduce/encrypt.py -i /home/ray/bashreduce/datasets/PostHistory.xml -o salida1core.txt -m "localhost localhost"

	4 Núcleos

	 time ./br -r /home/ray/bashreduce/encrypt.py -i /home/ray/bashreduce/datasets/PostHistory.xml -o salida1core.txt -m "localhost localhost localhost localhost"
