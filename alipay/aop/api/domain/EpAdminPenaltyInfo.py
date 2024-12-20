#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpAdminPenaltyPartiesInfo import EpAdminPenaltyPartiesInfo


class EpAdminPenaltyInfo(object):

    def __init__(self):
        self._case_name = None
        self._incident_date = None
        self._issue_date = None
        self._parties = None
        self._punish_cause = None
        self._punish_date = None
        self._punish_decision = None
        self._punish_decision_no = None
        self._punish_details = None
        self._punish_gist = None
        self._punish_organ = None
        self._source = None
        self._title = None

    @property
    def case_name(self):
        return self._case_name

    @case_name.setter
    def case_name(self, value):
        self._case_name = value
    @property
    def incident_date(self):
        return self._incident_date

    @incident_date.setter
    def incident_date(self, value):
        self._incident_date = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def parties(self):
        return self._parties

    @parties.setter
    def parties(self, value):
        if isinstance(value, list):
            self._parties = list()
            for i in value:
                if isinstance(i, EpAdminPenaltyPartiesInfo):
                    self._parties.append(i)
                else:
                    self._parties.append(EpAdminPenaltyPartiesInfo.from_alipay_dict(i))
    @property
    def punish_cause(self):
        return self._punish_cause

    @punish_cause.setter
    def punish_cause(self, value):
        if isinstance(value, list):
            self._punish_cause = list()
            for i in value:
                self._punish_cause.append(i)
    @property
    def punish_date(self):
        return self._punish_date

    @punish_date.setter
    def punish_date(self, value):
        self._punish_date = value
    @property
    def punish_decision(self):
        return self._punish_decision

    @punish_decision.setter
    def punish_decision(self, value):
        if isinstance(value, list):
            self._punish_decision = list()
            for i in value:
                self._punish_decision.append(i)
    @property
    def punish_decision_no(self):
        return self._punish_decision_no

    @punish_decision_no.setter
    def punish_decision_no(self, value):
        self._punish_decision_no = value
    @property
    def punish_details(self):
        return self._punish_details

    @punish_details.setter
    def punish_details(self, value):
        self._punish_details = value
    @property
    def punish_gist(self):
        return self._punish_gist

    @punish_gist.setter
    def punish_gist(self, value):
        if isinstance(value, list):
            self._punish_gist = list()
            for i in value:
                self._punish_gist.append(i)
    @property
    def punish_organ(self):
        return self._punish_organ

    @punish_organ.setter
    def punish_organ(self, value):
        if isinstance(value, list):
            self._punish_organ = list()
            for i in value:
                self._punish_organ.append(i)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_name:
            if hasattr(self.case_name, 'to_alipay_dict'):
                params['case_name'] = self.case_name.to_alipay_dict()
            else:
                params['case_name'] = self.case_name
        if self.incident_date:
            if hasattr(self.incident_date, 'to_alipay_dict'):
                params['incident_date'] = self.incident_date.to_alipay_dict()
            else:
                params['incident_date'] = self.incident_date
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
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
        if self.punish_cause:
            if isinstance(self.punish_cause, list):
                for i in range(0, len(self.punish_cause)):
                    element = self.punish_cause[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.punish_cause[i] = element.to_alipay_dict()
            if hasattr(self.punish_cause, 'to_alipay_dict'):
                params['punish_cause'] = self.punish_cause.to_alipay_dict()
            else:
                params['punish_cause'] = self.punish_cause
        if self.punish_date:
            if hasattr(self.punish_date, 'to_alipay_dict'):
                params['punish_date'] = self.punish_date.to_alipay_dict()
            else:
                params['punish_date'] = self.punish_date
        if self.punish_decision:
            if isinstance(self.punish_decision, list):
                for i in range(0, len(self.punish_decision)):
                    element = self.punish_decision[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.punish_decision[i] = element.to_alipay_dict()
            if hasattr(self.punish_decision, 'to_alipay_dict'):
                params['punish_decision'] = self.punish_decision.to_alipay_dict()
            else:
                params['punish_decision'] = self.punish_decision
        if self.punish_decision_no:
            if hasattr(self.punish_decision_no, 'to_alipay_dict'):
                params['punish_decision_no'] = self.punish_decision_no.to_alipay_dict()
            else:
                params['punish_decision_no'] = self.punish_decision_no
        if self.punish_details:
            if hasattr(self.punish_details, 'to_alipay_dict'):
                params['punish_details'] = self.punish_details.to_alipay_dict()
            else:
                params['punish_details'] = self.punish_details
        if self.punish_gist:
            if isinstance(self.punish_gist, list):
                for i in range(0, len(self.punish_gist)):
                    element = self.punish_gist[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.punish_gist[i] = element.to_alipay_dict()
            if hasattr(self.punish_gist, 'to_alipay_dict'):
                params['punish_gist'] = self.punish_gist.to_alipay_dict()
            else:
                params['punish_gist'] = self.punish_gist
        if self.punish_organ:
            if isinstance(self.punish_organ, list):
                for i in range(0, len(self.punish_organ)):
                    element = self.punish_organ[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.punish_organ[i] = element.to_alipay_dict()
            if hasattr(self.punish_organ, 'to_alipay_dict'):
                params['punish_organ'] = self.punish_organ.to_alipay_dict()
            else:
                params['punish_organ'] = self.punish_organ
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = EpAdminPenaltyInfo()
        if 'case_name' in d:
            o.case_name = d['case_name']
        if 'incident_date' in d:
            o.incident_date = d['incident_date']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'parties' in d:
            o.parties = d['parties']
        if 'punish_cause' in d:
            o.punish_cause = d['punish_cause']
        if 'punish_date' in d:
            o.punish_date = d['punish_date']
        if 'punish_decision' in d:
            o.punish_decision = d['punish_decision']
        if 'punish_decision_no' in d:
            o.punish_decision_no = d['punish_decision_no']
        if 'punish_details' in d:
            o.punish_details = d['punish_details']
        if 'punish_gist' in d:
            o.punish_gist = d['punish_gist']
        if 'punish_organ' in d:
            o.punish_organ = d['punish_organ']
        if 'source' in d:
            o.source = d['source']
        if 'title' in d:
            o.title = d['title']
        return o


