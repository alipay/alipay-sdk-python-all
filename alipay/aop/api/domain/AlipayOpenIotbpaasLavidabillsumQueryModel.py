#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotbpaasLavidabillsumQueryModel(object):

    def __init__(self):
        self._query_date = None

    @property
    def query_date(self):
        return self._query_date

    @query_date.setter
    def query_date(self, value):
        self._query_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.query_date:
            if hasattr(self.query_date, 'to_alipay_dict'):
                params['query_date'] = self.query_date.to_alipay_dict()
            else:
                params['query_date'] = self.query_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotbpaasLavidabillsumQueryModel()
        if 'query_date' in d:
            o.query_date = d['query_date']
        return o


