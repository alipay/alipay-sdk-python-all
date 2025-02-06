#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceSchemaapifirstRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceSchemaapifirstRainystestQueryResponse, self).__init__()
        self._orderStr = None

    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceSchemaapifirstRainystestQueryResponse, self).parse_response_content(response_content)
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
