#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalReportSmsSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalReportSmsSendResponse, self).__init__()
        self._sms_sent = None

    @property
    def sms_sent(self):
        return self._sms_sent

    @sms_sent.setter
    def sms_sent(self, value):
        self._sms_sent = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalReportSmsSendResponse, self).parse_response_content(response_content)
        if 'sms_sent' in response:
            self.sms_sent = response['sms_sent']
