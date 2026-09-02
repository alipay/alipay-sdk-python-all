#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AutohomeDealStatusModel(object):

    def __init__(self):
        self._clue_brand_id = None
        self._deal_brand_id = None
        self._deal_series_id = None

    @property
    def clue_brand_id(self):
        return self._clue_brand_id

    @clue_brand_id.setter
    def clue_brand_id(self, value):
        self._clue_brand_id = value
    @property
    def deal_brand_id(self):
        return self._deal_brand_id

    @deal_brand_id.setter
    def deal_brand_id(self, value):
        self._deal_brand_id = value
    @property
    def deal_series_id(self):
        return self._deal_series_id

    @deal_series_id.setter
    def deal_series_id(self, value):
        self._deal_series_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.clue_brand_id:
            if hasattr(self.clue_brand_id, 'to_alipay_dict'):
                params['clue_brand_id'] = self.clue_brand_id.to_alipay_dict()
            else:
                params['clue_brand_id'] = self.clue_brand_id
        if self.deal_brand_id:
            if hasattr(self.deal_brand_id, 'to_alipay_dict'):
                params['deal_brand_id'] = self.deal_brand_id.to_alipay_dict()
            else:
                params['deal_brand_id'] = self.deal_brand_id
        if self.deal_series_id:
            if hasattr(self.deal_series_id, 'to_alipay_dict'):
                params['deal_series_id'] = self.deal_series_id.to_alipay_dict()
            else:
                params['deal_series_id'] = self.deal_series_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AutohomeDealStatusModel()
        if 'clue_brand_id' in d:
            o.clue_brand_id = d['clue_brand_id']
        if 'deal_brand_id' in d:
            o.deal_brand_id = d['deal_brand_id']
        if 'deal_series_id' in d:
            o.deal_series_id = d['deal_series_id']
        return o


