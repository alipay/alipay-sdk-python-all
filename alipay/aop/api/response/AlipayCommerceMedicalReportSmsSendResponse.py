#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalReportSmsSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalReportSmsSendResponse, self).__init__()
        self._out_order_no = None
        self._sms_sent = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def sms_sent(self):
        return self._sms_sent

    @sms_sent.setter
    def sms_sent(self, value):
        self._sms_sent = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalReportSmsSendResponse, self).parse_response_content(response_content)
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'sms_sent' in response:
            self.sms_sent = response['sms_sent']
