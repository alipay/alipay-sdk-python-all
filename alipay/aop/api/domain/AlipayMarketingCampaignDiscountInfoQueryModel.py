#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignDiscountInfoQueryModel(object):

    def __init__(self):
        self._discount_id = None

    @property
    def discount_id(self):
        return self._discount_id

    @discount_id.setter
    def discount_id(self, value):
        self._discount_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_id:
            if hasattr(self.discount_id, 'to_alipay_dict'):
                params['discount_id'] = self.discount_id.to_alipay_dict()
            else:
                params['discount_id'] = self.discount_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignDiscountInfoQueryModel()
        if 'discount_id' in d:
            o.discount_id = d['discount_id']
        return o


