#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletSceneSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletSceneSignResponse, self).__init__()
        self._asset_no = None
        self._available_amount = None
        self._biz_scene = None
        self._out_biz_no = None
        self._total_amount = None
        self._user_wallet_id = None

    @property
    def asset_no(self):
        return self._asset_no

    @asset_no.setter
    def asset_no(self, value):
        self._asset_no = value
    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletSceneSignResponse, self).parse_response_content(response_content)
        if 'asset_no' in response:
            self.asset_no = response['asset_no']
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'user_wallet_id' in response:
            self.user_wallet_id = response['user_wallet_id']
