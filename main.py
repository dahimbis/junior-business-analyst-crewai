#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from analyst_business.crew import AnalystBusiness

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'company': 'Deloitte'
    }
    
    try:
        AnalystBusiness().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

