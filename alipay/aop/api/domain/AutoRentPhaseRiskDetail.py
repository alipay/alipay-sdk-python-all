#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AutoRentSingleRiskDetail import AutoRentSingleRiskDetail


class AutoRentPhaseRiskDetail(object):

    def __init__(self):
        self._auto_rent_single_risk_details = None
        self._phase = None
        self._risk_level = None

    @property
    def auto_rent_single_risk_details(self):
        return self._auto_rent_single_risk_details

    @auto_rent_single_risk_details.setter
    def auto_rent_single_risk_details(self, value):
        if isinstance(value, list):
            self._auto_rent_single_risk_details = list()
            for i in value:
                if isinstance(i, AutoRentSingleRiskDetail):
                    self._auto_rent_single_risk_details.append(i)
                else:
                    self._auto_rent_single_risk_details.append(AutoRentSingleRiskDetail.from_alipay_dict(i))
    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_rent_single_risk_details:
            if isinstance(self.auto_rent_single_risk_details, list):
                for i in range(0, len(self.auto_rent_single_risk_details)):
                    element = self.auto_rent_single_risk_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.auto_rent_single_risk_details[i] = element.to_alipay_dict()
            if hasattr(self.auto_rent_single_risk_details, 'to_alipay_dict'):
                params['auto_rent_single_risk_details'] = self.auto_rent_single_risk_details.to_alipay_dict()
            else:
                params['auto_rent_single_risk_details'] = self.auto_rent_single_risk_details
        if self.phase:
            if hasattr(self.phase, 'to_alipay_dict'):
                params['phase'] = self.phase.to_alipay_dict()
            else:
                params['phase'] = self.phase
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AutoRentPhaseRiskDetail()
        if 'auto_rent_single_risk_details' in d:
            o.auto_rent_single_risk_details = d['auto_rent_single_risk_details']
        if 'phase' in d:
            o.phase = d['phase']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        return o


