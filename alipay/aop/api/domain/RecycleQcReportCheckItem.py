#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleQcReportResult import RecycleQcReportResult
from alipay.aop.api.domain.RecycleQcReportResult import RecycleQcReportResult


class RecycleQcReportCheckItem(object):

    def __init__(self):
        self._is_consistent = None
        self._merchant_check_result = None
        self._user_self_check_result = None

    @property
    def is_consistent(self):
        return self._is_consistent

    @is_consistent.setter
    def is_consistent(self, value):
        self._is_consistent = value
    @property
    def merchant_check_result(self):
        return self._merchant_check_result

    @merchant_check_result.setter
    def merchant_check_result(self, value):
        if isinstance(value, RecycleQcReportResult):
            self._merchant_check_result = value
        else:
            self._merchant_check_result = RecycleQcReportResult.from_alipay_dict(value)
    @property
    def user_self_check_result(self):
        return self._user_self_check_result

    @user_self_check_result.setter
    def user_self_check_result(self, value):
        if isinstance(value, RecycleQcReportResult):
            self._user_self_check_result = value
        else:
            self._user_self_check_result = RecycleQcReportResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.is_consistent:
            if hasattr(self.is_consistent, 'to_alipay_dict'):
                params['is_consistent'] = self.is_consistent.to_alipay_dict()
            else:
                params['is_consistent'] = self.is_consistent
        if self.merchant_check_result:
            if hasattr(self.merchant_check_result, 'to_alipay_dict'):
                params['merchant_check_result'] = self.merchant_check_result.to_alipay_dict()
            else:
                params['merchant_check_result'] = self.merchant_check_result
        if self.user_self_check_result:
            if hasattr(self.user_self_check_result, 'to_alipay_dict'):
                params['user_self_check_result'] = self.user_self_check_result.to_alipay_dict()
            else:
                params['user_self_check_result'] = self.user_self_check_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleQcReportCheckItem()
        if 'is_consistent' in d:
            o.is_consistent = d['is_consistent']
        if 'merchant_check_result' in d:
            o.merchant_check_result = d['merchant_check_result']
        if 'user_self_check_result' in d:
            o.user_self_check_result = d['user_self_check_result']
        return o


