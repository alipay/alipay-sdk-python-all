#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusRealtimeInfo(object):

    def __init__(self):
        self._line_id = None
        self._line_name = None
        self._seconds_left = None
        self._station_id = None
        self._station_left = None
        self._station_name = None
        self._sub_status = None
        self._sub_text = None

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
    def seconds_left(self):
        return self._seconds_left

    @seconds_left.setter
    def seconds_left(self, value):
        self._seconds_left = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def station_left(self):
        return self._station_left

    @station_left.setter
    def station_left(self, value):
        self._station_left = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
    @property
    def sub_text(self):
        return self._sub_text

    @sub_text.setter
    def sub_text(self, value):
        self._sub_text = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.seconds_left:
            if hasattr(self.seconds_left, 'to_alipay_dict'):
                params['seconds_left'] = self.seconds_left.to_alipay_dict()
            else:
                params['seconds_left'] = self.seconds_left
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.station_left:
            if hasattr(self.station_left, 'to_alipay_dict'):
                params['station_left'] = self.station_left.to_alipay_dict()
            else:
                params['station_left'] = self.station_left
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
        if self.sub_text:
            if hasattr(self.sub_text, 'to_alipay_dict'):
                params['sub_text'] = self.sub_text.to_alipay_dict()
            else:
                params['sub_text'] = self.sub_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusRealtimeInfo()
        if 'line_id' in d:
            o.line_id = d['line_id']
        if 'line_name' in d:
            o.line_name = d['line_name']
        if 'seconds_left' in d:
            o.seconds_left = d['seconds_left']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'station_left' in d:
            o.station_left = d['station_left']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        if 'sub_text' in d:
            o.sub_text = d['sub_text']
        return o


