#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Area import Area


class AlipayCommerceTransportIntelligentizeFlowodanalysCreateModel(object):

    def __init__(self):
        self._area_city = None
        self._area_code = None
        self._area_selected = None
        self._city_code = None
        self._corp_id = None
        self._cross_city = None
        self._crowd_label = None
        self._data_month = None
        self._data_time = None
        self._ext_param = None
        self._flow_od_analysis_task_type = None
        self._line_name = None
        self._pattern = None
        self._precision = None
        self._request_id = None
        self._service_task_name = None
        self._station_name = None
        self._time_division = None
        self._traffic_type = None
        self._trans_type = None

    @property
    def area_city(self):
        return self._area_city

    @area_city.setter
    def area_city(self, value):
        self._area_city = value
    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def area_selected(self):
        return self._area_selected

    @area_selected.setter
    def area_selected(self, value):
        if isinstance(value, Area):
            self._area_selected = value
        else:
            self._area_selected = Area.from_alipay_dict(value)
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
    def cross_city(self):
        return self._cross_city

    @cross_city.setter
    def cross_city(self, value):
        self._cross_city = value
    @property
    def crowd_label(self):
        return self._crowd_label

    @crowd_label.setter
    def crowd_label(self, value):
        self._crowd_label = value
    @property
    def data_month(self):
        return self._data_month

    @data_month.setter
    def data_month(self, value):
        self._data_month = value
    @property
    def data_time(self):
        return self._data_time

    @data_time.setter
    def data_time(self, value):
        self._data_time = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def flow_od_analysis_task_type(self):
        return self._flow_od_analysis_task_type

    @flow_od_analysis_task_type.setter
    def flow_od_analysis_task_type(self, value):
        self._flow_od_analysis_task_type = value
    @property
    def line_name(self):
        return self._line_name

    @line_name.setter
    def line_name(self, value):
        self._line_name = value
    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        self._pattern = value
    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        self._precision = value
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
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def time_division(self):
        return self._time_division

    @time_division.setter
    def time_division(self, value):
        self._time_division = value
    @property
    def traffic_type(self):
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, value):
        self._traffic_type = value
    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_city:
            if hasattr(self.area_city, 'to_alipay_dict'):
                params['area_city'] = self.area_city.to_alipay_dict()
            else:
                params['area_city'] = self.area_city
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.area_selected:
            if hasattr(self.area_selected, 'to_alipay_dict'):
                params['area_selected'] = self.area_selected.to_alipay_dict()
            else:
                params['area_selected'] = self.area_selected
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
        if self.cross_city:
            if hasattr(self.cross_city, 'to_alipay_dict'):
                params['cross_city'] = self.cross_city.to_alipay_dict()
            else:
                params['cross_city'] = self.cross_city
        if self.crowd_label:
            if hasattr(self.crowd_label, 'to_alipay_dict'):
                params['crowd_label'] = self.crowd_label.to_alipay_dict()
            else:
                params['crowd_label'] = self.crowd_label
        if self.data_month:
            if hasattr(self.data_month, 'to_alipay_dict'):
                params['data_month'] = self.data_month.to_alipay_dict()
            else:
                params['data_month'] = self.data_month
        if self.data_time:
            if hasattr(self.data_time, 'to_alipay_dict'):
                params['data_time'] = self.data_time.to_alipay_dict()
            else:
                params['data_time'] = self.data_time
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.flow_od_analysis_task_type:
            if hasattr(self.flow_od_analysis_task_type, 'to_alipay_dict'):
                params['flow_od_analysis_task_type'] = self.flow_od_analysis_task_type.to_alipay_dict()
            else:
                params['flow_od_analysis_task_type'] = self.flow_od_analysis_task_type
        if self.line_name:
            if hasattr(self.line_name, 'to_alipay_dict'):
                params['line_name'] = self.line_name.to_alipay_dict()
            else:
                params['line_name'] = self.line_name
        if self.pattern:
            if hasattr(self.pattern, 'to_alipay_dict'):
                params['pattern'] = self.pattern.to_alipay_dict()
            else:
                params['pattern'] = self.pattern
        if self.precision:
            if hasattr(self.precision, 'to_alipay_dict'):
                params['precision'] = self.precision.to_alipay_dict()
            else:
                params['precision'] = self.precision
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
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        if self.time_division:
            if hasattr(self.time_division, 'to_alipay_dict'):
                params['time_division'] = self.time_division.to_alipay_dict()
            else:
                params['time_division'] = self.time_division
        if self.traffic_type:
            if hasattr(self.traffic_type, 'to_alipay_dict'):
                params['traffic_type'] = self.traffic_type.to_alipay_dict()
            else:
                params['traffic_type'] = self.traffic_type
        if self.trans_type:
            if hasattr(self.trans_type, 'to_alipay_dict'):
                params['trans_type'] = self.trans_type.to_alipay_dict()
            else:
                params['trans_type'] = self.trans_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIntelligentizeFlowodanalysCreateModel()
        if 'area_city' in d:
            o.area_city = d['area_city']
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'area_selected' in d:
            o.area_selected = d['area_selected']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'cross_city' in d:
            o.cross_city = d['cross_city']
        if 'crowd_label' in d:
            o.crowd_label = d['crowd_label']
        if 'data_month' in d:
            o.data_month = d['data_month']
        if 'data_time' in d:
            o.data_time = d['data_time']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'flow_od_analysis_task_type' in d:
            o.flow_od_analysis_task_type = d['flow_od_analysis_task_type']
        if 'line_name' in d:
            o.line_name = d['line_name']
        if 'pattern' in d:
            o.pattern = d['pattern']
        if 'precision' in d:
            o.precision = d['precision']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_task_name' in d:
            o.service_task_name = d['service_task_name']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'time_division' in d:
            o.time_division = d['time_division']
        if 'traffic_type' in d:
            o.traffic_type = d['traffic_type']
        if 'trans_type' in d:
            o.trans_type = d['trans_type']
        return o


