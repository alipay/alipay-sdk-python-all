#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportIntelligentizeOdpredictionexpCreateModel(object):

    def __init__(self):
        self._city_code = None
        self._corp_id = None
        self._ext_param = None
        self._od_prediction_service_task_id = None
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
    def od_prediction_service_task_id(self):
        return self._od_prediction_service_task_id

    @od_prediction_service_task_id.setter
    def od_prediction_service_task_id(self, value):
        self._od_prediction_service_task_id = value
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
        if self.od_prediction_service_task_id:
            if hasattr(self.od_prediction_service_task_id, 'to_alipay_dict'):
                params['od_prediction_service_task_id'] = self.od_prediction_service_task_id.to_alipay_dict()
            else:
                params['od_prediction_service_task_id'] = self.od_prediction_service_task_id
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
        o = AlipayCommerceTransportIntelligentizeOdpredictionexpCreateModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'od_prediction_service_task_id' in d:
            o.od_prediction_service_task_id = d['od_prediction_service_task_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_task_name' in d:
            o.service_task_name = d['service_task_name']
        return o


