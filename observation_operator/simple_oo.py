{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#tie-point model for ice and open water\n",
    "import numpy as np\n",
    "\n",
    "def tiepoint(overfladetemperatur,snedybde,istykkelse, iskoncentration):\n",
    "    #the mar+april 2013 model\n",
    "    #Tb for sea ice\n",
    "    T6vsi = 151.981 + 0.398 * overfladetemperatur+ 23.360 * snedybde -3.031 * istykkelse\n",
    "    T6hsi = 55.262 + 0.687 * overfladetemperatur+ 12.962 * snedybde -1.664 * istykkelse\n",
    "    T10vsi = 145.878 + 0.435 * overfladetemperatur+ 0.743 * snedybde -4.202 * istykkelse\n",
    "    T10hsi = 45.107 + 0.753 * overfladetemperatur -18.7322 * snedybde -3.490 * istykkelse\n",
    "    T18vsi = 138.073 + 0.479 * overfladetemperatur -71.814 * snedybde -5.570 * istykkelse\n",
    "    T18hsi = 78.424 + 0.641 * overfladetemperatur -85.184 * snedybde -5.341 * istykkelse\n",
    "    T36vsi = 123.102 + 0.526 * overfladetemperatur -216.727 * snedybde -4.036 * istykkelse\n",
    "    T36hsi = 131.862 + 0.429 * overfladetemperatur -214.352 * snedybde -3.035 * istykkelse\n",
    "    T89vsi = 2.525 + 0.902 * overfladetemperatur -180.427 * snedybde+ 1.904 * istykkelse\n",
    "    T89hsi = 31.120 + 0.743 * overfladetemperatur -184.806 * snedybde+ 3.197 * istykkelse\n",
    "    #Tb for open water\n",
    "    T6vow=161.35\n",
    "    T6how=82.13\n",
    "    T10vow=167.34\n",
    "    T10how=88.26\n",
    "    T18vow=183.72\n",
    "    T18how=108.46\n",
    "    T36vow=196.41\n",
    "    T36how=128.23\n",
    "    T89vow=243.20\n",
    "    T89how=196.94\n",
    "    #Tb for ice and open water\n",
    "    T6vsim  = iskoncentration*T6vsi  + (1-iskoncentration)*T6vow\n",
    "    T6hsim  = iskoncentration*T6hsi  + (1-iskoncentration)*T6how\n",
    "    T10vsim = iskoncentration*T10vsi + (1-iskoncentration)*T10vow\n",
    "    T10hsim = iskoncentration*T10hsi + (1-iskoncentration)*T10how\n",
    "    T18vsim = iskoncentration*T18vsi + (1-iskoncentration)*T18vow\n",
    "    T18hsim = iskoncentration*T18hsi + (1-iskoncentration)*T18how\n",
    "    T36vsim = iskoncentration*T36vsi + (1-iskoncentration)*T36vow\n",
    "    T36hsim = iskoncentration*T36hsi + (1-iskoncentration)*T36how    \n",
    "    T89vsim = iskoncentration*T89vsi + (1-iskoncentration)*T89vow\n",
    "    T89hsim = iskoncentration*T89hsi + (1-iskoncentration)*T89how    \n",
    "        \n",
    "    Tbv=np.array([T6vsim,T10vsim,T18vsim,T36vsim,T89vsim])\n",
    "    Tbh=np.array([T6hsim,T10hsim,T18hsim,T36hsim,T89hsim])\n",
    "    return Tbv, Tbh"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
