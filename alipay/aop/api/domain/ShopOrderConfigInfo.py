#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopOrderConfigInfo(object):

    def __init__(self):
        self._ext_infos = None
        self._order_entry_status = None
        self._shop_id = None
        self._store_id = None

    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def order_entry_status(self):
        return self._order_entry_status

    @order_entry_status.setter
    def order_entry_status(self, value):
        self._order_entry_status = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.order_entry_status:
            if hasattr(self.order_entry_status, 'to_alipay_dict'):
                params['order_entry_status'] = self.order_entry_status.to_alipay_dict()
            else:
                params['order_entry_status'] = self.order_entry_status
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopOrderConfigInfo()
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'order_entry_status' in d:
            o.order_entry_status = d['order_entry_status']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


