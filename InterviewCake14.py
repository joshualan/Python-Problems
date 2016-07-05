def can_two_movies_fill_a_flight(flight_length, movie_lengths):
	times = [0] * (flight_length + 1)

	for time in movie_lengths:
		if time > flight_length:
			continue

		other_movie = flight_length - time

		if times[other_movie] > 0:
			return True

		times[time] += 1

	return False

assert can_two_movies_fill_a_flight(12, [5,6,7])
assert can_two_movies_fill_a_flight(12, [150,6,1,6,7])
assert not can_two_movies_fill_a_flight(12, [5,6,1,1,1])
