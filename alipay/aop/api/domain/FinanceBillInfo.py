#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinanceBillInfo(object):

    def __init__(self):
        self._bill_state = None
        self._bill_type = None
        self._detail_info = None
        self._finance_bill_id = None

    @property
    def bill_state(self):
        return self._bill_state

    @bill_state.setter
    def bill_state(self, value):
        self._bill_state = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def detail_info(self):
        return self._detail_info

    @detail_info.setter
    def detail_info(self, value):
        self._detail_info = value
    @property
    def finance_bill_id(self):
        return self._finance_bill_id

    @finance_bill_id.setter
    def finance_bill_id(self, value):
        self._finance_bill_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_state:
            if hasattr(self.bill_state, 'to_alipay_dict'):
                params['bill_state'] = self.bill_state.to_alipay_dict()
            else:
                params['bill_state'] = self.bill_state
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.detail_info:
            if hasattr(self.detail_info, 'to_alipay_dict'):
                params['detail_info'] = self.detail_info.to_alipay_dict()
            else:
                params['detail_info'] = self.detail_info
        if self.finance_bill_id:
            if hasattr(self.finance_bill_id, 'to_alipay_dict'):
                params['finance_bill_id'] = self.finance_bill_id.to_alipay_dict()
            else:
                params['finance_bill_id'] = self.finance_bill_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinanceBillInfo()
        if 'bill_state' in d:
            o.bill_state = d['bill_state']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'detail_info' in d:
            o.detail_info = d['detail_info']
        if 'finance_bill_id' in d:
            o.finance_bill_id = d['finance_bill_id']
        return o


