#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiSceneprodBenefitSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiSceneprodBenefitSendResponse, self).__init__()
        self._retry = None
        self._send_id = None
        self._status = None

    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def send_id(self):
        return self._send_id

    @send_id.setter
    def send_id(self, value):
        self._send_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiSceneprodBenefitSendResponse, self).parse_response_content(response_content)
        if 'retry' in response:
            self.retry = response['retry']
        if 'send_id' in response:
            self.send_id = response['send_id']
        if 'status' in response:
            self.status = response['status']
