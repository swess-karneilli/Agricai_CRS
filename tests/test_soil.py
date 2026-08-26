from owslib.wcs import WebCoverageService

url = "https://maps.isric.org/mapserv?map=/map/phh2o.map"

wcs = WebCoverageService(
    url,
    version="2.0.1"
)

print("Connected to SoilGrids WCS")

print("\nAvailable layers:")

for layer in wcs.contents:
    print(layer)