#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoCplifeBasicserviceInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeBasicserviceInitializeResponse, self).__init__()
        self._bill_pay_auth_url = None
        self._next_action = None
        self._status = None

    @property
    def bill_pay_auth_url(self):
        return self._bill_pay_auth_url

    @bill_pay_auth_url.setter
    def bill_pay_auth_url(self, value):
        self._bill_pay_auth_url = value
    @property
    def next_action(self):
        return self._next_action

    @next_action.setter
    def next_action(self, value):
        self._next_action = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeBasicserviceInitializeResponse, self).parse_response_content(response_content)
        if 'bill_pay_auth_url' in response:
            self.bill_pay_auth_url = response['bill_pay_auth_url']
        if 'next_action' in response:
            self.next_action = response['next_action']
        if 'status' in response:
            self.status = response['status']
