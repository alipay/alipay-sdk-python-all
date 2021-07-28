#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetDeviceRelation(object):

    def __init__(self):
        self._asset_id = None
        self._device_ids = None
        self._device_supply_code = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def device_ids(self):
        return self._device_ids

    @device_ids.setter
    def device_ids(self, value):
        if isinstance(value, list):
            self._device_ids = list()
            for i in value:
                self._device_ids.append(i)
    @property
    def device_supply_code(self):
        return self._device_supply_code

    @device_supply_code.setter
    def device_supply_code(self, value):
        self._device_supply_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.device_ids:
            if isinstance(self.device_ids, list):
                for i in range(0, len(self.device_ids)):
                    element = self.device_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_ids[i] = element.to_alipay_dict()
            if hasattr(self.device_ids, 'to_alipay_dict'):
                params['device_ids'] = self.device_ids.to_alipay_dict()
            else:
                params['device_ids'] = self.device_ids
        if self.device_supply_code:
            if hasattr(self.device_supply_code, 'to_alipay_dict'):
                params['device_supply_code'] = self.device_supply_code.to_alipay_dict()
            else:
                params['device_supply_code'] = self.device_supply_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetDeviceRelation()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'device_ids' in d:
            o.device_ids = d['device_ids']
        if 'device_supply_code' in d:
            o.device_supply_code = d['device_supply_code']
        return o


