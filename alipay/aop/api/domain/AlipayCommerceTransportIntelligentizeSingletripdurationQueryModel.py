#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportIntelligentizeSingletripdurationQueryModel(object):

    def __init__(self):
        self._aggregate_type = None
        self._city_code = None
        self._corp_id = None
        self._direction = None
        self._ext_param = None
        self._line_id = None
        self._line_key = None
        self._request_id = None
        self._time_span = None

    @property
    def aggregate_type(self):
        return self._aggregate_type

    @aggregate_type.setter
    def aggregate_type(self, value):
        self._aggregate_type = value
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
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def line_key(self):
        return self._line_key

    @line_key.setter
    def line_key(self, value):
        self._line_key = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def time_span(self):
        return self._time_span

    @time_span.setter
    def time_span(self, value):
        self._time_span = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggregate_type:
            if hasattr(self.aggregate_type, 'to_alipay_dict'):
                params['aggregate_type'] = self.aggregate_type.to_alipay_dict()
            else:
                params['aggregate_type'] = self.aggregate_type
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
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.line_key:
            if hasattr(self.line_key, 'to_alipay_dict'):
                params['line_key'] = self.line_key.to_alipay_dict()
            else:
                params['line_key'] = self.line_key
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.time_span:
            if hasattr(self.time_span, 'to_alipay_dict'):
                params['time_span'] = self.time_span.to_alipay_dict()
            else:
                params['time_span'] = self.time_span
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIntelligentizeSingletripdurationQueryModel()
        if 'aggregate_type' in d:
            o.aggregate_type = d['aggregate_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'direction' in d:
            o.direction = d['direction']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'line_key' in d:
            o.line_key = d['line_key']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'time_span' in d:
            o.time_span = d['time_span']
        return o


