#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNopenLicenseInitializeModel(object):

    def __init__(self):
        self._device_sign = None
        self._item_id = None
        self._mcu_id = None
        self._public_key = None
        self._se_uuid = None
        self._sn = None
        self._supplier_id = None
        self._type = None

    @property
    def device_sign(self):
        return self._device_sign

    @device_sign.setter
    def device_sign(self, value):
        self._device_sign = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mcu_id(self):
        return self._mcu_id

    @mcu_id.setter
    def mcu_id(self, value):
        self._mcu_id = value
    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        self._public_key = value
    @property
    def se_uuid(self):
        return self._se_uuid

    @se_uuid.setter
    def se_uuid(self, value):
        self._se_uuid = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sign:
            if hasattr(self.device_sign, 'to_alipay_dict'):
                params['device_sign'] = self.device_sign.to_alipay_dict()
            else:
                params['device_sign'] = self.device_sign
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.mcu_id:
            if hasattr(self.mcu_id, 'to_alipay_dict'):
                params['mcu_id'] = self.mcu_id.to_alipay_dict()
            else:
                params['mcu_id'] = self.mcu_id
        if self.public_key:
            if hasattr(self.public_key, 'to_alipay_dict'):
                params['public_key'] = self.public_key.to_alipay_dict()
            else:
                params['public_key'] = self.public_key
        if self.se_uuid:
            if hasattr(self.se_uuid, 'to_alipay_dict'):
                params['se_uuid'] = self.se_uuid.to_alipay_dict()
            else:
                params['se_uuid'] = self.se_uuid
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNopenLicenseInitializeModel()
        if 'device_sign' in d:
            o.device_sign = d['device_sign']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mcu_id' in d:
            o.mcu_id = d['mcu_id']
        if 'public_key' in d:
            o.public_key = d['public_key']
        if 'se_uuid' in d:
            o.se_uuid = d['se_uuid']
        if 'sn' in d:
            o.sn = d['sn']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'type' in d:
            o.type = d['type']
        return o


