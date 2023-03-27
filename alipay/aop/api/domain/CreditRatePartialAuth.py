#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditRatePartialAuth(object):

    def __init__(self):
        self._cr_max_rank = None
        self._cr_min_rank = None

    @property
    def cr_max_rank(self):
        return self._cr_max_rank

    @cr_max_rank.setter
    def cr_max_rank(self, value):
        self._cr_max_rank = value
    @property
    def cr_min_rank(self):
        return self._cr_min_rank

    @cr_min_rank.setter
    def cr_min_rank(self, value):
        self._cr_min_rank = value


    def to_alipay_dict(self):
        params = dict()
        if self.cr_max_rank:
            if hasattr(self.cr_max_rank, 'to_alipay_dict'):
                params['cr_max_rank'] = self.cr_max_rank.to_alipay_dict()
            else:
                params['cr_max_rank'] = self.cr_max_rank
        if self.cr_min_rank:
            if hasattr(self.cr_min_rank, 'to_alipay_dict'):
                params['cr_min_rank'] = self.cr_min_rank.to_alipay_dict()
            else:
                params['cr_min_rank'] = self.cr_min_rank
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditRatePartialAuth()
        if 'cr_max_rank' in d:
            o.cr_max_rank = d['cr_max_rank']
        if 'cr_min_rank' in d:
            o.cr_min_rank = d['cr_min_rank']
        return o


