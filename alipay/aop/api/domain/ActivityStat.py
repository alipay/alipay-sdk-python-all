#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityStat(object):

    def __init__(self):
        self._contract_count = None
        self._finished_count = None
        self._lose_efficacy_count = None
        self._participator_count = None
        self._promising_count = None
        self._trade_count = None
        self._violated_count = None

    @property
    def contract_count(self):
        return self._contract_count

    @contract_count.setter
    def contract_count(self, value):
        self._contract_count = value
    @property
    def finished_count(self):
        return self._finished_count

    @finished_count.setter
    def finished_count(self, value):
        self._finished_count = value
    @property
    def lose_efficacy_count(self):
        return self._lose_efficacy_count

    @lose_efficacy_count.setter
    def lose_efficacy_count(self, value):
        self._lose_efficacy_count = value
    @property
    def participator_count(self):
        return self._participator_count

    @participator_count.setter
    def participator_count(self, value):
        self._participator_count = value
    @property
    def promising_count(self):
        return self._promising_count

    @promising_count.setter
    def promising_count(self, value):
        self._promising_count = value
    @property
    def trade_count(self):
        return self._trade_count

    @trade_count.setter
    def trade_count(self, value):
        self._trade_count = value
    @property
    def violated_count(self):
        return self._violated_count

    @violated_count.setter
    def violated_count(self, value):
        self._violated_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_count:
            if hasattr(self.contract_count, 'to_alipay_dict'):
                params['contract_count'] = self.contract_count.to_alipay_dict()
            else:
                params['contract_count'] = self.contract_count
        if self.finished_count:
            if hasattr(self.finished_count, 'to_alipay_dict'):
                params['finished_count'] = self.finished_count.to_alipay_dict()
            else:
                params['finished_count'] = self.finished_count
        if self.lose_efficacy_count:
            if hasattr(self.lose_efficacy_count, 'to_alipay_dict'):
                params['lose_efficacy_count'] = self.lose_efficacy_count.to_alipay_dict()
            else:
                params['lose_efficacy_count'] = self.lose_efficacy_count
        if self.participator_count:
            if hasattr(self.participator_count, 'to_alipay_dict'):
                params['participator_count'] = self.participator_count.to_alipay_dict()
            else:
                params['participator_count'] = self.participator_count
        if self.promising_count:
            if hasattr(self.promising_count, 'to_alipay_dict'):
                params['promising_count'] = self.promising_count.to_alipay_dict()
            else:
                params['promising_count'] = self.promising_count
        if self.trade_count:
            if hasattr(self.trade_count, 'to_alipay_dict'):
                params['trade_count'] = self.trade_count.to_alipay_dict()
            else:
                params['trade_count'] = self.trade_count
        if self.violated_count:
            if hasattr(self.violated_count, 'to_alipay_dict'):
                params['violated_count'] = self.violated_count.to_alipay_dict()
            else:
                params['violated_count'] = self.violated_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityStat()
        if 'contract_count' in d:
            o.contract_count = d['contract_count']
        if 'finished_count' in d:
            o.finished_count = d['finished_count']
        if 'lose_efficacy_count' in d:
            o.lose_efficacy_count = d['lose_efficacy_count']
        if 'participator_count' in d:
            o.participator_count = d['participator_count']
        if 'promising_count' in d:
            o.promising_count = d['promising_count']
        if 'trade_count' in d:
            o.trade_count = d['trade_count']
        if 'violated_count' in d:
            o.violated_count = d['violated_count']
        return o


