#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShipVerticalRiskVO import ShipVerticalRiskVO


class ShipAssessmentResultVO(object):

    def __init__(self):
        self._custom_ship_quality_flag = None
        self._error_reason = None
        self._ship_advice = None
        self._ship_assessment_results_level = None
        self._ship_comprehensive_risk_level = None
        self._ship_quality_flag = None
        self._vertical_risk = None

    @property
    def custom_ship_quality_flag(self):
        return self._custom_ship_quality_flag

    @custom_ship_quality_flag.setter
    def custom_ship_quality_flag(self, value):
        self._custom_ship_quality_flag = value
    @property
    def error_reason(self):
        return self._error_reason

    @error_reason.setter
    def error_reason(self, value):
        self._error_reason = value
    @property
    def ship_advice(self):
        return self._ship_advice

    @ship_advice.setter
    def ship_advice(self, value):
        self._ship_advice = value
    @property
    def ship_assessment_results_level(self):
        return self._ship_assessment_results_level

    @ship_assessment_results_level.setter
    def ship_assessment_results_level(self, value):
        self._ship_assessment_results_level = value
    @property
    def ship_comprehensive_risk_level(self):
        return self._ship_comprehensive_risk_level

    @ship_comprehensive_risk_level.setter
    def ship_comprehensive_risk_level(self, value):
        self._ship_comprehensive_risk_level = value
    @property
    def ship_quality_flag(self):
        return self._ship_quality_flag

    @ship_quality_flag.setter
    def ship_quality_flag(self, value):
        self._ship_quality_flag = value
    @property
    def vertical_risk(self):
        return self._vertical_risk

    @vertical_risk.setter
    def vertical_risk(self, value):
        if isinstance(value, ShipVerticalRiskVO):
            self._vertical_risk = value
        else:
            self._vertical_risk = ShipVerticalRiskVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.custom_ship_quality_flag:
            if hasattr(self.custom_ship_quality_flag, 'to_alipay_dict'):
                params['custom_ship_quality_flag'] = self.custom_ship_quality_flag.to_alipay_dict()
            else:
                params['custom_ship_quality_flag'] = self.custom_ship_quality_flag
        if self.error_reason:
            if hasattr(self.error_reason, 'to_alipay_dict'):
                params['error_reason'] = self.error_reason.to_alipay_dict()
            else:
                params['error_reason'] = self.error_reason
        if self.ship_advice:
            if hasattr(self.ship_advice, 'to_alipay_dict'):
                params['ship_advice'] = self.ship_advice.to_alipay_dict()
            else:
                params['ship_advice'] = self.ship_advice
        if self.ship_assessment_results_level:
            if hasattr(self.ship_assessment_results_level, 'to_alipay_dict'):
                params['ship_assessment_results_level'] = self.ship_assessment_results_level.to_alipay_dict()
            else:
                params['ship_assessment_results_level'] = self.ship_assessment_results_level
        if self.ship_comprehensive_risk_level:
            if hasattr(self.ship_comprehensive_risk_level, 'to_alipay_dict'):
                params['ship_comprehensive_risk_level'] = self.ship_comprehensive_risk_level.to_alipay_dict()
            else:
                params['ship_comprehensive_risk_level'] = self.ship_comprehensive_risk_level
        if self.ship_quality_flag:
            if hasattr(self.ship_quality_flag, 'to_alipay_dict'):
                params['ship_quality_flag'] = self.ship_quality_flag.to_alipay_dict()
            else:
                params['ship_quality_flag'] = self.ship_quality_flag
        if self.vertical_risk:
            if hasattr(self.vertical_risk, 'to_alipay_dict'):
                params['vertical_risk'] = self.vertical_risk.to_alipay_dict()
            else:
                params['vertical_risk'] = self.vertical_risk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShipAssessmentResultVO()
        if 'custom_ship_quality_flag' in d:
            o.custom_ship_quality_flag = d['custom_ship_quality_flag']
        if 'error_reason' in d:
            o.error_reason = d['error_reason']
        if 'ship_advice' in d:
            o.ship_advice = d['ship_advice']
        if 'ship_assessment_results_level' in d:
            o.ship_assessment_results_level = d['ship_assessment_results_level']
        if 'ship_comprehensive_risk_level' in d:
            o.ship_comprehensive_risk_level = d['ship_comprehensive_risk_level']
        if 'ship_quality_flag' in d:
            o.ship_quality_flag = d['ship_quality_flag']
        if 'vertical_risk' in d:
            o.vertical_risk = d['vertical_risk']
        return o


