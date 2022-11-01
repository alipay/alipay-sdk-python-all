#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserSportshealthAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSportshealthAccountQueryResponse, self).__init__()
        self._balance_amount = None
        self._open_id = None
        self._user_id = None

    @property
    def balance_amount(self):
        return self._balance_amount

    @balance_amount.setter
    def balance_amount(self, value):
        self._balance_amount = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSportshealthAccountQueryResponse, self).parse_response_content(response_content)
        if 'balance_amount' in response:
            self.balance_amount = response['balance_amount']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
