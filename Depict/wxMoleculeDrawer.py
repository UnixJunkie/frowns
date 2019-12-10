import MoleculeDrawer
from wxPython.wx import *

class wxMixin(wxScrolledWindow):
    def _init(self, parent, height=None, width=None):
        self.x0 = 0
        self.y0 = 0
        self.name = ""
        if height is None and width is None:
            size = parent.GetClientSize()
        else:
            size = (width, height)
        self.parent = parent
        wxScrolledWindow.__init__(self, parent, -1, (0,0), size,
                                  wxSUNKEN_BORDER)

        self._textFont = "HELVETICA"
        self.SetBackgroundColour(wxNamedColor("WHITE"))
        
        # flag used to redraw only when necessary
        EVT_PAINT(self, self.OnPaint)
        EVT_SIZE(self, self.OnSize)

    def _clear(self):        
        return 1
    
    def OnSize(self, event):
        self.Refresh()
        
    def OnPaint(self, event, dc=None):
        self.width, self.height = self.GetSize()

        if dc is None:
            dc = self.dc = wxPaintDC(self)
        else:
            self.dc = dc
            
        self.PrepareDC(dc)
        dc.BeginDrawing()

        if self.name:
            fontsize = min(16, self.width/len(self.name))
            self._drawText(self.name,  "Arial", fontsize, self.width/2, self.height-2*fontsize, "red")
            
        self.draw()

        dc.EndDrawing()
        # we need to clean up the dc otherwise terror ensues!
        self.dc = None

    def _drawPoly(self, coords, color="black"):
        dc = self.dc
        pen = dc.GetPen()
        brush = dc.GetBrush()
        if color is not None:
            dc.SetPen(wxPen(color, 1, wxSOLID))
            dc.SetBrush(wxBrush(color, wxSOLID))
        self.dc.DrawPolygon(coords)
        dc.SetPen(pen)
        dc.SetBrush(brush)
        
    def _drawOval(self, x, y, xh, yh):
        self.dc.DrawEllipseXY(self.x0+x, self.y0+y, xh-x, yh-y)
        
    def _drawLine(self, x1, y1, x2, y2, color):
        color = wxTheColourDatabase.FindColour(color)
        dc = self.dc
        pen = dc.GetPen()
        if color is not None:
            dc.SetPen(wxPen(color, 1, wxSOLID))
            
        self.dc.DrawLineXY(self.x0+x1, self.y0+y1, self.x0+x2, self.y0+y2)
        dc.SetPen(pen)
        
    def _drawText(self, text, font, fontsize, x, y, color, bg="white"):
        dc = self.dc
        font = wxFont(fontsize, wxDEFAULT, wxNORMAL, wxNORMAL,
                      0, self._textFont)
        dc.SetFont(font)
        w,h = dc.GetTextExtent(text)
        w+=2
        h+=2
        x -= w/2
        y -= h/2

        pen = dc.GetPen()
        # hack        
        dc.SetPen(wxWHITE_PEN)
        dc.DrawRectangleXY(self.x0+x, self.y0+y, w, h)
        
        dc.DrawTextXY(text, self.x0+x, self.y0+y)
        dc.SetPen(pen)

class MoleculeDrawer(MoleculeDrawer.DrawMolHarness, wxMixin):
    pass

test = """
  -ISIS-  04190215142D

 21 23  0  0  0  0  0  0  0  0999 V2000
    0.9750   -0.1292    0.0000 N   0  0  3  0  0  0  0  0  0  0  0  0
    0.5375    0.4833    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.5375   -0.7250    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.1750    0.2583    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.1750   -0.4917    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.3917   -0.4917    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.7167   -0.0542    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.7667    1.2083    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
    3.9750    0.1333    0.0000 C   0  0  3  0  0  0  0  0  0  0  0  0
    3.2250    0.0750    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    5.1417   -0.4292    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
    2.0375    0.6250    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.1542   -0.6667    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.9042   -0.6042    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.7875    0.6958    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.0667   -1.1667    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
   -0.8208    0.6333    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.8208   -0.8667    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.3000    0.8083    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.4708    0.2583    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.4708   -0.4917    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  2  1  1  0  0  0  0
  3  1  1  0  0  0  0
  4  2  1  0  0  0  0
  5  3  1  0  0  0  0
  6  9  1  0  0  0  0
  7  1  1  0  0  0  0
  8  2  2  0  0  0  0
  9 10  1  0  0  0  0
 10 14  1  0  0  0  0
 11  6  2  0  0  0  0
 12  7  2  0  0  0  0
 13  7  1  0  0  0  0
 14 13  2  0  0  0  0
 15 12  1  0  0  0  0
 16  6  1  0  0  0  0
 17  4  1  0  0  0  0
 18  5  1  0  0  0  0
 19  9  1  0  0  0  0
 20 17  2  0  0  0  0
 21 18  2  0  0  0  0
  4  5  2  0  0  0  0
 10 15  2  0  0  0  0
 20 21  1  0  0  0  0
M  END

$$$$
"""

class testApp(wxApp):
    def OnInit(self):
        from frowns import MDL
        from StringIO import StringIO
        reader = MDL.sdin(StringIO(test))
        
        mol, error, text = reader.next()
        wxInitAllImageHandlers()
        frame = wxFrame(None, -1, "", size=(350,200))

        
        drawer = self.drawer = MoleculeDrawer(frame, drawAromatic=0)
        drawer.setMolecule(mol)
        frame.Show(TRUE)
        return TRUE

 
if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../../")
    _app = testApp(0)
    _app.MainLoop()
