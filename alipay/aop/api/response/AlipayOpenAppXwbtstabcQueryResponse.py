#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppXwbtstabcQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppXwbtstabcQueryResponse, self).__init__()
        self._xwbbbdd = None

    @property
    def xwbbbdd(self):
        return self._xwbbbdd

    @xwbbbdd.setter
    def xwbbbdd(self, value):
        self._xwbbbdd = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppXwbtstabcQueryResponse, self).parse_response_content(response_content)
        if 'xwbbbdd' in response:
            self.xwbbbdd = response['xwbbbdd']
