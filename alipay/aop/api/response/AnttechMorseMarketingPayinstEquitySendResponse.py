#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PayInstEquitySendResult import PayInstEquitySendResult


class AnttechMorseMarketingPayinstEquitySendResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingPayinstEquitySendResponse, self).__init__()
        self._biz_no = None
        self._result_details = None
        self._send_order_id = None
        self._send_success = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def result_details(self):
        return self._result_details

    @result_details.setter
    def result_details(self, value):
        if isinstance(value, list):
            self._result_details = list()
            for i in value:
                if isinstance(i, PayInstEquitySendResult):
                    self._result_details.append(i)
                else:
                    self._result_details.append(PayInstEquitySendResult.from_alipay_dict(i))
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value
    @property
    def send_success(self):
        return self._send_success

    @send_success.setter
    def send_success(self, value):
        self._send_success = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingPayinstEquitySendResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'result_details' in response:
            self.result_details = response['result_details']
        if 'send_order_id' in response:
            self.send_order_id = response['send_order_id']
        if 'send_success' in response:
            self.send_success = response['send_success']
