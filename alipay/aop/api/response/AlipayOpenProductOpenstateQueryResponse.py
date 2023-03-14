#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenProductOpenstateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenProductOpenstateQueryResponse, self).__init__()
        self._effect_date = None
        self._expiry_date = None
        self._status = None

    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def expiry_date(self):
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self._expiry_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenProductOpenstateQueryResponse, self).parse_response_content(response_content)
        if 'effect_date' in response:
            self.effect_date = response['effect_date']
        if 'expiry_date' in response:
            self.expiry_date = response['expiry_date']
        if 'status' in response:
            self.status = response['status']
