#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantShopAddress import MerchantShopAddress
from alipay.aop.api.domain.AlipayMerchantInfo import AlipayMerchantInfo


class IsvMerchantShop(object):

    def __init__(self):
        self._address = None
        self._device_type = None
        self._merchant_info = None
        self._merchant_phone = None
        self._out_shop_id = None
        self._out_shop_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, MerchantShopAddress):
            self._address = value
        else:
            self._address = MerchantShopAddress.from_alipay_dict(value)
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, AlipayMerchantInfo):
            self._merchant_info = value
        else:
            self._merchant_info = AlipayMerchantInfo.from_alipay_dict(value)
    @property
    def merchant_phone(self):
        return self._merchant_phone

    @merchant_phone.setter
    def merchant_phone(self, value):
        self._merchant_phone = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def out_shop_name(self):
        return self._out_shop_name

    @out_shop_name.setter
    def out_shop_name(self, value):
        self._out_shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.merchant_phone:
            if hasattr(self.merchant_phone, 'to_alipay_dict'):
                params['merchant_phone'] = self.merchant_phone.to_alipay_dict()
            else:
                params['merchant_phone'] = self.merchant_phone
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.out_shop_name:
            if hasattr(self.out_shop_name, 'to_alipay_dict'):
                params['out_shop_name'] = self.out_shop_name.to_alipay_dict()
            else:
                params['out_shop_name'] = self.out_shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvMerchantShop()
        if 'address' in d:
            o.address = d['address']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'merchant_phone' in d:
            o.merchant_phone = d['merchant_phone']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'out_shop_name' in d:
            o.out_shop_name = d['out_shop_name']
        return o


