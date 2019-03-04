#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizResData(object):

    def __init__(self):
        self._biz_amount = None
        self._biz_date = None
        self._biz_no = None
        self._biz_user_id = None

    @property
    def biz_amount(self):
        return self._biz_amount

    @biz_amount.setter
    def biz_amount(self, value):
        self._biz_amount = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_user_id(self):
        return self._biz_user_id

    @biz_user_id.setter
    def biz_user_id(self, value):
        self._biz_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_amount:
            if hasattr(self.biz_amount, 'to_alipay_dict'):
                params['biz_amount'] = self.biz_amount.to_alipay_dict()
            else:
                params['biz_amount'] = self.biz_amount
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_user_id:
            if hasattr(self.biz_user_id, 'to_alipay_dict'):
                params['biz_user_id'] = self.biz_user_id.to_alipay_dict()
            else:
                params['biz_user_id'] = self.biz_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizResData()
        if 'biz_amount' in d:
            o.biz_amount = d['biz_amount']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_user_id' in d:
            o.biz_user_id = d['biz_user_id']
        return o


