#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VerticalRiskVO(object):

    def __init__(self):
        self._fulfillment_capacity_level = None
        self._mediary_risk_level = None
        self._ongoing_rent_level = None

    @property
    def fulfillment_capacity_level(self):
        return self._fulfillment_capacity_level

    @fulfillment_capacity_level.setter
    def fulfillment_capacity_level(self, value):
        self._fulfillment_capacity_level = value
    @property
    def mediary_risk_level(self):
        return self._mediary_risk_level

    @mediary_risk_level.setter
    def mediary_risk_level(self, value):
        self._mediary_risk_level = value
    @property
    def ongoing_rent_level(self):
        return self._ongoing_rent_level

    @ongoing_rent_level.setter
    def ongoing_rent_level(self, value):
        self._ongoing_rent_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_capacity_level:
            if hasattr(self.fulfillment_capacity_level, 'to_alipay_dict'):
                params['fulfillment_capacity_level'] = self.fulfillment_capacity_level.to_alipay_dict()
            else:
                params['fulfillment_capacity_level'] = self.fulfillment_capacity_level
        if self.mediary_risk_level:
            if hasattr(self.mediary_risk_level, 'to_alipay_dict'):
                params['mediary_risk_level'] = self.mediary_risk_level.to_alipay_dict()
            else:
                params['mediary_risk_level'] = self.mediary_risk_level
        if self.ongoing_rent_level:
            if hasattr(self.ongoing_rent_level, 'to_alipay_dict'):
                params['ongoing_rent_level'] = self.ongoing_rent_level.to_alipay_dict()
            else:
                params['ongoing_rent_level'] = self.ongoing_rent_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VerticalRiskVO()
        if 'fulfillment_capacity_level' in d:
            o.fulfillment_capacity_level = d['fulfillment_capacity_level']
        if 'mediary_risk_level' in d:
            o.mediary_risk_level = d['mediary_risk_level']
        if 'ongoing_rent_level' in d:
            o.ongoing_rent_level = d['ongoing_rent_level']
        return o


