import sublime
import sublime_plugin


class ViewTabs(sublime_plugin.EventListener):
    def on_new_window(self, window):
        if len(window.sheets()) > 1:
            window.set_tabs_visible(True)
        else:
            window.set_tabs_visible(False)

    def on_load_project(self, window):
        if len(window.sheets()) > 1:
            window.set_tabs_visible(True)
        else:
            window.set_tabs_visible(False)

    def on_new_project(self, window):
        if len(window.sheets()) > 1:
            window.set_tabs_visible(True)
        else:
            window.set_tabs_visible(False)

    def on_activated_async(self, view):
        if len(sublime.active_window().sheets()) > 1:
            sublime.active_window().set_tabs_visible(True)

    def on_close(self, view):
        if len(sublime.active_window().sheets()) < 2:
            sublime.active_window().set_tabs_visible(False)

    def on_new_window_async(self, window):
        if len(sublime.active_window().sheets()) < 2:
            sublime.active_window().set_tabs_visible(False)
