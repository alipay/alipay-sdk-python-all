#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendCard(object):

    def __init__(self):
        self._card_name = None
        self._card_recommend_reason = None
        self._card_type = None
        self._cate_1 = None
        self._cate_2 = None
        self._cate_3 = None

    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_recommend_reason(self):
        return self._card_recommend_reason

    @card_recommend_reason.setter
    def card_recommend_reason(self, value):
        self._card_recommend_reason = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def cate_1(self):
        return self._cate_1

    @cate_1.setter
    def cate_1(self, value):
        self._cate_1 = value
    @property
    def cate_2(self):
        return self._cate_2

    @cate_2.setter
    def cate_2(self, value):
        self._cate_2 = value
    @property
    def cate_3(self):
        return self._cate_3

    @cate_3.setter
    def cate_3(self, value):
        self._cate_3 = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_recommend_reason:
            if hasattr(self.card_recommend_reason, 'to_alipay_dict'):
                params['card_recommend_reason'] = self.card_recommend_reason.to_alipay_dict()
            else:
                params['card_recommend_reason'] = self.card_recommend_reason
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.cate_1:
            if hasattr(self.cate_1, 'to_alipay_dict'):
                params['cate_1'] = self.cate_1.to_alipay_dict()
            else:
                params['cate_1'] = self.cate_1
        if self.cate_2:
            if hasattr(self.cate_2, 'to_alipay_dict'):
                params['cate_2'] = self.cate_2.to_alipay_dict()
            else:
                params['cate_2'] = self.cate_2
        if self.cate_3:
            if hasattr(self.cate_3, 'to_alipay_dict'):
                params['cate_3'] = self.cate_3.to_alipay_dict()
            else:
                params['cate_3'] = self.cate_3
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecommendCard()
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_recommend_reason' in d:
            o.card_recommend_reason = d['card_recommend_reason']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'cate_1' in d:
            o.cate_1 = d['cate_1']
        if 'cate_2' in d:
            o.cate_2 = d['cate_2']
        if 'cate_3' in d:
            o.cate_3 = d['cate_3']
        return o


