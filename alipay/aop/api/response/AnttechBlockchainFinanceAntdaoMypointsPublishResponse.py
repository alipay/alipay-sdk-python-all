#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceAntdaoMypointsPublishResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceAntdaoMypointsPublishResponse, self).__init__()
        self._card_url = None
        self._data = None
        self._total_amount = None
        self._total_ccost = None

    @property
    def card_url(self):
        return self._card_url

    @card_url.setter
    def card_url(self, value):
        self._card_url = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_ccost(self):
        return self._total_ccost

    @total_ccost.setter
    def total_ccost(self, value):
        self._total_ccost = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceAntdaoMypointsPublishResponse, self).parse_response_content(response_content)
        if 'card_url' in response:
            self.card_url = response['card_url']
        if 'data' in response:
            self.data = response['data']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_ccost' in response:
            self.total_ccost = response['total_ccost']
