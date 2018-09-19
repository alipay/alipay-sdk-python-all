#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniTinyappExistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTinyappExistQueryResponse, self).__init__()
        self._exist_mini = None

    @property
    def exist_mini(self):
        return self._exist_mini

    @exist_mini.setter
    def exist_mini(self, value):
        self._exist_mini = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTinyappExistQueryResponse, self).parse_response_content(response_content)
        if 'exist_mini' in response:
            self.exist_mini = response['exist_mini']
