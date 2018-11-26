#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceMerchantInfo(object):

    def __init__(self):
        self._area_code = None
        self._brand_code = None
        self._device_mac = None
        self._device_num = None
        self._geo = None
        self._group = None
        self._merchant_id = None
        self._partner_id = None
        self._store_code = None
        self._wifimac = None
        self._wifiname = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def brand_code(self):
        return self._brand_code

    @brand_code.setter
    def brand_code(self, value):
        self._brand_code = value
    @property
    def device_mac(self):
        return self._device_mac

    @device_mac.setter
    def device_mac(self, value):
        self._device_mac = value
    @property
    def device_num(self):
        return self._device_num

    @device_num.setter
    def device_num(self, value):
        self._device_num = value
    @property
    def geo(self):
        return self._geo

    @geo.setter
    def geo(self, value):
        self._geo = value
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value
    @property
    def wifimac(self):
        return self._wifimac

    @wifimac.setter
    def wifimac(self, value):
        self._wifimac = value
    @property
    def wifiname(self):
        return self._wifiname

    @wifiname.setter
    def wifiname(self, value):
        self._wifiname = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.brand_code:
            if hasattr(self.brand_code, 'to_alipay_dict'):
                params['brand_code'] = self.brand_code.to_alipay_dict()
            else:
                params['brand_code'] = self.brand_code
        if self.device_mac:
            if hasattr(self.device_mac, 'to_alipay_dict'):
                params['device_mac'] = self.device_mac.to_alipay_dict()
            else:
                params['device_mac'] = self.device_mac
        if self.device_num:
            if hasattr(self.device_num, 'to_alipay_dict'):
                params['device_num'] = self.device_num.to_alipay_dict()
            else:
                params['device_num'] = self.device_num
        if self.geo:
            if hasattr(self.geo, 'to_alipay_dict'):
                params['geo'] = self.geo.to_alipay_dict()
            else:
                params['geo'] = self.geo
        if self.group:
            if hasattr(self.group, 'to_alipay_dict'):
                params['group'] = self.group.to_alipay_dict()
            else:
                params['group'] = self.group
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        if self.wifimac:
            if hasattr(self.wifimac, 'to_alipay_dict'):
                params['wifimac'] = self.wifimac.to_alipay_dict()
            else:
                params['wifimac'] = self.wifimac
        if self.wifiname:
            if hasattr(self.wifiname, 'to_alipay_dict'):
                params['wifiname'] = self.wifiname.to_alipay_dict()
            else:
                params['wifiname'] = self.wifiname
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceMerchantInfo()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'brand_code' in d:
            o.brand_code = d['brand_code']
        if 'device_mac' in d:
            o.device_mac = d['device_mac']
        if 'device_num' in d:
            o.device_num = d['device_num']
        if 'geo' in d:
            o.geo = d['geo']
        if 'group' in d:
            o.group = d['group']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'store_code' in d:
            o.store_code = d['store_code']
        if 'wifimac' in d:
            o.wifimac = d['wifimac']
        if 'wifiname' in d:
            o.wifiname = d['wifiname']
        return o


