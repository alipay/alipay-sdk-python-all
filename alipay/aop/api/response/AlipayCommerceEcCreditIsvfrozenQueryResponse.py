#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcCreditIsvfrozenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcCreditIsvfrozenQueryResponse, self).__init__()
        self._frozen_amount = None
        self._frozen_time = None
        self._status = None

    @property
    def frozen_amount(self):
        return self._frozen_amount

    @frozen_amount.setter
    def frozen_amount(self, value):
        self._frozen_amount = value
    @property
    def frozen_time(self):
        return self._frozen_time

    @frozen_time.setter
    def frozen_time(self, value):
        self._frozen_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcCreditIsvfrozenQueryResponse, self).parse_response_content(response_content)
        if 'frozen_amount' in response:
            self.frozen_amount = response['frozen_amount']
        if 'frozen_time' in response:
            self.frozen_time = response['frozen_time']
        if 'status' in response:
            self.status = response['status']
