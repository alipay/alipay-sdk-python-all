#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosCategoryDeleteModel(object):

    def __init__(self):
        self._cate_id = None
        self._shop_id = None

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_id:
            if hasattr(self.cate_id, 'to_alipay_dict'):
                params['cate_id'] = self.cate_id.to_alipay_dict()
            else:
                params['cate_id'] = self.cate_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosCategoryDeleteModel()
        if 'cate_id' in d:
            o.cate_id = d['cate_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


