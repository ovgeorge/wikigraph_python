import os
from make_title_ID_dicts import make_title_id
from make_graph import make_graph
from compactify import compactify

path_to_data = "./data/"

if __name__ == "__main__":
	print "Download latest Wiki dump..."
	# For EnWiki
	# os.system("wget -c -P " + path_to_data + " https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-page.sql.gz")
	# os.system("gunzip -c " + path_to_data + "*page.sql.gz > " + path_to_data + "page.sql")
	#os.system("wget -c -P " + path_to_data + " https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pagelinks.sql.gz")
	#os.system("gunzip -c " + path_to_data + "*pagelinks.sql.gz > " + path_to_data + "pagelinks.sql")
	# For SimpleWiki
	os.system("wget -c -P " + path_to_data + " https://dumps.wikimedia.org/simplewiki/latest/simplewiki-latest-page.sql.gz")
	os.system("gunzip -c " + path_to_data + "*page.sql.gz > " + path_to_data + "page.sql")
	os.system("wget -c -P " + path_to_data + " https://dumps.wikimedia.org/simplewiki/latest/simplewiki-latest-pagelinks.sql.gz")
	os.system("gunzip -c " + path_to_data + "*pagelinks.sql.gz > " + path_to_data + "pagelinks.sql")
	print "Download latest Wiki dump... Done"
	print "Make title-id dictionaries..."
	make_title_id(path_to_data)
	print "Make title-id dictionaries... Done"
	print "Make graph..."
	make_graph(path_to_data)
	print "Make graph... Done"
	print "Compactify..."
	compactify(path_to_data)
	print "Compactify... Done"
