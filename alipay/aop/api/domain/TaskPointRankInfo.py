#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskPointRankInfo(object):

    def __init__(self):
        self._difference = None
        self._rank = None
        self._total = None
        self._type = None

    @property
    def difference(self):
        return self._difference

    @difference.setter
    def difference(self, value):
        self._difference = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.difference:
            if hasattr(self.difference, 'to_alipay_dict'):
                params['difference'] = self.difference.to_alipay_dict()
            else:
                params['difference'] = self.difference
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskPointRankInfo()
        if 'difference' in d:
            o.difference = d['difference']
        if 'rank' in d:
            o.rank = d['rank']
        if 'total' in d:
            o.total = d['total']
        if 'type' in d:
            o.type = d['type']
        return o


