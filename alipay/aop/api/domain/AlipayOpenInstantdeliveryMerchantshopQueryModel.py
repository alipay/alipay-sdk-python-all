#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenInstantdeliveryMerchantshopQueryModel(object):

    def __init__(self):
        self._shop_no = None

    @property
    def shop_no(self):
        return self._shop_no

    @shop_no.setter
    def shop_no(self, value):
        self._shop_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_no:
            if hasattr(self.shop_no, 'to_alipay_dict'):
                params['shop_no'] = self.shop_no.to_alipay_dict()
            else:
                params['shop_no'] = self.shop_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenInstantdeliveryMerchantshopQueryModel()
        if 'shop_no' in d:
            o.shop_no = d['shop_no']
        return o


