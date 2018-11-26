#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosCategoryQueryModel(object):

    def __init__(self):
        self._cate_id = None

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_id:
            if hasattr(self.cate_id, 'to_alipay_dict'):
                params['cate_id'] = self.cate_id.to_alipay_dict()
            else:
                params['cate_id'] = self.cate_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosCategoryQueryModel()
        if 'cate_id' in d:
            o.cate_id = d['cate_id']
        return o


