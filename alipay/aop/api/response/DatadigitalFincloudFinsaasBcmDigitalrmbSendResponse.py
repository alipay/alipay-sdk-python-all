#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasBcmDigitalrmbSendResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasBcmDigitalrmbSendResponse, self).__init__()
        self._page_stage = None
        self._prize_code = None
        self._prize_price = None
        self._send_result = None

    @property
    def page_stage(self):
        return self._page_stage

    @page_stage.setter
    def page_stage(self, value):
        self._page_stage = value
    @property
    def prize_code(self):
        return self._prize_code

    @prize_code.setter
    def prize_code(self, value):
        self._prize_code = value
    @property
    def prize_price(self):
        return self._prize_price

    @prize_price.setter
    def prize_price(self, value):
        self._prize_price = value
    @property
    def send_result(self):
        return self._send_result

    @send_result.setter
    def send_result(self, value):
        self._send_result = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasBcmDigitalrmbSendResponse, self).parse_response_content(response_content)
        if 'page_stage' in response:
            self.page_stage = response['page_stage']
        if 'prize_code' in response:
            self.prize_code = response['prize_code']
        if 'prize_price' in response:
            self.prize_price = response['prize_price']
        if 'send_result' in response:
            self.send_result = response['send_result']
