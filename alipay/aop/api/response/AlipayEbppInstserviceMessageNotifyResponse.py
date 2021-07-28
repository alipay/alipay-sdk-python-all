#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceMessageNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceMessageNotifyResponse, self).__init__()
        self._bill_key = None
        self._status = None

    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceMessageNotifyResponse, self).parse_response_content(response_content)
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'status' in response:
            self.status = response['status']
