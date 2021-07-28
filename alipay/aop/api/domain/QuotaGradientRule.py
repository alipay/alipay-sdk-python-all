#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QuotaGradientRule(object):

    def __init__(self):
        self._score_400 = None
        self._score_450 = None
        self._score_500 = None
        self._score_550 = None
        self._score_600 = None
        self._score_650 = None
        self._score_700 = None
        self._score_750 = None
        self._score_800 = None
        self._score_850 = None
        self._score_900 = None
        self._score_950 = None

    @property
    def score_400(self):
        return self._score_400

    @score_400.setter
    def score_400(self, value):
        self._score_400 = value
    @property
    def score_450(self):
        return self._score_450

    @score_450.setter
    def score_450(self, value):
        self._score_450 = value
    @property
    def score_500(self):
        return self._score_500

    @score_500.setter
    def score_500(self, value):
        self._score_500 = value
    @property
    def score_550(self):
        return self._score_550

    @score_550.setter
    def score_550(self, value):
        self._score_550 = value
    @property
    def score_600(self):
        return self._score_600

    @score_600.setter
    def score_600(self, value):
        self._score_600 = value
    @property
    def score_650(self):
        return self._score_650

    @score_650.setter
    def score_650(self, value):
        self._score_650 = value
    @property
    def score_700(self):
        return self._score_700

    @score_700.setter
    def score_700(self, value):
        self._score_700 = value
    @property
    def score_750(self):
        return self._score_750

    @score_750.setter
    def score_750(self, value):
        self._score_750 = value
    @property
    def score_800(self):
        return self._score_800

    @score_800.setter
    def score_800(self, value):
        self._score_800 = value
    @property
    def score_850(self):
        return self._score_850

    @score_850.setter
    def score_850(self, value):
        self._score_850 = value
    @property
    def score_900(self):
        return self._score_900

    @score_900.setter
    def score_900(self, value):
        self._score_900 = value
    @property
    def score_950(self):
        return self._score_950

    @score_950.setter
    def score_950(self, value):
        self._score_950 = value


    def to_alipay_dict(self):
        params = dict()
        if self.score_400:
            if hasattr(self.score_400, 'to_alipay_dict'):
                params['score_400'] = self.score_400.to_alipay_dict()
            else:
                params['score_400'] = self.score_400
        if self.score_450:
            if hasattr(self.score_450, 'to_alipay_dict'):
                params['score_450'] = self.score_450.to_alipay_dict()
            else:
                params['score_450'] = self.score_450
        if self.score_500:
            if hasattr(self.score_500, 'to_alipay_dict'):
                params['score_500'] = self.score_500.to_alipay_dict()
            else:
                params['score_500'] = self.score_500
        if self.score_550:
            if hasattr(self.score_550, 'to_alipay_dict'):
                params['score_550'] = self.score_550.to_alipay_dict()
            else:
                params['score_550'] = self.score_550
        if self.score_600:
            if hasattr(self.score_600, 'to_alipay_dict'):
                params['score_600'] = self.score_600.to_alipay_dict()
            else:
                params['score_600'] = self.score_600
        if self.score_650:
            if hasattr(self.score_650, 'to_alipay_dict'):
                params['score_650'] = self.score_650.to_alipay_dict()
            else:
                params['score_650'] = self.score_650
        if self.score_700:
            if hasattr(self.score_700, 'to_alipay_dict'):
                params['score_700'] = self.score_700.to_alipay_dict()
            else:
                params['score_700'] = self.score_700
        if self.score_750:
            if hasattr(self.score_750, 'to_alipay_dict'):
                params['score_750'] = self.score_750.to_alipay_dict()
            else:
                params['score_750'] = self.score_750
        if self.score_800:
            if hasattr(self.score_800, 'to_alipay_dict'):
                params['score_800'] = self.score_800.to_alipay_dict()
            else:
                params['score_800'] = self.score_800
        if self.score_850:
            if hasattr(self.score_850, 'to_alipay_dict'):
                params['score_850'] = self.score_850.to_alipay_dict()
            else:
                params['score_850'] = self.score_850
        if self.score_900:
            if hasattr(self.score_900, 'to_alipay_dict'):
                params['score_900'] = self.score_900.to_alipay_dict()
            else:
                params['score_900'] = self.score_900
        if self.score_950:
            if hasattr(self.score_950, 'to_alipay_dict'):
                params['score_950'] = self.score_950.to_alipay_dict()
            else:
                params['score_950'] = self.score_950
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuotaGradientRule()
        if 'score_400' in d:
            o.score_400 = d['score_400']
        if 'score_450' in d:
            o.score_450 = d['score_450']
        if 'score_500' in d:
            o.score_500 = d['score_500']
        if 'score_550' in d:
            o.score_550 = d['score_550']
        if 'score_600' in d:
            o.score_600 = d['score_600']
        if 'score_650' in d:
            o.score_650 = d['score_650']
        if 'score_700' in d:
            o.score_700 = d['score_700']
        if 'score_750' in d:
            o.score_750 = d['score_750']
        if 'score_800' in d:
            o.score_800 = d['score_800']
        if 'score_850' in d:
            o.score_850 = d['score_850']
        if 'score_900' in d:
            o.score_900 = d['score_900']
        if 'score_950' in d:
            o.score_950 = d['score_950']
        return o


