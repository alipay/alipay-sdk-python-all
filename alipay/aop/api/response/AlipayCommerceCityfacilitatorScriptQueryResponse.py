#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCityfacilitatorScriptQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorScriptQueryResponse, self).__init__()
        self._content = None
        self._gmt_modified = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorScriptQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
