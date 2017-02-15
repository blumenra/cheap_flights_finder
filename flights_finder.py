import webbrowser
import random
import time
import datetime


class flights_finder(object):

	def __init__(self):

		print "Welcome to flights finder!\n"
		self.initialize_flight_data()


	def initialize_flight_data(self):
		
		self.initialize_departure_details()
		self.initialize_arrival_details()

		confirm = self.confirm_information()

		if not confirm:
			self.initialize_flight_data()


		# self.departure_date = self.convert_datetime_to_date(self.convert_date_to_datetime(self.initiale_departure_date) - datetime.timedelta(days=self.initial_range))
		self.departure_date = self.get_timedelta(
												date = self.initiale_departure_date,
												n = self.initial_range,
												relation = False
												)

		self.last_departure_day = self.convert_datetime_to_date(self.convert_date_to_datetime(self.initiale_departure_date) + datetime.timedelta(days=self.initial_range))
		self.range = self.initial_range
		self.shouldTerminate = False
		
		arrival_date = self.convert_datetime_to_date(self.convert_date_to_datetime(self.initiale_arrival_date) - datetime.timedelta(days=self.initial_range))
		self.create_routine(arrival_date)
		self.unchecked_days_left = (self.initial_range*2+1)**2

		self.to_string()

	def create_routine(self, arrival_date):

		self.index = 0
		self.routine = []

		i = 0
		stop = self.range*2+1
		while i < stop:
			self.routine.append(arrival_date)
			arrival_date = self.update_loop_date(self.initiale_arrival_date, arrival_date)
			# print "self.arrival_date: " + str(arrival_date)
			i += 1

		self.range =  self.initial_range

	def get_timedelta(self, date, n, relation):

		if relation:
			return self.convert_datetime_to_date(self.convert_date_to_datetime(date) + datetime.timedelta(days=n))
		else:
			return self.convert_datetime_to_date(self.convert_date_to_datetime(date) - datetime.timedelta(days=n))

	def initialize_departure_details(self):
		# self.initiale_departure_date = input("Please enter the *deprture date* in this format: 22/7/1991 => 910722\n")
		
		try:
			day = input("Please enter the departure Day: ")
			month = input("Please enter the departure Month: ")
			year = input("Please enter the departure Year: ")
			self.initial_range = input("Please enter the departure range: ")
			print ""

			self.initiale_departure_date = int(str(year)[2:4] + self.adjust_month(month) + self.adjust_day(day))
			
			ok = self.flight_data_input_check(day=day, month=month, year=year, drange=self.initial_range)
			if not ok:
				self.initialize_departure_details()


		except NameError:
			print "Invalid input. please enter a number in accordance to the format\n"
			self.initialize_departure_details()
		except SyntaxError:
			print "Invalid input. please enter a number in accordance to the format\n"
			self.initialize_departure_details()


	def initialize_arrival_details(self):
		# self.initiale_departure_date = input("Please enter the *deprture date* in this format: 22/7/1991 => 910722\n")
		
		try:
			day = input("Please enter the return Day: ")
			month = input("Please enter the return Month: ")
			year = input("Please enter the return Year: ")
			print ""

			self.initiale_arrival_date = int(str(year)[2:4] + self.adjust_month(month) + self.adjust_day(day))
			
			ok = self.flight_data_input_check(day=day, month=month, year=year)
			if not ok:
				self.initialize_arrival_details()


		except NameError:
			print "Invalid input. please enter a number in accordance to the format\n"
			self.initialize_arrival_details()
		except SyntaxError:
			print "Invalid input. please enter a number in accordance to the format\n"
			self.initialize_arrival_details()


	def convert_date_to_datetime(self, date):

		return	datetime.datetime(int("20" + str(date)[0:2]), int(str(date)[2:4]), int(str(date)[4:6]))


	def convert_datetime_to_date(self, dtime):
		
		return int(str(dtime.year)[2:4] + self.adjust_month(dtime.month) + self.adjust_day(dtime.day))


	def adjust_month(self, month):

		str_month = str(month)

		if len(str_month) == 1:
			return "0" + str_month

		return str_month


	def adjust_day(self, day):

		str_day = str(day)

		if len(str_day) == 1:
			return "0" + str_day

		return str_day


	def confirm_information(self):

		flight_range = "range: " + str(self.initial_range)
		
		deprture_date = "departure date: " + \
							str(self.initiale_departure_date)[4:6] + "/" + \
							str(self.initiale_departure_date)[2:4] + "/" + \
							str(20) + str(self.initiale_departure_date)[0:2]

		arrival_date = "return date: " + \
							str(self.initiale_arrival_date)[4:6] + "/" + \
							str(self.initiale_arrival_date)[2:4] + "/" + \
							str(20) + str(self.initiale_arrival_date)[0:2]


		print "\nPlease confirm the following information:\n" + \
							deprture_date + "\n" + \
							arrival_date + "\n" + \
							flight_range + "\n"

		user_input = raw_input("Is the information correct?[y/n] ")

		return self.to_proceed(user_input)


	def flight_data_input_check(self, day, month, year, drange=0):
		
		ok = True

		if (day <= 0) or \
			(day > 31) or \
			(month <= 0) or \
			(month > 12) or \
			(year <= 2016) or \
			(drange < 0) or \
			():

			print "Invalid input. Please try again.\n"
			ok = False


		return ok


	def update_dates(self):

		ans = False

		if self.finish():
			ans =  True

		elif self.index_on_last_of_routine():
			self.initialize_next_routine()

		else:
			self.index += 1

		return ans
			

	def extract_day(self, date):

		return int(str(date)[4:6])


	def index_on_last_of_routine(self):

		return self.index == len(self.routine)-1


	def finish(self):

		finished =  self.departure_date == self.last_departure_day and \
				self.index_on_last_of_routine()

		if finished:
			print "All flights were opened"

		return finished


	def initialize_next_routine(self):

		self.index = 0

		self.departure_date = self.update_loop_date(self.initiale_departure_date, self.departure_date)


	def update_loop_date(self, base_date, loop_date):

		before_initiale_departure_date = base_date > loop_date
				
		if before_initiale_departure_date:
			self.range -= 1

			loop_date = self.convert_datetime_to_date(self.convert_date_to_datetime(
															base_date) - datetime.timedelta(days=self.range))
		else:
			self.range += 1

			loop_date = self.convert_datetime_to_date(self.convert_date_to_datetime(
															base_date) + datetime.timedelta(days=self.range))

		return loop_date


	def wait_random_time(self,fixedTimes = 0):
		times = 0

		if fixedTimes > 0:
			times = fixedTimes
		else:
			times = random.uniform(0,3)

		time.sleep(times)


	def to_proceed(self, user_input):

		if user_input == "y":
			return True
		if user_input == "n":
			return False
		else:
			user_input = raw_input("Invalid input. please try again.\n")
			return self.to_proceed(user_input)


	def open_next_tabs(self):

		try:
			proceed = True

			num = raw_input("Enter the number of next tabs to open: ")

			if num == "all":
				num = self.unchecked_days_left

			if int(num) <= 5:
				user_input = raw_input("Are you sure you want to open %s tabs[y/n]? " % str(num))
				print ""
				proceed = self.to_proceed(user_input)
				num = int(num)

			elif int(num) > 5:
				user_input = raw_input("That's a fine amount of tabs.. Are you sure you want to open [%s] tabs[y/n]???? " % str(num))
				print ""
				proceed = self.to_proceed(user_input)
				num = int(num)

			if proceed:
				
				while num > 0 and not self.shouldTerminate:
					link = "https://www.skyscanner.com/transport/flights/tlv/tyoa/%s/%s/airfares-from-ben-gurion-intl-to-tokyo-in-april-2017.html?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home&currency=USD&market=US&locale=en-US#results" \
									% (self.departure_date,	self.routine[self.index])
					webbrowser.open(link)

					self.shouldTerminate = self.update_dates()

					num -= 1
					self.unchecked_days_left -= 1

					self.wait_random_time(7)


		except NameError:
			print "Invalid input. please enter a number\n"
			self.open_next_tabs()
		except SyntaxError:
			print "Invalid input. please enter a number\n"
			self.open_next_tabs()
		except ValueError:
			print "Invalid input. please enter a number\n"
			self.open_next_tabs()

	def run(self):

		self.open_next_tabs()

		while not self.shouldTerminate:
				
				print "\nThere are %s unchecked flights." % (self.unchecked_days_left)
				user_input = raw_input("Would you like to continue[y/n]? ")
				proceed = self.to_proceed(user_input)

				if not proceed:
					break

				else:
					
					self.open_next_tabs()


	def to_string(self):

		print "initiale departure date: " + str(self.convert_date_to_datetime(self.initiale_departure_date))
		print "initiale arrival date: " + str(self.convert_date_to_datetime(self.initiale_arrival_date))
		print "current departure date: " + str(self.convert_date_to_datetime(self.departure_date))
		print "routine: " + str(self.routine)
		print "index: " + str(self.index)
		print "last departure day: " + str(self.convert_date_to_datetime(self.last_departure_day))
		print "should terminate: " + str(self.shouldTerminate)
		print "initial range: " + str(self.initial_range)
		print "current range: " + str(self.range)
		print "unchecked days left: " + str(self.unchecked_days_left)