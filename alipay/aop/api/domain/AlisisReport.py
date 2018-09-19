#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReportCondition import ReportCondition


class AlisisReport(object):

    def __init__(self):
        self._conditions = None
        self._report_desc = None
        self._report_name = None
        self._report_uk = None

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        if isinstance(value, list):
            self._conditions = list()
            for i in value:
                if isinstance(i, ReportCondition):
                    self._conditions.append(i)
                else:
                    self._conditions.append(ReportCondition.from_alipay_dict(i))
    @property
    def report_desc(self):
        return self._report_desc

    @report_desc.setter
    def report_desc(self, value):
        self._report_desc = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_uk(self):
        return self._report_uk

    @report_uk.setter
    def report_uk(self, value):
        self._report_uk = value


    def to_alipay_dict(self):
        params = dict()
        if self.conditions:
            if isinstance(self.conditions, list):
                for i in range(0, len(self.conditions)):
                    element = self.conditions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conditions[i] = element.to_alipay_dict()
            if hasattr(self.conditions, 'to_alipay_dict'):
                params['conditions'] = self.conditions.to_alipay_dict()
            else:
                params['conditions'] = self.conditions
        if self.report_desc:
            if hasattr(self.report_desc, 'to_alipay_dict'):
                params['report_desc'] = self.report_desc.to_alipay_dict()
            else:
                params['report_desc'] = self.report_desc
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_uk:
            if hasattr(self.report_uk, 'to_alipay_dict'):
                params['report_uk'] = self.report_uk.to_alipay_dict()
            else:
                params['report_uk'] = self.report_uk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlisisReport()
        if 'conditions' in d:
            o.conditions = d['conditions']
        if 'report_desc' in d:
            o.report_desc = d['report_desc']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_uk' in d:
            o.report_uk = d['report_uk']
        return o


