("""Grade letter -> grade point converter.

Reads a letter grade from keyboard (e.g. A, A-, B+, C) and prints the
corresponding numeric grade point per the provided mapping. If the user
enters an invalid letter, the program asks them to re-enter until a valid
value is provided.

Mapping used:
A+ -> 4.0
A  -> 4.0
A- -> 3.7
B+ -> 3.3
B  -> 3.0
B- -> 2.7
C+ -> 2.3
C  -> 2.0
C- -> 1.7
D+ -> 1.3
D  -> 1.0
F  -> 0
""")

def get_grade_point(letter: str):
	"""Return the grade point for a given letter grade (case-insensitive).

	If the letter is not recognized, returns None.
	"""
	mapping = {
		'A+': 4.0,
		'A': 4.0,
		'A-': 3.7,
		'B+': 3.3,
		'B': 3.0,
		'B-': 2.7,
		'C+': 2.3,
		'C': 2.0,
		'C-': 1.7,
		'D+': 1.3,
		'D': 1.0,
		'F': 0.0,
	}
	if letter is None:
		return None
	key = letter.strip().upper()
	return mapping.get(key)


def main():
	prompt = "Nhập ký tự điểm (ví dụ A, A-, B+). Nhấn Ctrl+C để thoát: "
	try:
		while True:
			s = input(prompt)
			gp = get_grade_point(s)
			if gp is None:
				print("Ký tự không hợp lệ. Vui lòng nhập lại.")
				continue
			# Print with one decimal place for nicer formatting (matches table)
			if gp.is_integer():
				# e.g., 4.0 -> show 4.0
				print(f"Điểm tương ứng: {gp:.1f}")
			else:
				print(f"Điểm tương ứng: {gp}")
			break
	except KeyboardInterrupt:
		print("\nThoát chương trình.")


if __name__ == '__main__':
	main()

