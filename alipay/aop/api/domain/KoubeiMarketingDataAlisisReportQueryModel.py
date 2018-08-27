#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReportQueryCondition import ReportQueryCondition


class KoubeiMarketingDataAlisisReportQueryModel(object):

    def __init__(self):
        self._conditions = None
        self._report_uk = None

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        if isinstance(value, list):
            self._conditions = list()
            for i in value:
                if isinstance(i, ReportQueryCondition):
                    self._conditions.append(i)
                else:
                    self._conditions.append(ReportQueryCondition.from_alipay_dict(i))
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
        o = KoubeiMarketingDataAlisisReportQueryModel()
        if 'conditions' in d:
            o.conditions = d['conditions']
        if 'report_uk' in d:
            o.report_uk = d['report_uk']
        return o


