#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignPrizeAmountQueryModel(object):

    def __init__(self):
        self._camp_id = None
        self._prize_id = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignPrizeAmountQueryModel()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        return o


