#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudFundWalletOrderQueryModel(object):

    def __init__(self):
        self._bill_no = None
        self._bill_type = None
        self._biz_scene = None
        self._identity = None
        self._identity_open_id = None
        self._identity_type = None
        self._product_code = None
        self._user_wallet_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_open_id(self):
        return self._identity_open_id

    @identity_open_id.setter
    def identity_open_id(self, value):
        self._identity_open_id = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
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
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_open_id:
            if hasattr(self.identity_open_id, 'to_alipay_dict'):
                params['identity_open_id'] = self.identity_open_id.to_alipay_dict()
            else:
                params['identity_open_id'] = self.identity_open_id
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
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
        o = AlipayCloudFundWalletOrderQueryModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_open_id' in d:
            o.identity_open_id = d['identity_open_id']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        return o


