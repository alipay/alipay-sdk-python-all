#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseContentlibStandardcontentPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseContentlibStandardcontentPublishResponse, self).__init__()
        self._content_id = None
        self._extra_msg = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def extra_msg(self):
        return self._extra_msg

    @extra_msg.setter
    def extra_msg(self, value):
        self._extra_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseContentlibStandardcontentPublishResponse, self).parse_response_content(response_content)
        if 'content_id' in response:
            self.content_id = response['content_id']
        if 'extra_msg' in response:
            self.extra_msg = response['extra_msg']
