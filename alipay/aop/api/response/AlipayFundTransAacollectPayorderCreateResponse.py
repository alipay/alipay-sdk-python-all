#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransAacollectPayorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransAacollectPayorderCreateResponse, self).__init__()
        self._batch_no = None
        self._biz_type = None
        self._transfer_no = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def transfer_no(self):
        return self._transfer_no

    @transfer_no.setter
    def transfer_no(self, value):
        self._transfer_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransAacollectPayorderCreateResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'transfer_no' in response:
            self.transfer_no = response['transfer_no']
