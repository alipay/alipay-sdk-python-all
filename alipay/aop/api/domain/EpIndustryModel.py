#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpIndustryModel(object):

    def __init__(self):
        self._industry_desc = None

    @property
    def industry_desc(self):
        return self._industry_desc

    @industry_desc.setter
    def industry_desc(self, value):
        self._industry_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_desc:
            if hasattr(self.industry_desc, 'to_alipay_dict'):
                params['industry_desc'] = self.industry_desc.to_alipay_dict()
            else:
                params['industry_desc'] = self.industry_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpIndustryModel()
        if 'industry_desc' in d:
            o.industry_desc = d['industry_desc']
        return o


