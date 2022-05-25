#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantMemberwalletWalletQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantMemberwalletWalletQueryResponse, self).__init__()
        self._open = None
        self._open_time = None
        self._open_url = None
        self._wallet_id = None

    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, value):
        self._open = value
    @property
    def open_time(self):
        return self._open_time

    @open_time.setter
    def open_time(self, value):
        self._open_time = value
    @property
    def open_url(self):
        return self._open_url

    @open_url.setter
    def open_url(self, value):
        self._open_url = value
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantMemberwalletWalletQueryResponse, self).parse_response_content(response_content)
        if 'open' in response:
            self.open = response['open']
        if 'open_time' in response:
            self.open_time = response['open_time']
        if 'open_url' in response:
            self.open_url = response['open_url']
        if 'wallet_id' in response:
            self.wallet_id = response['wallet_id']
