#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistCarfinauctionApplyloanNotifyResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistCarfinauctionApplyloanNotifyResponse, self).__init__()
        self._disburse_time = None

    @property
    def disburse_time(self):
        return self._disburse_time

    @disburse_time.setter
    def disburse_time(self, value):
        self._disburse_time = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistCarfinauctionApplyloanNotifyResponse, self).parse_response_content(response_content)
        if 'disburse_time' in response:
            self.disburse_time = response['disburse_time']
