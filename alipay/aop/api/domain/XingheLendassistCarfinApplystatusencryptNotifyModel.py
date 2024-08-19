#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrgLoanDetail import OrgLoanDetail


class XingheLendassistCarfinApplystatusencryptNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._loan_list = None
        self._org_status = None
        self._out_apply_no = None
        self._status = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def loan_list(self):
        return self._loan_list

    @loan_list.setter
    def loan_list(self, value):
        if isinstance(value, list):
            self._loan_list = list()
            for i in value:
                if isinstance(i, OrgLoanDetail):
                    self._loan_list.append(i)
                else:
                    self._loan_list.append(OrgLoanDetail.from_alipay_dict(i))
    @property
    def org_status(self):
        return self._org_status

    @org_status.setter
    def org_status(self, value):
        self._org_status = value
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.loan_list:
            if isinstance(self.loan_list, list):
                for i in range(0, len(self.loan_list)):
                    element = self.loan_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.loan_list[i] = element.to_alipay_dict()
            if hasattr(self.loan_list, 'to_alipay_dict'):
                params['loan_list'] = self.loan_list.to_alipay_dict()
            else:
                params['loan_list'] = self.loan_list
        if self.org_status:
            if hasattr(self.org_status, 'to_alipay_dict'):
                params['org_status'] = self.org_status.to_alipay_dict()
            else:
                params['org_status'] = self.org_status
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinApplystatusencryptNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'loan_list' in d:
            o.loan_list = d['loan_list']
        if 'org_status' in d:
            o.org_status = d['org_status']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'status' in d:
            o.status = d['status']
        return o


