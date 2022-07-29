# Izak
# July 2022
# References:
# 		https://tkdocs.com/tutorial/widgets.html#button:~:text=do%20that%20yourself.-,The%20Command%20Callback,-The%20command%20option
# 		https://www.pythontutorial.net/tkinter/tkinter-command/#:~:text=Introduction%20to%20Tkinter%20command%20binding

from tkinter import *
from tkinter import ttk

from os import system
import sys

def test():
	# https://stackoverflow.com/a/19719292
	# if not admin.isUserAdmin():
	#     admin.runAsAdmin()

	root = Tk(className="Blog Build Buttons")
	content = ttk.Frame(root)

	mainframe = ttk.Frame(content, padding="3 3 12 12")
	# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	# root.columnconfigure(0, weight=1)
	# root.rowconfigure(0, weight=1)
	root.geometry("300x100")

	def build_serve():
		# system("""echo Starting""")
		# system("""npx @11ty/eleventy""")
		# system("""npm run s""")
		system("""echo Starting
		npx @11ty/eleventy
		npm run s""")

	def git(*args):
		system("cd ../")
		system("cd")
		system('echo directory changed')
		system("git pull")
		system("git add -A")
		system('git commit -m "{}"'.format(msg.get()))
		system("git push")
		system("cd _eleventy")

	build_serve_button = ttk.Button(root, text="Build & Serve", default="active", command=build_serve)

	msg = StringVar()
	msg_entry = ttk.Entry(root, width=7, textvariable=msg)
	msg_entry.grid(column=3, row=1)

	git_button = ttk.Button(root, text="Git", default="active", command=git)
	
	build_serve_button.grid(row=1, column=1)
	git_button.grid(row=1, column=2)

	root.mainloop()

if __name__ == "__main__":
    sys.exit(test())