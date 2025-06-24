#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReportConfigVO import ReportConfigVO


class SavePatrolReportConfigVO(object):

    def __init__(self):
        self._report_config = None
        self._report_switch = None

    @property
    def report_config(self):
        return self._report_config

    @report_config.setter
    def report_config(self, value):
        if isinstance(value, list):
            self._report_config = list()
            for i in value:
                if isinstance(i, ReportConfigVO):
                    self._report_config.append(i)
                else:
                    self._report_config.append(ReportConfigVO.from_alipay_dict(i))
    @property
    def report_switch(self):
        return self._report_switch

    @report_switch.setter
    def report_switch(self, value):
        self._report_switch = value


    def to_alipay_dict(self):
        params = dict()
        if self.report_config:
            if isinstance(self.report_config, list):
                for i in range(0, len(self.report_config)):
                    element = self.report_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_config[i] = element.to_alipay_dict()
            if hasattr(self.report_config, 'to_alipay_dict'):
                params['report_config'] = self.report_config.to_alipay_dict()
            else:
                params['report_config'] = self.report_config
        if self.report_switch:
            if hasattr(self.report_switch, 'to_alipay_dict'):
                params['report_switch'] = self.report_switch.to_alipay_dict()
            else:
                params['report_switch'] = self.report_switch
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SavePatrolReportConfigVO()
        if 'report_config' in d:
            o.report_config = d['report_config']
        if 'report_switch' in d:
            o.report_switch = d['report_switch']
        return o


