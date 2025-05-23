#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInstitutionExportQueryModel(object):

    def __init__(self):
        self._aggr_day = None
        self._end_date = None
        self._scc = None
        self._start_date = None

    @property
    def aggr_day(self):
        return self._aggr_day

    @aggr_day.setter
    def aggr_day(self, value):
        self._aggr_day = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def scc(self):
        return self._scc

    @scc.setter
    def scc(self, value):
        self._scc = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggr_day:
            if hasattr(self.aggr_day, 'to_alipay_dict'):
                params['aggr_day'] = self.aggr_day.to_alipay_dict()
            else:
                params['aggr_day'] = self.aggr_day
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.scc:
            if hasattr(self.scc, 'to_alipay_dict'):
                params['scc'] = self.scc.to_alipay_dict()
            else:
                params['scc'] = self.scc
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInstitutionExportQueryModel()
        if 'aggr_day' in d:
            o.aggr_day = d['aggr_day']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'scc' in d:
            o.scc = d['scc']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


