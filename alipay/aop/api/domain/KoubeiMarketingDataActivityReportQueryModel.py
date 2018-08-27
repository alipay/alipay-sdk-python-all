#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataActivityReportQueryModel(object):

    def __init__(self):
        self._biz_date = None
        self._camp_id = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataActivityReportQueryModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        return o


