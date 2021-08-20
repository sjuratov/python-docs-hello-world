from flask import Flask, render_template
import logging, os
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

APPINSIGHTS_INSTRUMENTATIONKEY = os.environ.get("APPINSIGHTS_INSTRUMENTATIONKEY")
CONNECTION_STRING = 'InstrumentationKey=' + APPINSIGHTS_INSTRUMENTATIONKEY

logger.addHandler(AzureLogHandler(
    connection_string=CONNECTION_STRING)
)

app = Flask(__name__)

@app.route("/")
def index():
    
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Render HTML with count variable
    return render_template("index.html", count=count)

    # Log event
    logger.info(count)

if __name__ == "__main__":
    app.run()