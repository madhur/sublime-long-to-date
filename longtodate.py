import sublime, sublime_plugin
from datetime import datetime

class LongToDate(sublime_plugin.TextCommand):
    def run(self, edit):
        #self.view.insert(edit, 0, "Hello, World!")
        sels = self.view.sel()
        print (sels)
        for sel in sels:
            print (sel)
            long_date = str(self.view.substr(sel))
            

def long_to_text(long_date):
    try:
        text_date = datetime.fromtimestamp(int(long_date)).strftime('%Y-%m-%d %H:%M:%S')
        return "{0} -> {1}".format(long_date, text_date)
    except ValueError:
        return None




class EventDump(sublime_plugin.EventListener):  
    def on_selection_modified(self, view):

        sels = view.sel()
        for sel in sels:
            long_date = str(view.substr(sel))
            text_date = long_to_text(long_date)
            if text_date != None:
                sublime.status_message(text_date)
            #self.view.set_status('long_to_date', text_date)