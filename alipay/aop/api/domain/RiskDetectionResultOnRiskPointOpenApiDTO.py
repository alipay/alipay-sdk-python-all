#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskDetectionResultOnRiskRulesMapDTO import RiskDetectionResultOnRiskRulesMapDTO


class RiskDetectionResultOnRiskPointOpenApiDTO(object):

    def __init__(self):
        self._need_break = None
        self._risk_detection_result_on_risk_rules_map_dto_list = None
        self._risk_level = None
        self._risk_point_code = None

    @property
    def need_break(self):
        return self._need_break

    @need_break.setter
    def need_break(self, value):
        self._need_break = value
    @property
    def risk_detection_result_on_risk_rules_map_dto_list(self):
        return self._risk_detection_result_on_risk_rules_map_dto_list

    @risk_detection_result_on_risk_rules_map_dto_list.setter
    def risk_detection_result_on_risk_rules_map_dto_list(self, value):
        if isinstance(value, list):
            self._risk_detection_result_on_risk_rules_map_dto_list = list()
            for i in value:
                if isinstance(i, RiskDetectionResultOnRiskRulesMapDTO):
                    self._risk_detection_result_on_risk_rules_map_dto_list.append(i)
                else:
                    self._risk_detection_result_on_risk_rules_map_dto_list.append(RiskDetectionResultOnRiskRulesMapDTO.from_alipay_dict(i))
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_point_code(self):
        return self._risk_point_code

    @risk_point_code.setter
    def risk_point_code(self, value):
        self._risk_point_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_break:
            if hasattr(self.need_break, 'to_alipay_dict'):
                params['need_break'] = self.need_break.to_alipay_dict()
            else:
                params['need_break'] = self.need_break
        if self.risk_detection_result_on_risk_rules_map_dto_list:
            if isinstance(self.risk_detection_result_on_risk_rules_map_dto_list, list):
                for i in range(0, len(self.risk_detection_result_on_risk_rules_map_dto_list)):
                    element = self.risk_detection_result_on_risk_rules_map_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_detection_result_on_risk_rules_map_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_detection_result_on_risk_rules_map_dto_list, 'to_alipay_dict'):
                params['risk_detection_result_on_risk_rules_map_dto_list'] = self.risk_detection_result_on_risk_rules_map_dto_list.to_alipay_dict()
            else:
                params['risk_detection_result_on_risk_rules_map_dto_list'] = self.risk_detection_result_on_risk_rules_map_dto_list
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_point_code:
            if hasattr(self.risk_point_code, 'to_alipay_dict'):
                params['risk_point_code'] = self.risk_point_code.to_alipay_dict()
            else:
                params['risk_point_code'] = self.risk_point_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskDetectionResultOnRiskPointOpenApiDTO()
        if 'need_break' in d:
            o.need_break = d['need_break']
        if 'risk_detection_result_on_risk_rules_map_dto_list' in d:
            o.risk_detection_result_on_risk_rules_map_dto_list = d['risk_detection_result_on_risk_rules_map_dto_list']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_point_code' in d:
            o.risk_point_code = d['risk_point_code']
        return o


