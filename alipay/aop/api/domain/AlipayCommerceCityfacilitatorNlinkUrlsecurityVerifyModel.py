#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorNlinkUrlsecurityVerifyModel(object):

    def __init__(self):
        self._device_sign = None
        self._mcu_uuid = None
        self._public_key = None
        self._se_uuid = None
        self._supplier_id = None

    @property
    def device_sign(self):
        return self._device_sign

    @device_sign.setter
    def device_sign(self, value):
        self._device_sign = value
    @property
    def mcu_uuid(self):
        return self._mcu_uuid

    @mcu_uuid.setter
    def mcu_uuid(self, value):
        self._mcu_uuid = value
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
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sign:
            if hasattr(self.device_sign, 'to_alipay_dict'):
                params['device_sign'] = self.device_sign.to_alipay_dict()
            else:
                params['device_sign'] = self.device_sign
        if self.mcu_uuid:
            if hasattr(self.mcu_uuid, 'to_alipay_dict'):
                params['mcu_uuid'] = self.mcu_uuid.to_alipay_dict()
            else:
                params['mcu_uuid'] = self.mcu_uuid
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
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorNlinkUrlsecurityVerifyModel()
        if 'device_sign' in d:
            o.device_sign = d['device_sign']
        if 'mcu_uuid' in d:
            o.mcu_uuid = d['mcu_uuid']
        if 'public_key' in d:
            o.public_key = d['public_key']
        if 'se_uuid' in d:
            o.se_uuid = d['se_uuid']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


