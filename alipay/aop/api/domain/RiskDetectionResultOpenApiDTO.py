#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskDetectionResultOnRiskPointOpenApiDTO import RiskDetectionResultOnRiskPointOpenApiDTO


class RiskDetectionResultOpenApiDTO(object):

    def __init__(self):
        self._document_no = None
        self._document_type = None
        self._need_break = None
        self._risk_detection_result_on_risk_point_open_api_dtos = None
        self._risk_level = None
        self._second_level_business_link = None

    @property
    def document_no(self):
        return self._document_no

    @document_no.setter
    def document_no(self, value):
        self._document_no = value
    @property
    def document_type(self):
        return self._document_type

    @document_type.setter
    def document_type(self, value):
        self._document_type = value
    @property
    def need_break(self):
        return self._need_break

    @need_break.setter
    def need_break(self, value):
        self._need_break = value
    @property
    def risk_detection_result_on_risk_point_open_api_dtos(self):
        return self._risk_detection_result_on_risk_point_open_api_dtos

    @risk_detection_result_on_risk_point_open_api_dtos.setter
    def risk_detection_result_on_risk_point_open_api_dtos(self, value):
        if isinstance(value, list):
            self._risk_detection_result_on_risk_point_open_api_dtos = list()
            for i in value:
                if isinstance(i, RiskDetectionResultOnRiskPointOpenApiDTO):
                    self._risk_detection_result_on_risk_point_open_api_dtos.append(i)
                else:
                    self._risk_detection_result_on_risk_point_open_api_dtos.append(RiskDetectionResultOnRiskPointOpenApiDTO.from_alipay_dict(i))
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def second_level_business_link(self):
        return self._second_level_business_link

    @second_level_business_link.setter
    def second_level_business_link(self, value):
        self._second_level_business_link = value


    def to_alipay_dict(self):
        params = dict()
        if self.document_no:
            if hasattr(self.document_no, 'to_alipay_dict'):
                params['document_no'] = self.document_no.to_alipay_dict()
            else:
                params['document_no'] = self.document_no
        if self.document_type:
            if hasattr(self.document_type, 'to_alipay_dict'):
                params['document_type'] = self.document_type.to_alipay_dict()
            else:
                params['document_type'] = self.document_type
        if self.need_break:
            if hasattr(self.need_break, 'to_alipay_dict'):
                params['need_break'] = self.need_break.to_alipay_dict()
            else:
                params['need_break'] = self.need_break
        if self.risk_detection_result_on_risk_point_open_api_dtos:
            if isinstance(self.risk_detection_result_on_risk_point_open_api_dtos, list):
                for i in range(0, len(self.risk_detection_result_on_risk_point_open_api_dtos)):
                    element = self.risk_detection_result_on_risk_point_open_api_dtos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_detection_result_on_risk_point_open_api_dtos[i] = element.to_alipay_dict()
            if hasattr(self.risk_detection_result_on_risk_point_open_api_dtos, 'to_alipay_dict'):
                params['risk_detection_result_on_risk_point_open_api_dtos'] = self.risk_detection_result_on_risk_point_open_api_dtos.to_alipay_dict()
            else:
                params['risk_detection_result_on_risk_point_open_api_dtos'] = self.risk_detection_result_on_risk_point_open_api_dtos
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.second_level_business_link:
            if hasattr(self.second_level_business_link, 'to_alipay_dict'):
                params['second_level_business_link'] = self.second_level_business_link.to_alipay_dict()
            else:
                params['second_level_business_link'] = self.second_level_business_link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskDetectionResultOpenApiDTO()
        if 'document_no' in d:
            o.document_no = d['document_no']
        if 'document_type' in d:
            o.document_type = d['document_type']
        if 'need_break' in d:
            o.need_break = d['need_break']
        if 'risk_detection_result_on_risk_point_open_api_dtos' in d:
            o.risk_detection_result_on_risk_point_open_api_dtos = d['risk_detection_result_on_risk_point_open_api_dtos']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'second_level_business_link' in d:
            o.second_level_business_link = d['second_level_business_link']
        return o


