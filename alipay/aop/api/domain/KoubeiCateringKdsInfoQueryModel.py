#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringKdsInfoQueryModel(object):

    def __init__(self):
        self._kds_id = None
        self._shop_id = None

    @property
    def kds_id(self):
        return self._kds_id

    @kds_id.setter
    def kds_id(self, value):
        self._kds_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.kds_id:
            if hasattr(self.kds_id, 'to_alipay_dict'):
                params['kds_id'] = self.kds_id.to_alipay_dict()
            else:
                params['kds_id'] = self.kds_id
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
        o = KoubeiCateringKdsInfoQueryModel()
        if 'kds_id' in d:
            o.kds_id = d['kds_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


