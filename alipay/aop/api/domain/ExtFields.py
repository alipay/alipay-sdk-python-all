#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtFields(object):

    def __init__(self):
        self._destination_station_id = None
        self._end_line = None
        self._origin_station_id = None

    @property
    def destination_station_id(self):
        return self._destination_station_id

    @destination_station_id.setter
    def destination_station_id(self, value):
        self._destination_station_id = value
    @property
    def end_line(self):
        return self._end_line

    @end_line.setter
    def end_line(self, value):
        self._end_line = value
    @property
    def origin_station_id(self):
        return self._origin_station_id

    @origin_station_id.setter
    def origin_station_id(self, value):
        self._origin_station_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.destination_station_id:
            if hasattr(self.destination_station_id, 'to_alipay_dict'):
                params['destination_station_id'] = self.destination_station_id.to_alipay_dict()
            else:
                params['destination_station_id'] = self.destination_station_id
        if self.end_line:
            if hasattr(self.end_line, 'to_alipay_dict'):
                params['end_line'] = self.end_line.to_alipay_dict()
            else:
                params['end_line'] = self.end_line
        if self.origin_station_id:
            if hasattr(self.origin_station_id, 'to_alipay_dict'):
                params['origin_station_id'] = self.origin_station_id.to_alipay_dict()
            else:
                params['origin_station_id'] = self.origin_station_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtFields()
        if 'destination_station_id' in d:
            o.destination_station_id = d['destination_station_id']
        if 'end_line' in d:
            o.end_line = d['end_line']
        if 'origin_station_id' in d:
            o.origin_station_id = d['origin_station_id']
        return o


