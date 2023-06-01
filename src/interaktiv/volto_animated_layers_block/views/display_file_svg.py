from plone.namedfile.browser import DisplayFile, ALLOWED_INLINE_MIMETYPES


class DisplayFileSvg(DisplayFile):
    allowed_inline_mimetypes = ALLOWED_INLINE_MIMETYPES + ["image/svg+xml", "image/svg+xml-compressed"]
