#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StationInfo import StationInfo


class OdPredictionLineInfo(object):

    def __init__(self):
        self._action = None
        self._direction = None
        self._ext_param = None
        self._line_id = None
        self._line_name = None
        self._price = None
        self._service_time = None
        self._station_list = None
        self._traffic_type = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
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
    def line_name(self):
        return self._line_name

    @line_name.setter
    def line_name(self, value):
        self._line_name = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def service_time(self):
        return self._service_time

    @service_time.setter
    def service_time(self, value):
        self._service_time = value
    @property
    def station_list(self):
        return self._station_list

    @station_list.setter
    def station_list(self, value):
        if isinstance(value, list):
            self._station_list = list()
            for i in value:
                if isinstance(i, StationInfo):
                    self._station_list.append(i)
                else:
                    self._station_list.append(StationInfo.from_alipay_dict(i))
    @property
    def traffic_type(self):
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, value):
        self._traffic_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
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
        if self.line_name:
            if hasattr(self.line_name, 'to_alipay_dict'):
                params['line_name'] = self.line_name.to_alipay_dict()
            else:
                params['line_name'] = self.line_name
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.service_time:
            if hasattr(self.service_time, 'to_alipay_dict'):
                params['service_time'] = self.service_time.to_alipay_dict()
            else:
                params['service_time'] = self.service_time
        if self.station_list:
            if isinstance(self.station_list, list):
                for i in range(0, len(self.station_list)):
                    element = self.station_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.station_list[i] = element.to_alipay_dict()
            if hasattr(self.station_list, 'to_alipay_dict'):
                params['station_list'] = self.station_list.to_alipay_dict()
            else:
                params['station_list'] = self.station_list
        if self.traffic_type:
            if hasattr(self.traffic_type, 'to_alipay_dict'):
                params['traffic_type'] = self.traffic_type.to_alipay_dict()
            else:
                params['traffic_type'] = self.traffic_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OdPredictionLineInfo()
        if 'action' in d:
            o.action = d['action']
        if 'direction' in d:
            o.direction = d['direction']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'line_name' in d:
            o.line_name = d['line_name']
        if 'price' in d:
            o.price = d['price']
        if 'service_time' in d:
            o.service_time = d['service_time']
        if 'station_list' in d:
            o.station_list = d['station_list']
        if 'traffic_type' in d:
            o.traffic_type = d['traffic_type']
        return o


