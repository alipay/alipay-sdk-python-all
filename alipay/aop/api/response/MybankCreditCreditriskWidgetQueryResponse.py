#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditCreditriskWidgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditCreditriskWidgetQueryResponse, self).__init__()
        self._widgetjson = None

    @property
    def widgetjson(self):
        return self._widgetjson

    @widgetjson.setter
    def widgetjson(self, value):
        self._widgetjson = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditCreditriskWidgetQueryResponse, self).parse_response_content(response_content)
        if 'widgetjson' in response:
            self.widgetjson = response['widgetjson']
