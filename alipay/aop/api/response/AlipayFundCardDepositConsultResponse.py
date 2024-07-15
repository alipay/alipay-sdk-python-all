#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundCardDepositConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundCardDepositConsultResponse, self).__init__()
        self._cert_no = None
        self._denomination = None
        self._expired_time = None
        self._status = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def denomination(self):
        return self._denomination

    @denomination.setter
    def denomination(self, value):
        self._denomination = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundCardDepositConsultResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'denomination' in response:
            self.denomination = response['denomination']
        if 'expired_time' in response:
            self.expired_time = response['expired_time']
        if 'status' in response:
            self.status = response['status']
