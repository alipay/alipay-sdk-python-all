#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceAssetDevicelistQueryModel(object):

    def __init__(self):
        self._asset_owner = None
        self._device_id = None
        self._device_supply_type = None

    @property
    def asset_owner(self):
        return self._asset_owner

    @asset_owner.setter
    def asset_owner(self, value):
        self._asset_owner = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_supply_type(self):
        return self._device_supply_type

    @device_supply_type.setter
    def device_supply_type(self, value):
        self._device_supply_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_owner:
            if hasattr(self.asset_owner, 'to_alipay_dict'):
                params['asset_owner'] = self.asset_owner.to_alipay_dict()
            else:
                params['asset_owner'] = self.asset_owner
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_supply_type:
            if hasattr(self.device_supply_type, 'to_alipay_dict'):
                params['device_supply_type'] = self.device_supply_type.to_alipay_dict()
            else:
                params['device_supply_type'] = self.device_supply_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceAssetDevicelistQueryModel()
        if 'asset_owner' in d:
            o.asset_owner = d['asset_owner']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_supply_type' in d:
            o.device_supply_type = d['device_supply_type']
        return o


