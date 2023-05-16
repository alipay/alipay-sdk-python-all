#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OdPredictionLineInfo import OdPredictionLineInfo


class AlipayCommerceTransportIntelligentizeOdpredictionCreateModel(object):

    def __init__(self):
        self._city_code = None
        self._corp_id = None
        self._ext_param = None
        self._line_list = None
        self._month = None
        self._network_version = None
        self._od_predict_type = None
        self._replace = None
        self._request_id = None
        self._service_task_name = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def line_list(self):
        return self._line_list

    @line_list.setter
    def line_list(self, value):
        if isinstance(value, list):
            self._line_list = list()
            for i in value:
                if isinstance(i, OdPredictionLineInfo):
                    self._line_list.append(i)
                else:
                    self._line_list.append(OdPredictionLineInfo.from_alipay_dict(i))
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def network_version(self):
        return self._network_version

    @network_version.setter
    def network_version(self, value):
        self._network_version = value
    @property
    def od_predict_type(self):
        return self._od_predict_type

    @od_predict_type.setter
    def od_predict_type(self, value):
        self._od_predict_type = value
    @property
    def replace(self):
        return self._replace

    @replace.setter
    def replace(self, value):
        self._replace = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def service_task_name(self):
        return self._service_task_name

    @service_task_name.setter
    def service_task_name(self, value):
        self._service_task_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_list:
            if isinstance(self.line_list, list):
                for i in range(0, len(self.line_list)):
                    element = self.line_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.line_list[i] = element.to_alipay_dict()
            if hasattr(self.line_list, 'to_alipay_dict'):
                params['line_list'] = self.line_list.to_alipay_dict()
            else:
                params['line_list'] = self.line_list
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.network_version:
            if hasattr(self.network_version, 'to_alipay_dict'):
                params['network_version'] = self.network_version.to_alipay_dict()
            else:
                params['network_version'] = self.network_version
        if self.od_predict_type:
            if hasattr(self.od_predict_type, 'to_alipay_dict'):
                params['od_predict_type'] = self.od_predict_type.to_alipay_dict()
            else:
                params['od_predict_type'] = self.od_predict_type
        if self.replace:
            if hasattr(self.replace, 'to_alipay_dict'):
                params['replace'] = self.replace.to_alipay_dict()
            else:
                params['replace'] = self.replace
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.service_task_name:
            if hasattr(self.service_task_name, 'to_alipay_dict'):
                params['service_task_name'] = self.service_task_name.to_alipay_dict()
            else:
                params['service_task_name'] = self.service_task_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIntelligentizeOdpredictionCreateModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_list' in d:
            o.line_list = d['line_list']
        if 'month' in d:
            o.month = d['month']
        if 'network_version' in d:
            o.network_version = d['network_version']
        if 'od_predict_type' in d:
            o.od_predict_type = d['od_predict_type']
        if 'replace' in d:
            o.replace = d['replace']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_task_name' in d:
            o.service_task_name = d['service_task_name']
        return o


