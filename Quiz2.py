import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.output(17, GPIO.LOW)
GPIO.output(18, GPIO.LOW)

score = 0

def correct_light():
	"Answer correctly and turn on the green light"
	GPIO.output(17, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17, GPIO.LOW)

def wrong_light():
	"Answer incorrectly and turn on the red light"
	GPIO.output(18, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(18, GPIO.LOW)

print("1. Which of the following is NOT a python data type?")
print("a.int b.float c.rational d.string e.bool")
ans = input("enter a/b/c/d/e：").upper()
if ans == "c":
	print("正确！")
	correct_light()
	score += 1
else:
	print("Incorrect！")
	wrong_light()

print("\n2. Which of the following is NOT a built-in operation in Python?")
print("a.+ b.% c.abs() d.sqrt()")
ans = input("enter a/b/c/d：").upper()
if ans == "d":
	print("Correct！")
	correct_light()
	score += 1
else:
	print("	Incorrect！")
	wrong_light()

print("\n3. In a mixed-type expression involving ints and floats, Python will convert:")
print("a.floats to ints b.ints to strings c.floats and ints to strings d.ints to floats")
ans = input("enter a/b/c/d：").upper()
if ans == "d":
	print("Correct！")
	correct_light()
	score += 1
else:
	print("Incorrect！")
	wrong_light()

print("\n4. The best structure for implementing a multi-way decision in Python is:")
print("a.if b.if-else c.if-elif-else d.try")
ans = input("enter a/b/c/d：").upper()
if ans == "c":
	print("Correct！")
	correct_light()
	score += 1
else:
	print("Incorrect！")
	wrong_light()


print("\n5. What statement can be executed in the body of a loop to cause it to terminate?")
print("A. if B. exit C. continue d.break")
ans = input("enter a/b/c/d：").upper()
if ans == "d":
	print("Correct！")
	correct_light()
	score += 1
else:
	print("Incorrect！")
	wrong_light()

print(f"\nGame over！Final score：{score}/5")

GPIO.cleanup()

