#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DigitalShopInfo(object):

    def __init__(self):
        self._digital_shop_address = None
        self._digital_shop_id = None
        self._digital_shop_name = None

    @property
    def digital_shop_address(self):
        return self._digital_shop_address

    @digital_shop_address.setter
    def digital_shop_address(self, value):
        self._digital_shop_address = value
    @property
    def digital_shop_id(self):
        return self._digital_shop_id

    @digital_shop_id.setter
    def digital_shop_id(self, value):
        self._digital_shop_id = value
    @property
    def digital_shop_name(self):
        return self._digital_shop_name

    @digital_shop_name.setter
    def digital_shop_name(self, value):
        self._digital_shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.digital_shop_address:
            if hasattr(self.digital_shop_address, 'to_alipay_dict'):
                params['digital_shop_address'] = self.digital_shop_address.to_alipay_dict()
            else:
                params['digital_shop_address'] = self.digital_shop_address
        if self.digital_shop_id:
            if hasattr(self.digital_shop_id, 'to_alipay_dict'):
                params['digital_shop_id'] = self.digital_shop_id.to_alipay_dict()
            else:
                params['digital_shop_id'] = self.digital_shop_id
        if self.digital_shop_name:
            if hasattr(self.digital_shop_name, 'to_alipay_dict'):
                params['digital_shop_name'] = self.digital_shop_name.to_alipay_dict()
            else:
                params['digital_shop_name'] = self.digital_shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DigitalShopInfo()
        if 'digital_shop_address' in d:
            o.digital_shop_address = d['digital_shop_address']
        if 'digital_shop_id' in d:
            o.digital_shop_id = d['digital_shop_id']
        if 'digital_shop_name' in d:
            o.digital_shop_name = d['digital_shop_name']
        return o


