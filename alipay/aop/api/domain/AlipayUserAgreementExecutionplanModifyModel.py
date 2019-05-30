#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementExecutionplanModifyModel(object):

    def __init__(self):
        self._agreement_no = None
        self._deduct_time = None
        self._memo = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def deduct_time(self):
        return self._deduct_time

    @deduct_time.setter
    def deduct_time(self, value):
        self._deduct_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.deduct_time:
            if hasattr(self.deduct_time, 'to_alipay_dict'):
                params['deduct_time'] = self.deduct_time.to_alipay_dict()
            else:
                params['deduct_time'] = self.deduct_time
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementExecutionplanModifyModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'deduct_time' in d:
            o.deduct_time = d['deduct_time']
        if 'memo' in d:
            o.memo = d['memo']
        return o


