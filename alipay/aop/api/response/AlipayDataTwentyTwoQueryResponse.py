#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataTwentyTwoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataTwentyTwoQueryResponse, self).__init__()
        self._return_id = None
        self._return_open_id = None

    @property
    def return_id(self):
        return self._return_id

    @return_id.setter
    def return_id(self, value):
        self._return_id = value
    @property
    def return_open_id(self):
        return self._return_open_id

    @return_open_id.setter
    def return_open_id(self, value):
        self._return_open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataTwentyTwoQueryResponse, self).parse_response_content(response_content)
        if 'return_id' in response:
            self.return_id = response['return_id']
        if 'return_open_id' in response:
            self.return_open_id = response['return_open_id']
