#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceYuebaolqdDetailQueryModel(object):

    def __init__(self):
        self._report_date = None

    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceYuebaolqdDetailQueryModel()
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o


