import time
import models
import pandas as pd
import urbansim.sim.simulation as sim

print "Started", time.ctime()
in_year, out_year = 2010, 2011

sim.run([
    "neighborhood_vars",         # node-level variables for hedonics

    "rsh_simulate",              # residential sales hedonic
    "rrh_simulate",              # residential rental hedonic
    #"nrh_simulate",             # non-residential rent hedonic

    #"households_relocation",
    "households_relocation_filtered",
    "households_transition",
    
    "hlcm_owner_simulate",       # location choice model for owners
    "hlcm_renter_simulate",      # location choice model for renters
    #"hlcm_simulate",
    #"hlcm_li_simulate",

    #"jobs_relocation",
    #"jobs_transition",
    #"elcm_simulate",

    "price_vars",				# node-level variables for feasibility
    "cap_rate_precompute",		# translate rental/ownership income into consistent terms

    "feasibility",				# calculate feasibility of all new building types
    "residential_developer",	# choose new buildings and create them
    #"non_residential_developer",
     
    "diagnostic_output",
    #"travel_model_output"
], years=range(in_year, out_year))
print "Finished", time.ctime()
