#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpVerdictPartiesInfo import EpVerdictPartiesInfo


class EpVerdictInfo(object):

    def __init__(self):
        self._case_cause = None
        self._case_no = None
        self._court = None
        self._issue_date = None
        self._judgment_date = None
        self._parties = None
        self._payment_sum = None
        self._title = None

    @property
    def case_cause(self):
        return self._case_cause

    @case_cause.setter
    def case_cause(self, value):
        self._case_cause = value
    @property
    def case_no(self):
        return self._case_no

    @case_no.setter
    def case_no(self, value):
        self._case_no = value
    @property
    def court(self):
        return self._court

    @court.setter
    def court(self, value):
        self._court = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def judgment_date(self):
        return self._judgment_date

    @judgment_date.setter
    def judgment_date(self, value):
        self._judgment_date = value
    @property
    def parties(self):
        return self._parties

    @parties.setter
    def parties(self, value):
        if isinstance(value, list):
            self._parties = list()
            for i in value:
                if isinstance(i, EpVerdictPartiesInfo):
                    self._parties.append(i)
                else:
                    self._parties.append(EpVerdictPartiesInfo.from_alipay_dict(i))
    @property
    def payment_sum(self):
        return self._payment_sum

    @payment_sum.setter
    def payment_sum(self, value):
        self._payment_sum = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_cause:
            if hasattr(self.case_cause, 'to_alipay_dict'):
                params['case_cause'] = self.case_cause.to_alipay_dict()
            else:
                params['case_cause'] = self.case_cause
        if self.case_no:
            if hasattr(self.case_no, 'to_alipay_dict'):
                params['case_no'] = self.case_no.to_alipay_dict()
            else:
                params['case_no'] = self.case_no
        if self.court:
            if hasattr(self.court, 'to_alipay_dict'):
                params['court'] = self.court.to_alipay_dict()
            else:
                params['court'] = self.court
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.judgment_date:
            if hasattr(self.judgment_date, 'to_alipay_dict'):
                params['judgment_date'] = self.judgment_date.to_alipay_dict()
            else:
                params['judgment_date'] = self.judgment_date
        if self.parties:
            if isinstance(self.parties, list):
                for i in range(0, len(self.parties)):
                    element = self.parties[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.parties[i] = element.to_alipay_dict()
            if hasattr(self.parties, 'to_alipay_dict'):
                params['parties'] = self.parties.to_alipay_dict()
            else:
                params['parties'] = self.parties
        if self.payment_sum:
            if hasattr(self.payment_sum, 'to_alipay_dict'):
                params['payment_sum'] = self.payment_sum.to_alipay_dict()
            else:
                params['payment_sum'] = self.payment_sum
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpVerdictInfo()
        if 'case_cause' in d:
            o.case_cause = d['case_cause']
        if 'case_no' in d:
            o.case_no = d['case_no']
        if 'court' in d:
            o.court = d['court']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'judgment_date' in d:
            o.judgment_date = d['judgment_date']
        if 'parties' in d:
            o.parties = d['parties']
        if 'payment_sum' in d:
            o.payment_sum = d['payment_sum']
        if 'title' in d:
            o.title = d['title']
        return o


