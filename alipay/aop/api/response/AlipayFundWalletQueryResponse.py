#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletQueryResponse, self).__init__()
        self._identity_name = None
        self._identity_no = None
        self._out_biz_no = None
        self._user_wallet_id = None

    @property
    def identity_name(self):
        return self._identity_name

    @identity_name.setter
    def identity_name(self, value):
        self._identity_name = value
    @property
    def identity_no(self):
        return self._identity_no

    @identity_no.setter
    def identity_no(self, value):
        self._identity_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletQueryResponse, self).parse_response_content(response_content)
        if 'identity_name' in response:
            self.identity_name = response['identity_name']
        if 'identity_no' in response:
            self.identity_no = response['identity_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
