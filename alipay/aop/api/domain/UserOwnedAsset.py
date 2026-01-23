#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserOwnedAsset(object):

    def __init__(self):
        self._owned_sku_asset_num = None
        self._sku_id = None
        self._sku_name = None

    @property
    def owned_sku_asset_num(self):
        return self._owned_sku_asset_num

    @owned_sku_asset_num.setter
    def owned_sku_asset_num(self, value):
        self._owned_sku_asset_num = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.owned_sku_asset_num:
            if hasattr(self.owned_sku_asset_num, 'to_alipay_dict'):
                params['owned_sku_asset_num'] = self.owned_sku_asset_num.to_alipay_dict()
            else:
                params['owned_sku_asset_num'] = self.owned_sku_asset_num
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserOwnedAsset()
        if 'owned_sku_asset_num' in d:
            o.owned_sku_asset_num = d['owned_sku_asset_num']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        return o


