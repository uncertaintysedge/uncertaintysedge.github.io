# Izak
# July 2022
# References:
# 		https://tkdocs.com/tutorial/widgets.html#button:~:text=do%20that%20yourself.-,The%20Command%20Callback,-The%20command%20option
# 		https://www.pythontutorial.net/tkinter/tkinter-command/#:~:text=Introduction%20to%20Tkinter%20command%20binding

from tkinter import *
from tkinter import ttk

import subprocess
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

	_eleventy = r"C:\root\uncertaintysedge.github.io\_eleventy"
	def build_serve():
		# os.system("""echo Starting""")
		# os.system("""npx @11ty/eleventy""")
		# 0s.system("""npm run s""")
		subprocess.call(["echo", "starting..."], cwd=_eleventy, shell=True)
		subprocess.call(["cd"], cwd=_eleventy, shell=True)
		subprocess.call(["npx.cmd", "@11ty/eleventy"], cwd=_eleventy, shell=True)
		subprocess.call(["npm.cmd", "run", "s"], cwd=_eleventy, shell=True)

	blog_dir = r"C:\root\uncertaintysedge.github.io"
	def git():
		subprocess.call(["cd"], cwd=blog_dir, shell=True)
		subprocess.call("git pull".split(), cwd=blog_dir, shell=True)
		subprocess.call("git add -A".split(), cwd=blog_dir, shell=True)
		subprocess.call(['git', 'commit', '-m', '"{}"'.format(msg.get())], cwd=blog_dir, shell=True)
		subprocess.call(["git push".split()], cwd=blog_dir, shell=True)
		# call("git pull")
		# call("git add -A")
		# call('git commit -m "{}"'.format(msg.get()))
		# call("git push")

	build_serve_button = ttk.Button(root, text="Build & Serve", default="active", command=build_serve)

	msg = StringVar()
	msg_entry = ttk.Entry(root, width=7, textvariable=msg)
	msg_entry.grid(column=3, row=1)

	git_button = ttk.Button(root, text="Git", default="disabled", command=git)
	
	build_serve_button.grid(row=1, column=1)
	git_button.grid(row=1, column=2)

	root.mainloop()

if __name__ == "__main__":
    sys.exit(test())