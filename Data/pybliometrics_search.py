# Getting pybliometrics to work -----------------------------------------------
# pip install pybliometrics
# Connect to Erasmus VPN --> see https://my.eur.nl/en/eur/ict-1/wifi-and-vpn/vpn-connection
# Get an API key from https://dev.elsevier.com/

# PACKAGES --------------------------------------------------------------------
from pybliometrics.scopus import ScopusSearch
import pandas as pd

# Scopus search --------------------------------------------------------------

# Download the results from Scopus search
search_result = ScopusSearch("KEY(machine learning)  AND  KEY(marketing)")

# Check how many articles were found
print("Documents found:", search_result.get_results_size())

# Convert to pandas
data = pd.DataFrame(search_result.results)