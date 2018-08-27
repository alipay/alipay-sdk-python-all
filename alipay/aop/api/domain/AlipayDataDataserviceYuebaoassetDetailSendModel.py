#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlmReportData import AlmReportData


class AlipayDataDataserviceYuebaoassetDetailSendModel(object):

    def __init__(self):
        self._alm_report_data = None

    @property
    def alm_report_data(self):
        return self._alm_report_data

    @alm_report_data.setter
    def alm_report_data(self, value):
        if isinstance(value, list):
            self._alm_report_data = list()
            for i in value:
                if isinstance(i, AlmReportData):
                    self._alm_report_data.append(i)
                else:
                    self._alm_report_data.append(AlmReportData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alm_report_data:
            if isinstance(self.alm_report_data, list):
                for i in range(0, len(self.alm_report_data)):
                    element = self.alm_report_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.alm_report_data[i] = element.to_alipay_dict()
            if hasattr(self.alm_report_data, 'to_alipay_dict'):
                params['alm_report_data'] = self.alm_report_data.to_alipay_dict()
            else:
                params['alm_report_data'] = self.alm_report_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceYuebaoassetDetailSendModel()
        if 'alm_report_data' in d:
            o.alm_report_data = d['alm_report_data']
        return o


