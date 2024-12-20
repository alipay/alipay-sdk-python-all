#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpLitigationNoticeInfo(object):

    def __init__(self):
        self._body = None
        self._parties = None
        self._proclamation_date = None
        self._proclamation_people = None
        self._proclamation_type = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def parties(self):
        return self._parties

    @parties.setter
    def parties(self, value):
        if isinstance(value, list):
            self._parties = list()
            for i in value:
                self._parties.append(i)
    @property
    def proclamation_date(self):
        return self._proclamation_date

    @proclamation_date.setter
    def proclamation_date(self, value):
        self._proclamation_date = value
    @property
    def proclamation_people(self):
        return self._proclamation_people

    @proclamation_people.setter
    def proclamation_people(self, value):
        self._proclamation_people = value
    @property
    def proclamation_type(self):
        return self._proclamation_type

    @proclamation_type.setter
    def proclamation_type(self, value):
        self._proclamation_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
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
        if self.proclamation_date:
            if hasattr(self.proclamation_date, 'to_alipay_dict'):
                params['proclamation_date'] = self.proclamation_date.to_alipay_dict()
            else:
                params['proclamation_date'] = self.proclamation_date
        if self.proclamation_people:
            if hasattr(self.proclamation_people, 'to_alipay_dict'):
                params['proclamation_people'] = self.proclamation_people.to_alipay_dict()
            else:
                params['proclamation_people'] = self.proclamation_people
        if self.proclamation_type:
            if hasattr(self.proclamation_type, 'to_alipay_dict'):
                params['proclamation_type'] = self.proclamation_type.to_alipay_dict()
            else:
                params['proclamation_type'] = self.proclamation_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpLitigationNoticeInfo()
        if 'body' in d:
            o.body = d['body']
        if 'parties' in d:
            o.parties = d['parties']
        if 'proclamation_date' in d:
            o.proclamation_date = d['proclamation_date']
        if 'proclamation_people' in d:
            o.proclamation_people = d['proclamation_people']
        if 'proclamation_type' in d:
            o.proclamation_type = d['proclamation_type']
        return o


