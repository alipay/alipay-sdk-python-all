#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserQuanyibaoOpenbenefitSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserQuanyibaoOpenbenefitSendResponse, self).__init__()
        self._send_biz_no = None
        self._send_status = None

    @property
    def send_biz_no(self):
        return self._send_biz_no

    @send_biz_no.setter
    def send_biz_no(self, value):
        self._send_biz_no = value
    @property
    def send_status(self):
        return self._send_status

    @send_status.setter
    def send_status(self, value):
        self._send_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserQuanyibaoOpenbenefitSendResponse, self).parse_response_content(response_content)
        if 'send_biz_no' in response:
            self.send_biz_no = response['send_biz_no']
        if 'send_status' in response:
            self.send_status = response['send_status']
