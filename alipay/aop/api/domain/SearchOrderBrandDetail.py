#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BrandDetail import BrandDetail


class SearchOrderBrandDetail(object):

    def __init__(self):
        self._brand_detail = None
        self._key = None

    @property
    def brand_detail(self):
        return self._brand_detail

    @brand_detail.setter
    def brand_detail(self, value):
        if isinstance(value, BrandDetail):
            self._brand_detail = value
        else:
            self._brand_detail = BrandDetail.from_alipay_dict(value)
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_detail:
            if hasattr(self.brand_detail, 'to_alipay_dict'):
                params['brand_detail'] = self.brand_detail.to_alipay_dict()
            else:
                params['brand_detail'] = self.brand_detail
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchOrderBrandDetail()
        if 'brand_detail' in d:
            o.brand_detail = d['brand_detail']
        if 'key' in d:
            o.key = d['key']
        return o


