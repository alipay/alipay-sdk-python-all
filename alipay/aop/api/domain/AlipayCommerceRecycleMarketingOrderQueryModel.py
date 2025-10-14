#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleMarketingOrderQueryModel(object):

    def __init__(self):
        self._promo_id = None

    @property
    def promo_id(self):
        return self._promo_id

    @promo_id.setter
    def promo_id(self, value):
        self._promo_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.promo_id:
            if hasattr(self.promo_id, 'to_alipay_dict'):
                params['promo_id'] = self.promo_id.to_alipay_dict()
            else:
                params['promo_id'] = self.promo_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleMarketingOrderQueryModel()
        if 'promo_id' in d:
            o.promo_id = d['promo_id']
        return o


