#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditRateNoAuth(object):

    def __init__(self):
        self._cr_rank_title = None

    @property
    def cr_rank_title(self):
        return self._cr_rank_title

    @cr_rank_title.setter
    def cr_rank_title(self, value):
        self._cr_rank_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.cr_rank_title:
            if hasattr(self.cr_rank_title, 'to_alipay_dict'):
                params['cr_rank_title'] = self.cr_rank_title.to_alipay_dict()
            else:
                params['cr_rank_title'] = self.cr_rank_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditRateNoAuth()
        if 'cr_rank_title' in d:
            o.cr_rank_title = d['cr_rank_title']
        return o


