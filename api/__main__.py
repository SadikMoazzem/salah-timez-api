import os
import sys

sys.path.append(os.path.dirname(__file__) + os.sep + os.pardir)
from api import app


# -------- Entrypoint via console ----------
app.run(host='0.0.0.0', threaded=True)