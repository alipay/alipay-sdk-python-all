#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAnalysisCommonRequest import OpenApiAnalysisCommonRequest


class AlipayCloudCloudpromoAnalysistrafficSourcetrendQueryModel(object):

    def __init__(self):
        self._common_request = None
        self._first_source_type = None
        self._second_source_type = None

    @property
    def common_request(self):
        return self._common_request

    @common_request.setter
    def common_request(self, value):
        if isinstance(value, OpenApiAnalysisCommonRequest):
            self._common_request = value
        else:
            self._common_request = OpenApiAnalysisCommonRequest.from_alipay_dict(value)
    @property
    def first_source_type(self):
        return self._first_source_type

    @first_source_type.setter
    def first_source_type(self, value):
        if isinstance(value, list):
            self._first_source_type = list()
            for i in value:
                self._first_source_type.append(i)
    @property
    def second_source_type(self):
        return self._second_source_type

    @second_source_type.setter
    def second_source_type(self, value):
        if isinstance(value, list):
            self._second_source_type = list()
            for i in value:
                self._second_source_type.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.common_request:
            if hasattr(self.common_request, 'to_alipay_dict'):
                params['common_request'] = self.common_request.to_alipay_dict()
            else:
                params['common_request'] = self.common_request
        if self.first_source_type:
            if isinstance(self.first_source_type, list):
                for i in range(0, len(self.first_source_type)):
                    element = self.first_source_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.first_source_type[i] = element.to_alipay_dict()
            if hasattr(self.first_source_type, 'to_alipay_dict'):
                params['first_source_type'] = self.first_source_type.to_alipay_dict()
            else:
                params['first_source_type'] = self.first_source_type
        if self.second_source_type:
            if isinstance(self.second_source_type, list):
                for i in range(0, len(self.second_source_type)):
                    element = self.second_source_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.second_source_type[i] = element.to_alipay_dict()
            if hasattr(self.second_source_type, 'to_alipay_dict'):
                params['second_source_type'] = self.second_source_type.to_alipay_dict()
            else:
                params['second_source_type'] = self.second_source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAnalysistrafficSourcetrendQueryModel()
        if 'common_request' in d:
            o.common_request = d['common_request']
        if 'first_source_type' in d:
            o.first_source_type = d['first_source_type']
        if 'second_source_type' in d:
            o.second_source_type = d['second_source_type']
        return o


