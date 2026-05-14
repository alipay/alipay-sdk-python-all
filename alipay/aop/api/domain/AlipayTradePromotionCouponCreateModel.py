#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromotionCoupon import PromotionCoupon


class AlipayTradePromotionCouponCreateModel(object):

    def __init__(self):
        self._request_info = None

    @property
    def request_info(self):
        return self._request_info

    @request_info.setter
    def request_info(self, value):
        if isinstance(value, PromotionCoupon):
            self._request_info = value
        else:
            self._request_info = PromotionCoupon.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.request_info:
            if hasattr(self.request_info, 'to_alipay_dict'):
                params['request_info'] = self.request_info.to_alipay_dict()
            else:
                params['request_info'] = self.request_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePromotionCouponCreateModel()
        if 'request_info' in d:
            o.request_info = d['request_info']
        return o


