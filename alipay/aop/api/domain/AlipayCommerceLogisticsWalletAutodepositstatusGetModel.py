#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsWalletAutodepositstatusGetModel(object):

    def __init__(self):
        self._biz_product_code = None
        self._biz_scene_code = None
        self._open_id = None
        self._user_id = None
        self._user_wallet_id = None
        self._wallet_partner_id = None
        self._wallet_template_id = None

    @property
    def biz_product_code(self):
        return self._biz_product_code

    @biz_product_code.setter
    def biz_product_code(self, value):
        self._biz_product_code = value
    @property
    def biz_scene_code(self):
        return self._biz_scene_code

    @biz_scene_code.setter
    def biz_scene_code(self, value):
        self._biz_scene_code = value
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
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value
    @property
    def wallet_partner_id(self):
        return self._wallet_partner_id

    @wallet_partner_id.setter
    def wallet_partner_id(self, value):
        self._wallet_partner_id = value
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product_code:
            if hasattr(self.biz_product_code, 'to_alipay_dict'):
                params['biz_product_code'] = self.biz_product_code.to_alipay_dict()
            else:
                params['biz_product_code'] = self.biz_product_code
        if self.biz_scene_code:
            if hasattr(self.biz_scene_code, 'to_alipay_dict'):
                params['biz_scene_code'] = self.biz_scene_code.to_alipay_dict()
            else:
                params['biz_scene_code'] = self.biz_scene_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_wallet_id:
            if hasattr(self.user_wallet_id, 'to_alipay_dict'):
                params['user_wallet_id'] = self.user_wallet_id.to_alipay_dict()
            else:
                params['user_wallet_id'] = self.user_wallet_id
        if self.wallet_partner_id:
            if hasattr(self.wallet_partner_id, 'to_alipay_dict'):
                params['wallet_partner_id'] = self.wallet_partner_id.to_alipay_dict()
            else:
                params['wallet_partner_id'] = self.wallet_partner_id
        if self.wallet_template_id:
            if hasattr(self.wallet_template_id, 'to_alipay_dict'):
                params['wallet_template_id'] = self.wallet_template_id.to_alipay_dict()
            else:
                params['wallet_template_id'] = self.wallet_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsWalletAutodepositstatusGetModel()
        if 'biz_product_code' in d:
            o.biz_product_code = d['biz_product_code']
        if 'biz_scene_code' in d:
            o.biz_scene_code = d['biz_scene_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        if 'wallet_partner_id' in d:
            o.wallet_partner_id = d['wallet_partner_id']
        if 'wallet_template_id' in d:
            o.wallet_template_id = d['wallet_template_id']
        return o


