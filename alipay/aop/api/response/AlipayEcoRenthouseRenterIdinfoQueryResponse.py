#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoRenthouseRenterIdinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoRenthouseRenterIdinfoQueryResponse, self).__init__()
        self._status_value = None

    @property
    def status_value(self):
        return self._status_value

    @status_value.setter
    def status_value(self, value):
        self._status_value = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoRenthouseRenterIdinfoQueryResponse, self).parse_response_content(response_content)
        if 'status_value' in response:
            self.status_value = response['status_value']
