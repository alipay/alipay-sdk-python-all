#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicArticlesummaryDataBatchqueryModel(object):

    def __init__(self):
        self._begin_date = None
        self._end_date = None

    @property
    def begin_date(self):
        return self._begin_date

    @begin_date.setter
    def begin_date(self, value):
        self._begin_date = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.begin_date:
            if hasattr(self.begin_date, 'to_alipay_dict'):
                params['begin_date'] = self.begin_date.to_alipay_dict()
            else:
                params['begin_date'] = self.begin_date
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicArticlesummaryDataBatchqueryModel()
        if 'begin_date' in d:
            o.begin_date = d['begin_date']
        if 'end_date' in d:
            o.end_date = d['end_date']
        return o


