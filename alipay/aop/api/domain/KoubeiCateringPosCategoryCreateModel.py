#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosCategoryCreateModel(object):

    def __init__(self):
        self._cate_name = None
        self._creator = None
        self._shop_id = None

    @property
    def cate_name(self):
        return self._cate_name

    @cate_name.setter
    def cate_name(self, value):
        self._cate_name = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_name:
            if hasattr(self.cate_name, 'to_alipay_dict'):
                params['cate_name'] = self.cate_name.to_alipay_dict()
            else:
                params['cate_name'] = self.cate_name
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
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
        o = KoubeiCateringPosCategoryCreateModel()
        if 'cate_name' in d:
            o.cate_name = d['cate_name']
        if 'creator' in d:
            o.creator = d['creator']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


