import sys

from pytz import unicode

from Sql.lib.conf import Config

if sys.version_info[0] > 2:
    from django.utils.translation import gettext_lazy as _
else:
    new_str = unicode
    from django.utils.translation import ugettext_lazy as _

LEAFLET_TILE_LAYER = Config(
    key="leaflet_tile_layer",
    help=_(
        "Tile layer server URL for the Leaflet map charts. Read more on http://leafletjs.com/reference.html#tilelayer. "
        "Make sure you add the tile domain to the img-src section of the 'secure_content_security_policy' "
        "configuration parameter as well."),
    type=str,
    default="http://{s}.tile.osm.org/{z}/{x}/{y}.png")

LEAFLET_TILE_LAYER_ATTRIBUTION = Config(
    key="leaflet_tile_layer_attribution",
    help=_("The copyright message for the specified Leaflet maps Tile Layer"),
    default='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors')
