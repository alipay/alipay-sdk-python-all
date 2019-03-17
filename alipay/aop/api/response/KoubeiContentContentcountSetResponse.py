#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiContentContentcountSetResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiContentContentcountSetResponse, self).__init__()
        self._content_id = None
        self._trace_id = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiContentContentcountSetResponse, self).parse_response_content(response_content)
        if 'content_id' in response:
            self.content_id = response['content_id']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
