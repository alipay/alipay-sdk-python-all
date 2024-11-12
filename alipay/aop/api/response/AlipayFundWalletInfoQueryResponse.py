#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletInfoQueryResponse, self).__init__()
        self._create_time = None
        self._modify_time = None
        self._open_id = None
        self._status = None
        self._user_id = None
        self._user_wallet_id = None
        self._wallet_template_id = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletInfoQueryResponse, self).parse_response_content(response_content)
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'modify_time' in response:
            self.modify_time = response['modify_time']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'status' in response:
            self.status = response['status']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
        if 'wallet_template_id' in response:
            self.wallet_template_id = response['wallet_template_id']
