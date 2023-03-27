#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCreditlinkloanDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCreditlinkloanDataQueryResponse, self).__init__()
        self._collect_data_content = None
        self._merchant_biz_no = None

    @property
    def collect_data_content(self):
        return self._collect_data_content

    @collect_data_content.setter
    def collect_data_content(self, value):
        self._collect_data_content = value
    @property
    def merchant_biz_no(self):
        return self._merchant_biz_no

    @merchant_biz_no.setter
    def merchant_biz_no(self, value):
        self._merchant_biz_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCreditlinkloanDataQueryResponse, self).parse_response_content(response_content)
        if 'collect_data_content' in response:
            self.collect_data_content = response['collect_data_content']
        if 'merchant_biz_no' in response:
            self.merchant_biz_no = response['merchant_biz_no']
