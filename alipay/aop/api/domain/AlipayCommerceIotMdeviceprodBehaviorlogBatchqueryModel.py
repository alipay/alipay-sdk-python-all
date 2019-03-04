#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotMdeviceprodBehaviorlogBatchqueryModel(object):

    def __init__(self):
        self._behavior_type = None
        self._device_sn = None
        self._imei = None
        self._item_id = None

    @property
    def behavior_type(self):
        return self._behavior_type

    @behavior_type.setter
    def behavior_type(self, value):
        self._behavior_type = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.behavior_type:
            if hasattr(self.behavior_type, 'to_alipay_dict'):
                params['behavior_type'] = self.behavior_type.to_alipay_dict()
            else:
                params['behavior_type'] = self.behavior_type
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotMdeviceprodBehaviorlogBatchqueryModel()
        if 'behavior_type' in d:
            o.behavior_type = d['behavior_type']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'imei' in d:
            o.imei = d['imei']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


