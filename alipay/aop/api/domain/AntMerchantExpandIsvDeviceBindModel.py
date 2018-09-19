#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIsvDeviceBindModel(object):

    def __init__(self):
        self._biz_type = None
        self._device_sn = None
        self._item_id = None
        self._memo = None
        self._order_no = None
        self._shop_id = None
        self._supplier_no = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def supplier_no(self):
        return self._supplier_no

    @supplier_no.setter
    def supplier_no(self, value):
        self._supplier_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.supplier_no:
            if hasattr(self.supplier_no, 'to_alipay_dict'):
                params['supplier_no'] = self.supplier_no.to_alipay_dict()
            else:
                params['supplier_no'] = self.supplier_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIsvDeviceBindModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'supplier_no' in d:
            o.supplier_no = d['supplier_no']
        return o


