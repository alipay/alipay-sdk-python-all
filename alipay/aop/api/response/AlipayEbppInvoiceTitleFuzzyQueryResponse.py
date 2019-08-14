#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceTitleFuzzyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceTitleFuzzyQueryResponse, self).__init__()
        self._enterprise_name = None

    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        if isinstance(value, list):
            self._enterprise_name = list()
            for i in value:
                self._enterprise_name.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceTitleFuzzyQueryResponse, self).parse_response_content(response_content)
        if 'enterprise_name' in response:
            self.enterprise_name = response['enterprise_name']
