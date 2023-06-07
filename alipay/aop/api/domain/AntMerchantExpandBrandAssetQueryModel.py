#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandBrandAssetQueryModel(object):

    def __init__(self):
        self._asset_type = None
        self._brand_id = None
        self._carrier_id = None
        self._confirm = None
        self._page_number = None
        self._page_size = None

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
    @property
    def confirm(self):
        return self._confirm

    @confirm.setter
    def confirm(self, value):
        self._confirm = value
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.confirm:
            if hasattr(self.confirm, 'to_alipay_dict'):
                params['confirm'] = self.confirm.to_alipay_dict()
            else:
                params['confirm'] = self.confirm
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandBrandAssetQueryModel()
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'carrier_id' in d:
            o.carrier_id = d['carrier_id']
        if 'confirm' in d:
            o.confirm = d['confirm']
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


