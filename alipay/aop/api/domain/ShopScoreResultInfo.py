#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopScoreResultInfo(object):

    def __init__(self):
        self._cat_sale_score = None
        self._home_user_score = None
        self._poi_sale_score = None
        self._resident_user_score = None
        self._work_user_score = None

    @property
    def cat_sale_score(self):
        return self._cat_sale_score

    @cat_sale_score.setter
    def cat_sale_score(self, value):
        self._cat_sale_score = value
    @property
    def home_user_score(self):
        return self._home_user_score

    @home_user_score.setter
    def home_user_score(self, value):
        self._home_user_score = value
    @property
    def poi_sale_score(self):
        return self._poi_sale_score

    @poi_sale_score.setter
    def poi_sale_score(self, value):
        self._poi_sale_score = value
    @property
    def resident_user_score(self):
        return self._resident_user_score

    @resident_user_score.setter
    def resident_user_score(self, value):
        self._resident_user_score = value
    @property
    def work_user_score(self):
        return self._work_user_score

    @work_user_score.setter
    def work_user_score(self, value):
        self._work_user_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.cat_sale_score:
            if hasattr(self.cat_sale_score, 'to_alipay_dict'):
                params['cat_sale_score'] = self.cat_sale_score.to_alipay_dict()
            else:
                params['cat_sale_score'] = self.cat_sale_score
        if self.home_user_score:
            if hasattr(self.home_user_score, 'to_alipay_dict'):
                params['home_user_score'] = self.home_user_score.to_alipay_dict()
            else:
                params['home_user_score'] = self.home_user_score
        if self.poi_sale_score:
            if hasattr(self.poi_sale_score, 'to_alipay_dict'):
                params['poi_sale_score'] = self.poi_sale_score.to_alipay_dict()
            else:
                params['poi_sale_score'] = self.poi_sale_score
        if self.resident_user_score:
            if hasattr(self.resident_user_score, 'to_alipay_dict'):
                params['resident_user_score'] = self.resident_user_score.to_alipay_dict()
            else:
                params['resident_user_score'] = self.resident_user_score
        if self.work_user_score:
            if hasattr(self.work_user_score, 'to_alipay_dict'):
                params['work_user_score'] = self.work_user_score.to_alipay_dict()
            else:
                params['work_user_score'] = self.work_user_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopScoreResultInfo()
        if 'cat_sale_score' in d:
            o.cat_sale_score = d['cat_sale_score']
        if 'home_user_score' in d:
            o.home_user_score = d['home_user_score']
        if 'poi_sale_score' in d:
            o.poi_sale_score = d['poi_sale_score']
        if 'resident_user_score' in d:
            o.resident_user_score = d['resident_user_score']
        if 'work_user_score' in d:
            o.work_user_score = d['work_user_score']
        return o


