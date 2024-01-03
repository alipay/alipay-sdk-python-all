#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundWalletPayurlApplyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._payment_mode = None
        self._product_code = None
        self._user_wallet_id = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def payment_mode(self):
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, value):
        self._payment_mode = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.payment_mode:
            if hasattr(self.payment_mode, 'to_alipay_dict'):
                params['payment_mode'] = self.payment_mode.to_alipay_dict()
            else:
                params['payment_mode'] = self.payment_mode
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.user_wallet_id:
            if hasattr(self.user_wallet_id, 'to_alipay_dict'):
                params['user_wallet_id'] = self.user_wallet_id.to_alipay_dict()
            else:
                params['user_wallet_id'] = self.user_wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundWalletPayurlApplyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'payment_mode' in d:
            o.payment_mode = d['payment_mode']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        return o


