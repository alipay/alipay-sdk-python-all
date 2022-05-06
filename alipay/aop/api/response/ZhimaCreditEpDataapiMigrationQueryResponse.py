#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpDataapiMigrationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDataapiMigrationQueryResponse, self).__init__()
        self._content = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDataapiMigrationQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
