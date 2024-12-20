#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpSubordinateRegionalInfo import EpSubordinateRegionalInfo
from alipay.aop.api.domain.EpPartiesDetailsInfo import EpPartiesDetailsInfo


class EpCourtNoticeInfo(object):

    def __init__(self):
        self._affiliating_area = None
        self._body = None
        self._case_cause = None
        self._case_no = None
        self._court = None
        self._court_date = None
        self._issue_date = None
        self._other_roles = None
        self._parties_details = None
        self._titles = None

    @property
    def affiliating_area(self):
        return self._affiliating_area

    @affiliating_area.setter
    def affiliating_area(self, value):
        if isinstance(value, EpSubordinateRegionalInfo):
            self._affiliating_area = value
        else:
            self._affiliating_area = EpSubordinateRegionalInfo.from_alipay_dict(value)
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
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
    def court_date(self):
        return self._court_date

    @court_date.setter
    def court_date(self, value):
        self._court_date = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def other_roles(self):
        return self._other_roles

    @other_roles.setter
    def other_roles(self, value):
        if isinstance(value, list):
            self._other_roles = list()
            for i in value:
                self._other_roles.append(i)
    @property
    def parties_details(self):
        return self._parties_details

    @parties_details.setter
    def parties_details(self, value):
        if isinstance(value, list):
            self._parties_details = list()
            for i in value:
                if isinstance(i, EpPartiesDetailsInfo):
                    self._parties_details.append(i)
                else:
                    self._parties_details.append(EpPartiesDetailsInfo.from_alipay_dict(i))
    @property
    def titles(self):
        return self._titles

    @titles.setter
    def titles(self, value):
        self._titles = value


    def to_alipay_dict(self):
        params = dict()
        if self.affiliating_area:
            if hasattr(self.affiliating_area, 'to_alipay_dict'):
                params['affiliating_area'] = self.affiliating_area.to_alipay_dict()
            else:
                params['affiliating_area'] = self.affiliating_area
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
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
        if self.court_date:
            if hasattr(self.court_date, 'to_alipay_dict'):
                params['court_date'] = self.court_date.to_alipay_dict()
            else:
                params['court_date'] = self.court_date
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.other_roles:
            if isinstance(self.other_roles, list):
                for i in range(0, len(self.other_roles)):
                    element = self.other_roles[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_roles[i] = element.to_alipay_dict()
            if hasattr(self.other_roles, 'to_alipay_dict'):
                params['other_roles'] = self.other_roles.to_alipay_dict()
            else:
                params['other_roles'] = self.other_roles
        if self.parties_details:
            if isinstance(self.parties_details, list):
                for i in range(0, len(self.parties_details)):
                    element = self.parties_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.parties_details[i] = element.to_alipay_dict()
            if hasattr(self.parties_details, 'to_alipay_dict'):
                params['parties_details'] = self.parties_details.to_alipay_dict()
            else:
                params['parties_details'] = self.parties_details
        if self.titles:
            if hasattr(self.titles, 'to_alipay_dict'):
                params['titles'] = self.titles.to_alipay_dict()
            else:
                params['titles'] = self.titles
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpCourtNoticeInfo()
        if 'affiliating_area' in d:
            o.affiliating_area = d['affiliating_area']
        if 'body' in d:
            o.body = d['body']
        if 'case_cause' in d:
            o.case_cause = d['case_cause']
        if 'case_no' in d:
            o.case_no = d['case_no']
        if 'court' in d:
            o.court = d['court']
        if 'court_date' in d:
            o.court_date = d['court_date']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'other_roles' in d:
            o.other_roles = d['other_roles']
        if 'parties_details' in d:
            o.parties_details = d['parties_details']
        if 'titles' in d:
            o.titles = d['titles']
        return o


