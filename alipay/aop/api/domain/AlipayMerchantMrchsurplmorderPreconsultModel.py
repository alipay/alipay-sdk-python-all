#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantMrchsurplmorderPreconsultModel(object):

    def __init__(self):
        self._biz_id = None
        self._item_id = None
        self._merchant_exts = None
        self._sku_id = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def merchant_exts(self):
        return self._merchant_exts

    @merchant_exts.setter
    def merchant_exts(self, value):
        self._merchant_exts = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.merchant_exts:
            if hasattr(self.merchant_exts, 'to_alipay_dict'):
                params['merchant_exts'] = self.merchant_exts.to_alipay_dict()
            else:
                params['merchant_exts'] = self.merchant_exts
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantMrchsurplmorderPreconsultModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'merchant_exts' in d:
            o.merchant_exts = d['merchant_exts']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


