#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArrangementBaseSelector(object):

    def __init__(self):
        self._ar_statuses = None
        self._mark_type = None
        self._pd_codes = None
        self._pd_marks = None
        self._select_pd_mark = None
        self._select_pd_name = None

    @property
    def ar_statuses(self):
        return self._ar_statuses

    @ar_statuses.setter
    def ar_statuses(self, value):
        if isinstance(value, list):
            self._ar_statuses = list()
            for i in value:
                self._ar_statuses.append(i)
    @property
    def mark_type(self):
        return self._mark_type

    @mark_type.setter
    def mark_type(self, value):
        self._mark_type = value
    @property
    def pd_codes(self):
        return self._pd_codes

    @pd_codes.setter
    def pd_codes(self, value):
        if isinstance(value, list):
            self._pd_codes = list()
            for i in value:
                self._pd_codes.append(i)
    @property
    def pd_marks(self):
        return self._pd_marks

    @pd_marks.setter
    def pd_marks(self, value):
        if isinstance(value, list):
            self._pd_marks = list()
            for i in value:
                self._pd_marks.append(i)
    @property
    def select_pd_mark(self):
        return self._select_pd_mark

    @select_pd_mark.setter
    def select_pd_mark(self, value):
        self._select_pd_mark = value
    @property
    def select_pd_name(self):
        return self._select_pd_name

    @select_pd_name.setter
    def select_pd_name(self, value):
        self._select_pd_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_statuses:
            if isinstance(self.ar_statuses, list):
                for i in range(0, len(self.ar_statuses)):
                    element = self.ar_statuses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ar_statuses[i] = element.to_alipay_dict()
            if hasattr(self.ar_statuses, 'to_alipay_dict'):
                params['ar_statuses'] = self.ar_statuses.to_alipay_dict()
            else:
                params['ar_statuses'] = self.ar_statuses
        if self.mark_type:
            if hasattr(self.mark_type, 'to_alipay_dict'):
                params['mark_type'] = self.mark_type.to_alipay_dict()
            else:
                params['mark_type'] = self.mark_type
        if self.pd_codes:
            if isinstance(self.pd_codes, list):
                for i in range(0, len(self.pd_codes)):
                    element = self.pd_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pd_codes[i] = element.to_alipay_dict()
            if hasattr(self.pd_codes, 'to_alipay_dict'):
                params['pd_codes'] = self.pd_codes.to_alipay_dict()
            else:
                params['pd_codes'] = self.pd_codes
        if self.pd_marks:
            if isinstance(self.pd_marks, list):
                for i in range(0, len(self.pd_marks)):
                    element = self.pd_marks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pd_marks[i] = element.to_alipay_dict()
            if hasattr(self.pd_marks, 'to_alipay_dict'):
                params['pd_marks'] = self.pd_marks.to_alipay_dict()
            else:
                params['pd_marks'] = self.pd_marks
        if self.select_pd_mark:
            if hasattr(self.select_pd_mark, 'to_alipay_dict'):
                params['select_pd_mark'] = self.select_pd_mark.to_alipay_dict()
            else:
                params['select_pd_mark'] = self.select_pd_mark
        if self.select_pd_name:
            if hasattr(self.select_pd_name, 'to_alipay_dict'):
                params['select_pd_name'] = self.select_pd_name.to_alipay_dict()
            else:
                params['select_pd_name'] = self.select_pd_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArrangementBaseSelector()
        if 'ar_statuses' in d:
            o.ar_statuses = d['ar_statuses']
        if 'mark_type' in d:
            o.mark_type = d['mark_type']
        if 'pd_codes' in d:
            o.pd_codes = d['pd_codes']
        if 'pd_marks' in d:
            o.pd_marks = d['pd_marks']
        if 'select_pd_mark' in d:
            o.select_pd_mark = d['select_pd_mark']
        if 'select_pd_name' in d:
            o.select_pd_name = d['select_pd_name']
        return o


