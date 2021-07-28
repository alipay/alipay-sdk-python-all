#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CloudbusLocation import CloudbusLocation
from alipay.aop.api.domain.CloudbusStop import CloudbusStop


class CloudbusPredictRItem(object):

    def __init__(self):
        self._line_lon_lat = None
        self._operation_time = None
        self._route_volume = None
        self._stops = None

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
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        if isinstance(value, list):
            self._operation_time = list()
            for i in value:
                self._operation_time.append(i)
    @property
    def route_volume(self):
        return self._route_volume

    @route_volume.setter
    def route_volume(self, value):
        self._route_volume = value
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
        if self.route_volume:
            if hasattr(self.route_volume, 'to_alipay_dict'):
                params['route_volume'] = self.route_volume.to_alipay_dict()
            else:
                params['route_volume'] = self.route_volume
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
        o = CloudbusPredictRItem()
        if 'line_lon_lat' in d:
            o.line_lon_lat = d['line_lon_lat']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'route_volume' in d:
            o.route_volume = d['route_volume']
        if 'stops' in d:
            o.stops = d['stops']
        return o


