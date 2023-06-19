#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGamecenterPaymentQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGamecenterPaymentQuerystatusResponse, self).__init__()
        self._cp_extra = None
        self._status = None

    @property
    def cp_extra(self):
        return self._cp_extra

    @cp_extra.setter
    def cp_extra(self, value):
        self._cp_extra = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGamecenterPaymentQuerystatusResponse, self).parse_response_content(response_content)
        if 'cp_extra' in response:
            self.cp_extra = response['cp_extra']
        if 'status' in response:
            self.status = response['status']
