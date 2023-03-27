#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletWithdrawResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletWithdrawResponse, self).__init__()
        self._bill_no = None
        self._biz_scene = None
        self._user_wallet_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletWithdrawResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
