#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpFinalCaseInfo(object):

    def __init__(self):
        self._case_no = None
        self._case_register_date = None
        self._end_date = None
        self._execution_court = None
        self._issue_date = None
        self._outstanding_amount = None
        self._performed_name = None
        self._xzbd = None

    @property
    def case_no(self):
        return self._case_no

    @case_no.setter
    def case_no(self, value):
        self._case_no = value
    @property
    def case_register_date(self):
        return self._case_register_date

    @case_register_date.setter
    def case_register_date(self, value):
        self._case_register_date = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def execution_court(self):
        return self._execution_court

    @execution_court.setter
    def execution_court(self, value):
        self._execution_court = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def outstanding_amount(self):
        return self._outstanding_amount

    @outstanding_amount.setter
    def outstanding_amount(self, value):
        self._outstanding_amount = value
    @property
    def performed_name(self):
        return self._performed_name

    @performed_name.setter
    def performed_name(self, value):
        self._performed_name = value
    @property
    def xzbd(self):
        return self._xzbd

    @xzbd.setter
    def xzbd(self, value):
        self._xzbd = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_no:
            if hasattr(self.case_no, 'to_alipay_dict'):
                params['case_no'] = self.case_no.to_alipay_dict()
            else:
                params['case_no'] = self.case_no
        if self.case_register_date:
            if hasattr(self.case_register_date, 'to_alipay_dict'):
                params['case_register_date'] = self.case_register_date.to_alipay_dict()
            else:
                params['case_register_date'] = self.case_register_date
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.execution_court:
            if hasattr(self.execution_court, 'to_alipay_dict'):
                params['execution_court'] = self.execution_court.to_alipay_dict()
            else:
                params['execution_court'] = self.execution_court
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.outstanding_amount:
            if hasattr(self.outstanding_amount, 'to_alipay_dict'):
                params['outstanding_amount'] = self.outstanding_amount.to_alipay_dict()
            else:
                params['outstanding_amount'] = self.outstanding_amount
        if self.performed_name:
            if hasattr(self.performed_name, 'to_alipay_dict'):
                params['performed_name'] = self.performed_name.to_alipay_dict()
            else:
                params['performed_name'] = self.performed_name
        if self.xzbd:
            if hasattr(self.xzbd, 'to_alipay_dict'):
                params['xzbd'] = self.xzbd.to_alipay_dict()
            else:
                params['xzbd'] = self.xzbd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpFinalCaseInfo()
        if 'case_no' in d:
            o.case_no = d['case_no']
        if 'case_register_date' in d:
            o.case_register_date = d['case_register_date']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'execution_court' in d:
            o.execution_court = d['execution_court']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'outstanding_amount' in d:
            o.outstanding_amount = d['outstanding_amount']
        if 'performed_name' in d:
            o.performed_name = d['performed_name']
        if 'xzbd' in d:
            o.xzbd = d['xzbd']
        return o


