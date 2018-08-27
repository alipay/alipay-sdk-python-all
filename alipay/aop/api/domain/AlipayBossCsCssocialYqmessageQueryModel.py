#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossCsCssocialYqmessageQueryModel(object):

    def __init__(self):
        self._search_criteria = None

    @property
    def search_criteria(self):
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, value):
        self._search_criteria = value


    def to_alipay_dict(self):
        params = dict()
        if self.search_criteria:
            if hasattr(self.search_criteria, 'to_alipay_dict'):
                params['search_criteria'] = self.search_criteria.to_alipay_dict()
            else:
                params['search_criteria'] = self.search_criteria
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossCsCssocialYqmessageQueryModel()
        if 'search_criteria' in d:
            o.search_criteria = d['search_criteria']
        return o


