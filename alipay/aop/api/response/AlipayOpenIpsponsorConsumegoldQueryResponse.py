#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIpsponsorConsumegoldQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIpsponsorConsumegoldQueryResponse, self).__init__()
        self._open_status = None
        self._total_amount = None

    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIpsponsorConsumegoldQueryResponse, self).parse_response_content(response_content)
        if 'open_status' in response:
            self.open_status = response['open_status']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
