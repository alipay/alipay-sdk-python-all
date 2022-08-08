#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestagainCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestagainCreateResponse, self).__init__()
        self._xxxxxx = None

    @property
    def xxxxxx(self):
        return self._xxxxxx

    @xxxxxx.setter
    def xxxxxx(self, value):
        self._xxxxxx = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestagainCreateResponse, self).parse_response_content(response_content)
        if 'xxxxxx' in response:
            self.xxxxxx = response['xxxxxx']
