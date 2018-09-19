#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignDetailInfoQueryModel(object):

    def __init__(self):
        self._camp_id = None
        self._shop_limit_count = None

    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def shop_limit_count(self):
        return self._shop_limit_count

    @shop_limit_count.setter
    def shop_limit_count(self, value):
        self._shop_limit_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.shop_limit_count:
            if hasattr(self.shop_limit_count, 'to_alipay_dict'):
                params['shop_limit_count'] = self.shop_limit_count.to_alipay_dict()
            else:
                params['shop_limit_count'] = self.shop_limit_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignDetailInfoQueryModel()
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'shop_limit_count' in d:
            o.shop_limit_count = d['shop_limit_count']
        return o


