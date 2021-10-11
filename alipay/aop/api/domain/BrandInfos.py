#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchBrandBoxInfo import SearchBrandBoxInfo


class BrandInfos(object):

    def __init__(self):
        self._box_exclusive_info = None
        self._brand_id = None
        self._brand_name = None

    @property
    def box_exclusive_info(self):
        return self._box_exclusive_info

    @box_exclusive_info.setter
    def box_exclusive_info(self, value):
        if isinstance(value, SearchBrandBoxInfo):
            self._box_exclusive_info = value
        else:
            self._box_exclusive_info = SearchBrandBoxInfo.from_alipay_dict(value)
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.box_exclusive_info:
            if hasattr(self.box_exclusive_info, 'to_alipay_dict'):
                params['box_exclusive_info'] = self.box_exclusive_info.to_alipay_dict()
            else:
                params['box_exclusive_info'] = self.box_exclusive_info
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandInfos()
        if 'box_exclusive_info' in d:
            o.box_exclusive_info = d['box_exclusive_info']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        return o


