#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommissionRuleQueryModel(object):

    def __init__(self):
        self._ant_shop_id = None

    @property
    def ant_shop_id(self):
        return self._ant_shop_id

    @ant_shop_id.setter
    def ant_shop_id(self, value):
        self._ant_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_shop_id:
            if hasattr(self.ant_shop_id, 'to_alipay_dict'):
                params['ant_shop_id'] = self.ant_shop_id.to_alipay_dict()
            else:
                params['ant_shop_id'] = self.ant_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommissionRuleQueryModel()
        if 'ant_shop_id' in d:
            o.ant_shop_id = d['ant_shop_id']
        return o


