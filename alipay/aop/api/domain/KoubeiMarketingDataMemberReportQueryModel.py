#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataMemberReportQueryModel(object):

    def __init__(self):
        self._biz_date = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataMemberReportQueryModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        return o


