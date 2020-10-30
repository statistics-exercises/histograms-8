import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
        fighand = plt.gca()
        for i in range(nparam+1) :
            x, y = fighand.patches[i].get_xy() 
            self.assertTrue( np.fabs(x+0.5*fighand.patches[i].get_width()-i)<1e-7, "the x-coordinates of the bars in your histogram are not correct" )
  
    def test_normalisation(self) : 
        ssum = 0.
        fighand=plt.gca()
        for i in range(nparam+1) : ssum = ssum + fighand.patches[i].get_height()
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "your histogram is not normalised" )

    def test_plot(self) : 
        fighand=plt.gca()
        for i in range(nparam+1) :
            pval = sp.binom( nparam, i )*pow(prob,i)*pow( 1-prob, nparam-i )
            bar = np.sqrt( pval*(1-pval)  )*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( fighand.patches[i].get_height() - pval )<bar, "the heights of the bars in your histogram suggest that you have sampled the histogram incorrectly") )
