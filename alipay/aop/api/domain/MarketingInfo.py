#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromotionDetail import PromotionDetail


class MarketingInfo(object):

    def __init__(self):
        self._promotion_list = None
        self._total_amount = None
        self._use_mode = None

    @property
    def promotion_list(self):
        return self._promotion_list

    @promotion_list.setter
    def promotion_list(self, value):
        if isinstance(value, list):
            self._promotion_list = list()
            for i in value:
                if isinstance(i, PromotionDetail):
                    self._promotion_list.append(i)
                else:
                    self._promotion_list.append(PromotionDetail.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def use_mode(self):
        return self._use_mode

    @use_mode.setter
    def use_mode(self, value):
        self._use_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.promotion_list:
            if isinstance(self.promotion_list, list):
                for i in range(0, len(self.promotion_list)):
                    element = self.promotion_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promotion_list[i] = element.to_alipay_dict()
            if hasattr(self.promotion_list, 'to_alipay_dict'):
                params['promotion_list'] = self.promotion_list.to_alipay_dict()
            else:
                params['promotion_list'] = self.promotion_list
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.use_mode:
            if hasattr(self.use_mode, 'to_alipay_dict'):
                params['use_mode'] = self.use_mode.to_alipay_dict()
            else:
                params['use_mode'] = self.use_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MarketingInfo()
        if 'promotion_list' in d:
            o.promotion_list = d['promotion_list']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'use_mode' in d:
            o.use_mode = d['use_mode']
        return o


