#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppProdmodeDropdataQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._search_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def search_type(self):
        return self._search_type

    @search_type.setter
    def search_type(self, value):
        self._search_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.search_type:
            if hasattr(self.search_type, 'to_alipay_dict'):
                params['search_type'] = self.search_type.to_alipay_dict()
            else:
                params['search_type'] = self.search_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppProdmodeDropdataQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'search_type' in d:
            o.search_type = d['search_type']
        return o


