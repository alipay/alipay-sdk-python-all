#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasTransferPaymentDisburseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTransferPaymentDisburseResponse, self).__init__()
        self._pass_through_info = None
        self._transaction_results = None

    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def transaction_results(self):
        return self._transaction_results

    @transaction_results.setter
    def transaction_results(self, value):
        self._transaction_results = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTransferPaymentDisburseResponse, self).parse_response_content(response_content)
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']
        if 'transaction_results' in response:
            self.transaction_results = response['transaction_results']
