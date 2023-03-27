#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Reasons import Reasons


class ItemRiskInfo(object):

    def __init__(self):
        self._audit_time = None
        self._risk_infos = None

    @property
    def audit_time(self):
        return self._audit_time

    @audit_time.setter
    def audit_time(self, value):
        self._audit_time = value
    @property
    def risk_infos(self):
        return self._risk_infos

    @risk_infos.setter
    def risk_infos(self, value):
        if isinstance(value, Reasons):
            self._risk_infos = value
        else:
            self._risk_infos = Reasons.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.audit_time:
            if hasattr(self.audit_time, 'to_alipay_dict'):
                params['audit_time'] = self.audit_time.to_alipay_dict()
            else:
                params['audit_time'] = self.audit_time
        if self.risk_infos:
            if hasattr(self.risk_infos, 'to_alipay_dict'):
                params['risk_infos'] = self.risk_infos.to_alipay_dict()
            else:
                params['risk_infos'] = self.risk_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemRiskInfo()
        if 'audit_time' in d:
            o.audit_time = d['audit_time']
        if 'risk_infos' in d:
            o.risk_infos = d['risk_infos']
        return o


