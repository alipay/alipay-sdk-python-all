#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitOrderInfo import BenefitOrderInfo


class BenefitLuckDrawInfo(object):

    def __init__(self):
        self._can_luck_draw = None
        self._has_luck_draw = None
        self._order_info = None

    @property
    def can_luck_draw(self):
        return self._can_luck_draw

    @can_luck_draw.setter
    def can_luck_draw(self, value):
        self._can_luck_draw = value
    @property
    def has_luck_draw(self):
        return self._has_luck_draw

    @has_luck_draw.setter
    def has_luck_draw(self, value):
        self._has_luck_draw = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        if isinstance(value, BenefitOrderInfo):
            self._order_info = value
        else:
            self._order_info = BenefitOrderInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.can_luck_draw:
            if hasattr(self.can_luck_draw, 'to_alipay_dict'):
                params['can_luck_draw'] = self.can_luck_draw.to_alipay_dict()
            else:
                params['can_luck_draw'] = self.can_luck_draw
        if self.has_luck_draw:
            if hasattr(self.has_luck_draw, 'to_alipay_dict'):
                params['has_luck_draw'] = self.has_luck_draw.to_alipay_dict()
            else:
                params['has_luck_draw'] = self.has_luck_draw
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitLuckDrawInfo()
        if 'can_luck_draw' in d:
            o.can_luck_draw = d['can_luck_draw']
        if 'has_luck_draw' in d:
            o.has_luck_draw = d['has_luck_draw']
        if 'order_info' in d:
            o.order_info = d['order_info']
        return o


