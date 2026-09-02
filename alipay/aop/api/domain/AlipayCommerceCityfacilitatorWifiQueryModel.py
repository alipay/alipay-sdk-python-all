#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorWifiQueryModel(object):

    def __init__(self):
        self._page_number = None
        self._page_size = None
        self._shop_id = None
        self._wifi_name = None

    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def wifi_name(self):
        return self._wifi_name

    @wifi_name.setter
    def wifi_name(self, value):
        self._wifi_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_number:
            if hasattr(self.page_number, 'to_alipay_dict'):
                params['page_number'] = self.page_number.to_alipay_dict()
            else:
                params['page_number'] = self.page_number
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.wifi_name:
            if hasattr(self.wifi_name, 'to_alipay_dict'):
                params['wifi_name'] = self.wifi_name.to_alipay_dict()
            else:
                params['wifi_name'] = self.wifi_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorWifiQueryModel()
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'wifi_name' in d:
            o.wifi_name = d['wifi_name']
        return o


