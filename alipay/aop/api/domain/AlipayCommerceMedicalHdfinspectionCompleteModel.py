#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChceckReport import ChceckReport


class AlipayCommerceMedicalHdfinspectionCompleteModel(object):

    def __init__(self):
        self._biz_source = None
        self._reports = None
        self._reserve_code = None

    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def reports(self):
        return self._reports

    @reports.setter
    def reports(self, value):
        if isinstance(value, list):
            self._reports = list()
            for i in value:
                if isinstance(i, ChceckReport):
                    self._reports.append(i)
                else:
                    self._reports.append(ChceckReport.from_alipay_dict(i))
    @property
    def reserve_code(self):
        return self._reserve_code

    @reserve_code.setter
    def reserve_code(self, value):
        self._reserve_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.reports:
            if isinstance(self.reports, list):
                for i in range(0, len(self.reports)):
                    element = self.reports[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reports[i] = element.to_alipay_dict()
            if hasattr(self.reports, 'to_alipay_dict'):
                params['reports'] = self.reports.to_alipay_dict()
            else:
                params['reports'] = self.reports
        if self.reserve_code:
            if hasattr(self.reserve_code, 'to_alipay_dict'):
                params['reserve_code'] = self.reserve_code.to_alipay_dict()
            else:
                params['reserve_code'] = self.reserve_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfinspectionCompleteModel()
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'reports' in d:
            o.reports = d['reports']
        if 'reserve_code' in d:
            o.reserve_code = d['reserve_code']
        return o


