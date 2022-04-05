import sublime
import sublime_plugin

class ViewTabs(sublime_plugin.EventListener):

    def on_activated_async(self, view):
        if len(sublime.active_window().sheets()) > 1:
            sublime.active_window().set_tabs_visible(True)

    def on_close(self, view):
        if len(sublime.active_window().sheets()) < 2:
            sublime.active_window().set_tabs_visible(False)

    def on_new_window_async(self, window):
        if len(sublime.active_window().sheets()) < 2:
            sublime.active_window().set_tabs_visible(False)

class LineHighlight(sublime_plugin.ViewEventListener):
    def on_activated_async(self):
        self.view.settings().set("highlight_line", True)

    def on_deactivated_async(self):
        self.view.settings().set("highlight_line", False)
