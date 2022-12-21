#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestGrayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestGrayQueryResponse, self).__init__()
        self._res = None

    @property
    def res(self):
        return self._res

    @res.setter
    def res(self, value):
        self._res = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestGrayQueryResponse, self).parse_response_content(response_content)
        if 'res' in response:
            self.res = response['res']
