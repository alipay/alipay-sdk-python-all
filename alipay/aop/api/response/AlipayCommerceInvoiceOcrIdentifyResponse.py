#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceInvoiceOcrIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceInvoiceOcrIdentifyResponse, self).__init__()
        self._raw_data_list = None

    @property
    def raw_data_list(self):
        return self._raw_data_list

    @raw_data_list.setter
    def raw_data_list(self, value):
        if isinstance(value, list):
            self._raw_data_list = list()
            for i in value:
                self._raw_data_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceInvoiceOcrIdentifyResponse, self).parse_response_content(response_content)
        if 'raw_data_list' in response:
            self.raw_data_list = response['raw_data_list']
