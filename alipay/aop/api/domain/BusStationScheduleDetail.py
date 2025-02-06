#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusStation import BusStation


class BusStationScheduleDetail(object):

    def __init__(self):
        self._station = None
        self._station_time = None
        self._type = None

    @property
    def station(self):
        return self._station

    @station.setter
    def station(self, value):
        if isinstance(value, BusStation):
            self._station = value
        else:
            self._station = BusStation.from_alipay_dict(value)
    @property
    def station_time(self):
        return self._station_time

    @station_time.setter
    def station_time(self, value):
        self._station_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.station:
            if hasattr(self.station, 'to_alipay_dict'):
                params['station'] = self.station.to_alipay_dict()
            else:
                params['station'] = self.station
        if self.station_time:
            if hasattr(self.station_time, 'to_alipay_dict'):
                params['station_time'] = self.station_time.to_alipay_dict()
            else:
                params['station_time'] = self.station_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusStationScheduleDetail()
        if 'station' in d:
            o.station = d['station']
        if 'station_time' in d:
            o.station_time = d['station_time']
        if 'type' in d:
            o.type = d['type']
        return o


