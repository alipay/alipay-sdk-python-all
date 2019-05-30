#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMdeviceprodTradeBatchqueryModel(object):

    def __init__(self):
        self._device_sn = None
        self._item_id = None
        self._supplier_sn = None
        self._trade_no = None

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
    def supplier_sn(self):
        return self._supplier_sn

    @supplier_sn.setter
    def supplier_sn(self, value):
        self._supplier_sn = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.supplier_sn:
            if hasattr(self.supplier_sn, 'to_alipay_dict'):
                params['supplier_sn'] = self.supplier_sn.to_alipay_dict()
            else:
                params['supplier_sn'] = self.supplier_sn
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMdeviceprodTradeBatchqueryModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'supplier_sn' in d:
            o.supplier_sn = d['supplier_sn']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


