#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenPromoBudget import OpenPromoBudget
from alipay.aop.api.domain.OpenPromoCamp import OpenPromoCamp
from alipay.aop.api.domain.OpenPromoPrize import OpenPromoPrize


class AlipayMarketingCampaignActivityOfflineCreateModel(object):

    def __init__(self):
        self._budget = None
        self._camp = None
        self._out_biz_no = None
        self._prize = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if isinstance(value, OpenPromoBudget):
            self._budget = value
        else:
            self._budget = OpenPromoBudget.from_alipay_dict(value)
    @property
    def camp(self):
        return self._camp

    @camp.setter
    def camp(self, value):
        if isinstance(value, OpenPromoCamp):
            self._camp = value
        else:
            self._camp = OpenPromoCamp.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prize(self):
        return self._prize

    @prize.setter
    def prize(self, value):
        if isinstance(value, OpenPromoPrize):
            self._prize = value
        else:
            self._prize = OpenPromoPrize.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.camp:
            if hasattr(self.camp, 'to_alipay_dict'):
                params['camp'] = self.camp.to_alipay_dict()
            else:
                params['camp'] = self.camp
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prize:
            if hasattr(self.prize, 'to_alipay_dict'):
                params['prize'] = self.prize.to_alipay_dict()
            else:
                params['prize'] = self.prize
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignActivityOfflineCreateModel()
        if 'budget' in d:
            o.budget = d['budget']
        if 'camp' in d:
            o.camp = d['camp']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prize' in d:
            o.prize = d['prize']
        return o


