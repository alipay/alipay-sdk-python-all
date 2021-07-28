#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CloudbusLocation import CloudbusLocation
from alipay.aop.api.domain.CloudbusStop import CloudbusStop


class CloudbusRoute(object):

    def __init__(self):
        self._action = None
        self._direction = None
        self._line_id = None
        self._line_lon_lat = None
        self._line_name = None
        self._operation_time = None
        self._price = None
        self._stops = None

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
    def line_id(self):
        return self._line_id

    @line_id.setter
    def line_id(self, value):
        self._line_id = value
    @property
    def line_lon_lat(self):
        return self._line_lon_lat

    @line_lon_lat.setter
    def line_lon_lat(self, value):
        if isinstance(value, list):
            self._line_lon_lat = list()
            for i in value:
                if isinstance(i, CloudbusLocation):
                    self._line_lon_lat.append(i)
                else:
                    self._line_lon_lat.append(CloudbusLocation.from_alipay_dict(i))
    @property
    def line_name(self):
        return self._line_name

    @line_name.setter
    def line_name(self, value):
        self._line_name = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        if isinstance(value, list):
            self._operation_time = list()
            for i in value:
                self._operation_time.append(i)
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def stops(self):
        return self._stops

    @stops.setter
    def stops(self, value):
        if isinstance(value, list):
            self._stops = list()
            for i in value:
                if isinstance(i, CloudbusStop):
                    self._stops.append(i)
                else:
                    self._stops.append(CloudbusStop.from_alipay_dict(i))


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
        if self.line_id:
            if hasattr(self.line_id, 'to_alipay_dict'):
                params['line_id'] = self.line_id.to_alipay_dict()
            else:
                params['line_id'] = self.line_id
        if self.line_lon_lat:
            if isinstance(self.line_lon_lat, list):
                for i in range(0, len(self.line_lon_lat)):
                    element = self.line_lon_lat[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.line_lon_lat[i] = element.to_alipay_dict()
            if hasattr(self.line_lon_lat, 'to_alipay_dict'):
                params['line_lon_lat'] = self.line_lon_lat.to_alipay_dict()
            else:
                params['line_lon_lat'] = self.line_lon_lat
        if self.line_name:
            if hasattr(self.line_name, 'to_alipay_dict'):
                params['line_name'] = self.line_name.to_alipay_dict()
            else:
                params['line_name'] = self.line_name
        if self.operation_time:
            if isinstance(self.operation_time, list):
                for i in range(0, len(self.operation_time)):
                    element = self.operation_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_time[i] = element.to_alipay_dict()
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.stops:
            if isinstance(self.stops, list):
                for i in range(0, len(self.stops)):
                    element = self.stops[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stops[i] = element.to_alipay_dict()
            if hasattr(self.stops, 'to_alipay_dict'):
                params['stops'] = self.stops.to_alipay_dict()
            else:
                params['stops'] = self.stops
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudbusRoute()
        if 'action' in d:
            o.action = d['action']
        if 'direction' in d:
            o.direction = d['direction']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'line_lon_lat' in d:
            o.line_lon_lat = d['line_lon_lat']
        if 'line_name' in d:
            o.line_name = d['line_name']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'price' in d:
            o.price = d['price']
        if 'stops' in d:
            o.stops = d['stops']
        return o


