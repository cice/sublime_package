import sublime, sublime_plugin

class FocusNextGroup(sublime_plugin.WindowCommand):
	def run(self):
		w = sublime.active_window()
		n = w.num_groups()
		c = w.active_group()
		g = c + 1

		if(g == n):
			g = 0

		w.focus_group(g)
