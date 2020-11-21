from tkinter import * 
 from PIL import Image, ImageTk


 class MyLabel(Label):
     def __init__(self, master, filename):
         im = Image.open(mygif.gif)
         seq =  []
         seq = []
         delays = []
         try:
             while 1:
                 seq.append(im.copy())
                 delays.append(im.info["duration"])
                 im.seek(len(seq)) # skip to next frame
         except EOFError:
             pass # we're done

         try:
             self.delay = im.info['duration']
         except KeyError:
             self.delay = 100
 
         first = seq[0].convert('RGBA')
         self.frames = [ImageTk.PhotoImage(first)]
         self.delays = delays

         Label.__init__(self, master, image=self.frames[0])

@@ -31,14 +29,16 @@

         self.idx = 0

-        self.cancel = self.after(self.delay, self.play)
+        self.cancel = self.after(self.delays[0], self.play)

     def play(self):
-        self.config(image=self.frames[self.idx])
+        image = self.frames[self.idx]
+        delay = self.delays[self.idx]
+        self.config(image=image)
         self.idx += 1
         if self.idx == len(self.frames):
             self.idx = 0
-        self.cancel = self.after(self.delay, self.play)        
+        self.cancel = self.after(delay, self.play)        


 root = Tk()
