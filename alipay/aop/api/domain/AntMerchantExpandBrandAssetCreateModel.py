#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandBrandAssetCreateModel(object):

    def __init__(self):
        self._asset_ids = None
        self._asset_type = None
        self._brand_id = None
        self._carrier_id = None

    @property
    def asset_ids(self):
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, value):
        if isinstance(value, list):
            self._asset_ids = list()
            for i in value:
                self._asset_ids.append(i)
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def carrier_id(self):
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, value):
        self._carrier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_ids:
            if isinstance(self.asset_ids, list):
                for i in range(0, len(self.asset_ids)):
                    element = self.asset_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_ids[i] = element.to_alipay_dict()
            if hasattr(self.asset_ids, 'to_alipay_dict'):
                params['asset_ids'] = self.asset_ids.to_alipay_dict()
            else:
                params['asset_ids'] = self.asset_ids
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.carrier_id:
            if hasattr(self.carrier_id, 'to_alipay_dict'):
                params['carrier_id'] = self.carrier_id.to_alipay_dict()
            else:
                params['carrier_id'] = self.carrier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandBrandAssetCreateModel()
        if 'asset_ids' in d:
            o.asset_ids = d['asset_ids']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'carrier_id' in d:
            o.carrier_id = d['carrier_id']
        return o


