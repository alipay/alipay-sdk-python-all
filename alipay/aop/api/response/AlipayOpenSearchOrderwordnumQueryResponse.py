#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSearchOrderwordnumQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchOrderwordnumQueryResponse, self).__init__()
        self._keyword_num = None

    @property
    def keyword_num(self):
        return self._keyword_num

    @keyword_num.setter
    def keyword_num(self, value):
        self._keyword_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchOrderwordnumQueryResponse, self).parse_response_content(response_content)
        if 'keyword_num' in response:
            self.keyword_num = response['keyword_num']
