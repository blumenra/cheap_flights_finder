
import flights_finder


def main():

	# datetimed =  datetime.datetime(2017, 04, 10) - datetime.timedelta(days=10)
	# print datetimed
	finder = flights_finder.flights_finder()
	# print "finished intializing finder:)\n"
	# finder.to_string()
	finder.run()


	# response = urllib2.urlopen("https://youtube.com/results?search_query=bla")
	# html = response.read()
	# print "html: " + html
	# print "a"



if __name__ == '__main__':
	main()