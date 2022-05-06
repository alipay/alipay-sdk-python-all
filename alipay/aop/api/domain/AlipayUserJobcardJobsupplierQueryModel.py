#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserJobcardJobsupplierQueryModel(object):

    def __init__(self):
        self._job_supplier_code = None
        self._user_id = None

    @property
    def job_supplier_code(self):
        return self._job_supplier_code

    @job_supplier_code.setter
    def job_supplier_code(self, value):
        self._job_supplier_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.job_supplier_code:
            if hasattr(self.job_supplier_code, 'to_alipay_dict'):
                params['job_supplier_code'] = self.job_supplier_code.to_alipay_dict()
            else:
                params['job_supplier_code'] = self.job_supplier_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserJobcardJobsupplierQueryModel()
        if 'job_supplier_code' in d:
            o.job_supplier_code = d['job_supplier_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


