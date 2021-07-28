#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeBuyerCreditConfirmModel(object):

    def __init__(self):
        self._grant_credit_quota = None
        self._grant_operation_no = None

    @property
    def grant_credit_quota(self):
        return self._grant_credit_quota

    @grant_credit_quota.setter
    def grant_credit_quota(self, value):
        self._grant_credit_quota = value
    @property
    def grant_operation_no(self):
        return self._grant_operation_no

    @grant_operation_no.setter
    def grant_operation_no(self, value):
        self._grant_operation_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.grant_credit_quota:
            if hasattr(self.grant_credit_quota, 'to_alipay_dict'):
                params['grant_credit_quota'] = self.grant_credit_quota.to_alipay_dict()
            else:
                params['grant_credit_quota'] = self.grant_credit_quota
        if self.grant_operation_no:
            if hasattr(self.grant_operation_no, 'to_alipay_dict'):
                params['grant_operation_no'] = self.grant_operation_no.to_alipay_dict()
            else:
                params['grant_operation_no'] = self.grant_operation_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeBuyerCreditConfirmModel()
        if 'grant_credit_quota' in d:
            o.grant_credit_quota = d['grant_credit_quota']
        if 'grant_operation_no' in d:
            o.grant_operation_no = d['grant_operation_no']
        return o


