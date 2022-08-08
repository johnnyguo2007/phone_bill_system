def is_international(destination_number):
	"""
	Determine whether the call record is a internatinoal call
	or a local call
	:param destination_number:
	:return: boolean value
	"""
	is_inter = len(destination_number) > 10
	return is_inter
