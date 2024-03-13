#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BrandRankDTO(object):

    def __init__(self):
        self._brand_name = None
        self._rank = None
        self._trd_amt_index = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def trd_amt_index(self):
        return self._trd_amt_index

    @trd_amt_index.setter
    def trd_amt_index(self, value):
        self._trd_amt_index = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.trd_amt_index:
            if hasattr(self.trd_amt_index, 'to_alipay_dict'):
                params['trd_amt_index'] = self.trd_amt_index.to_alipay_dict()
            else:
                params['trd_amt_index'] = self.trd_amt_index
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandRankDTO()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'rank' in d:
            o.rank = d['rank']
        if 'trd_amt_index' in d:
            o.trd_amt_index = d['trd_amt_index']
        return o


