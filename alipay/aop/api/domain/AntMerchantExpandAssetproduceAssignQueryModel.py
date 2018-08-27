#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandAssetproduceAssignQueryModel(object):

    def __init__(self):
        self._page_size = None

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AntMerchantExpandAssetproduceAssignQueryModel()
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


