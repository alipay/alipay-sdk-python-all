#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeaseItemSkuDTO(object):

    def __init__(self):
        self._brand_pid = None
        self._brand_sku_id = None
        self._lease_price = None
        self._lessor_path = None
        self._lessor_pid = None
        self._lessor_sku_id = None
        self._sku_id = None

    @property
    def brand_pid(self):
        return self._brand_pid

    @brand_pid.setter
    def brand_pid(self, value):
        self._brand_pid = value
    @property
    def brand_sku_id(self):
        return self._brand_sku_id

    @brand_sku_id.setter
    def brand_sku_id(self, value):
        self._brand_sku_id = value
    @property
    def lease_price(self):
        return self._lease_price

    @lease_price.setter
    def lease_price(self, value):
        self._lease_price = value
    @property
    def lessor_path(self):
        return self._lessor_path

    @lessor_path.setter
    def lessor_path(self, value):
        self._lessor_path = value
    @property
    def lessor_pid(self):
        return self._lessor_pid

    @lessor_pid.setter
    def lessor_pid(self, value):
        self._lessor_pid = value
    @property
    def lessor_sku_id(self):
        return self._lessor_sku_id

    @lessor_sku_id.setter
    def lessor_sku_id(self, value):
        self._lessor_sku_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_pid:
            if hasattr(self.brand_pid, 'to_alipay_dict'):
                params['brand_pid'] = self.brand_pid.to_alipay_dict()
            else:
                params['brand_pid'] = self.brand_pid
        if self.brand_sku_id:
            if hasattr(self.brand_sku_id, 'to_alipay_dict'):
                params['brand_sku_id'] = self.brand_sku_id.to_alipay_dict()
            else:
                params['brand_sku_id'] = self.brand_sku_id
        if self.lease_price:
            if hasattr(self.lease_price, 'to_alipay_dict'):
                params['lease_price'] = self.lease_price.to_alipay_dict()
            else:
                params['lease_price'] = self.lease_price
        if self.lessor_path:
            if hasattr(self.lessor_path, 'to_alipay_dict'):
                params['lessor_path'] = self.lessor_path.to_alipay_dict()
            else:
                params['lessor_path'] = self.lessor_path
        if self.lessor_pid:
            if hasattr(self.lessor_pid, 'to_alipay_dict'):
                params['lessor_pid'] = self.lessor_pid.to_alipay_dict()
            else:
                params['lessor_pid'] = self.lessor_pid
        if self.lessor_sku_id:
            if hasattr(self.lessor_sku_id, 'to_alipay_dict'):
                params['lessor_sku_id'] = self.lessor_sku_id.to_alipay_dict()
            else:
                params['lessor_sku_id'] = self.lessor_sku_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LeaseItemSkuDTO()
        if 'brand_pid' in d:
            o.brand_pid = d['brand_pid']
        if 'brand_sku_id' in d:
            o.brand_sku_id = d['brand_sku_id']
        if 'lease_price' in d:
            o.lease_price = d['lease_price']
        if 'lessor_path' in d:
            o.lessor_path = d['lessor_path']
        if 'lessor_pid' in d:
            o.lessor_pid = d['lessor_pid']
        if 'lessor_sku_id' in d:
            o.lessor_sku_id = d['lessor_sku_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


