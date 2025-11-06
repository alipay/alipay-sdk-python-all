#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UniOpenResItemDetailInfos(object):

    def __init__(self):
        self._default_settle_target = None
        self._default_settle_type = None
        self._merchant_type = None
        self._smid = None
        self._sub_merchant_order_id = None
        self._user_wallet_id = None

    @property
    def default_settle_target(self):
        return self._default_settle_target

    @default_settle_target.setter
    def default_settle_target(self, value):
        self._default_settle_target = value
    @property
    def default_settle_type(self):
        return self._default_settle_type

    @default_settle_type.setter
    def default_settle_type(self, value):
        self._default_settle_type = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def sub_merchant_order_id(self):
        return self._sub_merchant_order_id

    @sub_merchant_order_id.setter
    def sub_merchant_order_id(self, value):
        self._sub_merchant_order_id = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.default_settle_target:
            if hasattr(self.default_settle_target, 'to_alipay_dict'):
                params['default_settle_target'] = self.default_settle_target.to_alipay_dict()
            else:
                params['default_settle_target'] = self.default_settle_target
        if self.default_settle_type:
            if hasattr(self.default_settle_type, 'to_alipay_dict'):
                params['default_settle_type'] = self.default_settle_type.to_alipay_dict()
            else:
                params['default_settle_type'] = self.default_settle_type
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.sub_merchant_order_id:
            if hasattr(self.sub_merchant_order_id, 'to_alipay_dict'):
                params['sub_merchant_order_id'] = self.sub_merchant_order_id.to_alipay_dict()
            else:
                params['sub_merchant_order_id'] = self.sub_merchant_order_id
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
        o = UniOpenResItemDetailInfos()
        if 'default_settle_target' in d:
            o.default_settle_target = d['default_settle_target']
        if 'default_settle_type' in d:
            o.default_settle_type = d['default_settle_type']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'smid' in d:
            o.smid = d['smid']
        if 'sub_merchant_order_id' in d:
            o.sub_merchant_order_id = d['sub_merchant_order_id']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        return o


