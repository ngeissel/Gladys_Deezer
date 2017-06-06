#!/usr/bin/env python
# coding: utf8

import subprocess
import json
import urllib2

def text_recognition(text):
	# print "TEXT RECOGNITION"
	# print text
	# Jouer un artiste
	if text[:8] == "joue du ":
		artist = text[8:].replace(" ", "+")
		track = urllib2.urlopen("https://api.deezer.com/search?q=" + artist).read()
		track = json.loads(track)
		print(track["data"][0]["album"]["title"])
		# play_music("dzmedia:///album/" + str(track["data"][0]["album"]["id"]))
		return "dzmedia:///album/" + str(track["data"][0]["album"]["id"])

	# Jouer un album
	if text[:13] == "joue l'album ":
		album = text[13:].replace(" ", "+")
		track = urllib2.urlopen("https://api.deezer.com/search?q=" + album).read()
		track = json.loads(track)
		print(track["data"][0]["album"]["title"])
		# play_music("dzmedia:///album/" + str(track["data"][0]["album"]["id"]))
		return "dzmedia:///album/" + str(track["data"][0]["album"]["id"])

	# Jouer une musique
	if text[:16] == "joue la musique ":
		music = text[16:].replace(" ", "+")
		track = urllib2.urlopen("https://api.deezer.com/search?q=" + music).read()
		track = json.loads(track)
		print(track)
		# play_music("dzmedia:///track/" + str(track["data"][0]["id"]))
		return "dzmedia:///track/" + str(track["data"][0]["id"])

	# Jouer la radio
	if text[:5] == "joue " and text[len(text) - 17:] == " sur Orange radio":
		radio_name = text[5:len(text) - 17]
		print "\"" + radio_name + "\""
		return "radio" + radio_name
		# play_radio(radio_name)

	# Couper la radio
	if text == "coupe la radio" or text == "arrête la radio" or text == "coupe la musique":
		subprocess.call(["killall mplayer"], shell=True)
		return "null_command"

	# Configurer le volume
	if text[:17] == "mets le volume a " or text[:17] == "mets le volume à ":
		value = text[17:]
		# Correction lors de la lecture des valeurs
		if value == "zéro":
			value = 0
		elif value == "deux":
			value = 2
		else:
			value = int(text[17:])
		volume = 10 * value
		subprocess.call( "./set_volume.sh " + str(volume) + "%", shell=True)
		return "null_command"

	return "null_command"
