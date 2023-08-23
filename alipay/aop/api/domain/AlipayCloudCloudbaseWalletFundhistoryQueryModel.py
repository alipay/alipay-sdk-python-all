#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseWalletFundhistoryQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._fund_date = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def fund_date(self):
        return self._fund_date

    @fund_date.setter
    def fund_date(self, value):
        self._fund_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.fund_date:
            if hasattr(self.fund_date, 'to_alipay_dict'):
                params['fund_date'] = self.fund_date.to_alipay_dict()
            else:
                params['fund_date'] = self.fund_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseWalletFundhistoryQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'fund_date' in d:
            o.fund_date = d['fund_date']
        return o


