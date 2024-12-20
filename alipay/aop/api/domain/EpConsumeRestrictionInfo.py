#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpConsumeRestrictionInfo(object):

    def __init__(self):
        self._case_no = None
        self._case_register_date = None
        self._enterprise_information = None
        self._execution_court = None
        self._issue_date = None
        self._xzxfryxm = None

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
    def enterprise_information(self):
        return self._enterprise_information

    @enterprise_information.setter
    def enterprise_information(self, value):
        self._enterprise_information = value
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
    def xzxfryxm(self):
        return self._xzxfryxm

    @xzxfryxm.setter
    def xzxfryxm(self, value):
        self._xzxfryxm = value


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
        if self.enterprise_information:
            if hasattr(self.enterprise_information, 'to_alipay_dict'):
                params['enterprise_information'] = self.enterprise_information.to_alipay_dict()
            else:
                params['enterprise_information'] = self.enterprise_information
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
        if self.xzxfryxm:
            if hasattr(self.xzxfryxm, 'to_alipay_dict'):
                params['xzxfryxm'] = self.xzxfryxm.to_alipay_dict()
            else:
                params['xzxfryxm'] = self.xzxfryxm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpConsumeRestrictionInfo()
        if 'case_no' in d:
            o.case_no = d['case_no']
        if 'case_register_date' in d:
            o.case_register_date = d['case_register_date']
        if 'enterprise_information' in d:
            o.enterprise_information = d['enterprise_information']
        if 'execution_court' in d:
            o.execution_court = d['execution_court']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'xzxfryxm' in d:
            o.xzxfryxm = d['xzxfryxm']
        return o


