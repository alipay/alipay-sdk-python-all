#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsHealthGiftBatchGainSumInsuredResult(object):

    def __init__(self):
        self._admit = None
        self._biz_type = None
        self._delta_sum_insured = None
        self._product_group_biz_type = None
        self._source = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def delta_sum_insured(self):
        return self._delta_sum_insured

    @delta_sum_insured.setter
    def delta_sum_insured(self, value):
        self._delta_sum_insured = value
    @property
    def product_group_biz_type(self):
        return self._product_group_biz_type

    @product_group_biz_type.setter
    def product_group_biz_type(self, value):
        self._product_group_biz_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.admit:
            if hasattr(self.admit, 'to_alipay_dict'):
                params['admit'] = self.admit.to_alipay_dict()
            else:
                params['admit'] = self.admit
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.delta_sum_insured:
            if hasattr(self.delta_sum_insured, 'to_alipay_dict'):
                params['delta_sum_insured'] = self.delta_sum_insured.to_alipay_dict()
            else:
                params['delta_sum_insured'] = self.delta_sum_insured
        if self.product_group_biz_type:
            if hasattr(self.product_group_biz_type, 'to_alipay_dict'):
                params['product_group_biz_type'] = self.product_group_biz_type.to_alipay_dict()
            else:
                params['product_group_biz_type'] = self.product_group_biz_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsHealthGiftBatchGainSumInsuredResult()
        if 'admit' in d:
            o.admit = d['admit']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'delta_sum_insured' in d:
            o.delta_sum_insured = d['delta_sum_insured']
        if 'product_group_biz_type' in d:
            o.product_group_biz_type = d['product_group_biz_type']
        if 'source' in d:
            o.source = d['source']
        return o


