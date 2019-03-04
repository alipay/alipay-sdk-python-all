#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MemberBenefitModel(object):

    def __init__(self):
        self._benefit_desc = None
        self._end_date = None
        self._start_date = None
        self._title = None

    @property
    def benefit_desc(self):
        return self._benefit_desc

    @benefit_desc.setter
    def benefit_desc(self, value):
        if isinstance(value, list):
            self._benefit_desc = list()
            for i in value:
                self._benefit_desc.append(i)
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_desc:
            if isinstance(self.benefit_desc, list):
                for i in range(0, len(self.benefit_desc)):
                    element = self.benefit_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_desc[i] = element.to_alipay_dict()
            if hasattr(self.benefit_desc, 'to_alipay_dict'):
                params['benefit_desc'] = self.benefit_desc.to_alipay_dict()
            else:
                params['benefit_desc'] = self.benefit_desc
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
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
        o = MemberBenefitModel()
        if 'benefit_desc' in d:
            o.benefit_desc = d['benefit_desc']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'title' in d:
            o.title = d['title']
        return o


