from drf_spectacular import renderers


class XLSXRenderer(renderers.BaseRenderer):
    media_type = "application/vnd.ms-excel"
    format = "xlsx"
    charset = None
    render_style = "binary"

    def render(self, data, media_type=None, renderer_context=None):
        return data
