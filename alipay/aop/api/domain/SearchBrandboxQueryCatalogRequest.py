#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SearchBrandboxQueryCatalogRequest(object):

    def __init__(self):
        self._brand_id = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchBrandboxQueryCatalogRequest()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        return o


