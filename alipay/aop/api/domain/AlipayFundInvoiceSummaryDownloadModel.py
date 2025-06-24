#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundInvoiceSummaryDownloadModel(object):

    def __init__(self):
        self._check_date = None

    @property
    def check_date(self):
        return self._check_date

    @check_date.setter
    def check_date(self, value):
        self._check_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_date:
            if hasattr(self.check_date, 'to_alipay_dict'):
                params['check_date'] = self.check_date.to_alipay_dict()
            else:
                params['check_date'] = self.check_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundInvoiceSummaryDownloadModel()
        if 'check_date' in d:
            o.check_date = d['check_date']
        return o


