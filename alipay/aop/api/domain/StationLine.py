#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusRealtimeInfo import BusRealtimeInfo


class StationLine(object):

    def __init__(self):
        self._buses = None
        self._end_stop = None
        self._first_bus = None
        self._interval = None
        self._last_bus = None
        self._line_detail_schema = None
        self._line_id = None
        self._line_name = None
        self._real_time = None
        self._start_stop = None
        self._station_id = None
        self._station_name = None

    @property
    def buses(self):
        return self._buses

    @buses.setter
    def buses(self, value):
        if isinstance(value, BusRealtimeInfo):
            self._buses = value
        else:
            self._buses = BusRealtimeInfo.from_alipay_dict(value)
    @property
    def end_stop(self):
        return self._end_stop

    @end_stop.setter
    def end_stop(self, value):
        self._end_stop = value
    @property
    def first_bus(self):
        return self._first_bus

    @first_bus.setter
    def first_bus(self, value):
        self._first_bus = value
    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value
    @property
    def last_bus(self):
        return self._last_bus

    @last_bus.setter
    def last_bus(self, value):
        self._last_bus = value
    @property
    def line_detail_schema(self):
        return self._line_detail_schema

    @line_detail_schema.setter
    def line_detail_schema(self, value):
        self._line_detail_schema = value
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
    def real_time(self):
        return self._real_time

    @real_time.setter
    def real_time(self, value):
        self._real_time = value
    @property
    def start_stop(self):
        return self._start_stop

    @start_stop.setter
    def start_stop(self, value):
        self._start_stop = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.buses:
            if hasattr(self.buses, 'to_alipay_dict'):
                params['buses'] = self.buses.to_alipay_dict()
            else:
                params['buses'] = self.buses
        if self.end_stop:
            if hasattr(self.end_stop, 'to_alipay_dict'):
                params['end_stop'] = self.end_stop.to_alipay_dict()
            else:
                params['end_stop'] = self.end_stop
        if self.first_bus:
            if hasattr(self.first_bus, 'to_alipay_dict'):
                params['first_bus'] = self.first_bus.to_alipay_dict()
            else:
                params['first_bus'] = self.first_bus
        if self.interval:
            if hasattr(self.interval, 'to_alipay_dict'):
                params['interval'] = self.interval.to_alipay_dict()
            else:
                params['interval'] = self.interval
        if self.last_bus:
            if hasattr(self.last_bus, 'to_alipay_dict'):
                params['last_bus'] = self.last_bus.to_alipay_dict()
            else:
                params['last_bus'] = self.last_bus
        if self.line_detail_schema:
            if hasattr(self.line_detail_schema, 'to_alipay_dict'):
                params['line_detail_schema'] = self.line_detail_schema.to_alipay_dict()
            else:
                params['line_detail_schema'] = self.line_detail_schema
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
        if self.real_time:
            if hasattr(self.real_time, 'to_alipay_dict'):
                params['real_time'] = self.real_time.to_alipay_dict()
            else:
                params['real_time'] = self.real_time
        if self.start_stop:
            if hasattr(self.start_stop, 'to_alipay_dict'):
                params['start_stop'] = self.start_stop.to_alipay_dict()
            else:
                params['start_stop'] = self.start_stop
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StationLine()
        if 'buses' in d:
            o.buses = d['buses']
        if 'end_stop' in d:
            o.end_stop = d['end_stop']
        if 'first_bus' in d:
            o.first_bus = d['first_bus']
        if 'interval' in d:
            o.interval = d['interval']
        if 'last_bus' in d:
            o.last_bus = d['last_bus']
        if 'line_detail_schema' in d:
            o.line_detail_schema = d['line_detail_schema']
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'line_name' in d:
            o.line_name = d['line_name']
        if 'real_time' in d:
            o.real_time = d['real_time']
        if 'start_stop' in d:
            o.start_stop = d['start_stop']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'station_name' in d:
            o.station_name = d['station_name']
        return o


