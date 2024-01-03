#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcTripInfo(object):

    def __init__(self):
        self._end_station_name = None
        self._out_order_id = None
        self._start_station_name = None
        self._sub_scene = None
        self._sub_type = None
        self._total_amount = None
        self._trade_no = None
        self._trip_end_time = None
        self._trip_id = None
        self._trip_start_time = None

    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value
    @property
    def sub_scene(self):
        return self._sub_scene

    @sub_scene.setter
    def sub_scene(self, value):
        self._sub_scene = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trip_end_time(self):
        return self._trip_end_time

    @trip_end_time.setter
    def trip_end_time(self, value):
        self._trip_end_time = value
    @property
    def trip_id(self):
        return self._trip_id

    @trip_id.setter
    def trip_id(self, value):
        self._trip_id = value
    @property
    def trip_start_time(self):
        return self._trip_start_time

    @trip_start_time.setter
    def trip_start_time(self, value):
        self._trip_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        if self.sub_scene:
            if hasattr(self.sub_scene, 'to_alipay_dict'):
                params['sub_scene'] = self.sub_scene.to_alipay_dict()
            else:
                params['sub_scene'] = self.sub_scene
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trip_end_time:
            if hasattr(self.trip_end_time, 'to_alipay_dict'):
                params['trip_end_time'] = self.trip_end_time.to_alipay_dict()
            else:
                params['trip_end_time'] = self.trip_end_time
        if self.trip_id:
            if hasattr(self.trip_id, 'to_alipay_dict'):
                params['trip_id'] = self.trip_id.to_alipay_dict()
            else:
                params['trip_id'] = self.trip_id
        if self.trip_start_time:
            if hasattr(self.trip_start_time, 'to_alipay_dict'):
                params['trip_start_time'] = self.trip_start_time.to_alipay_dict()
            else:
                params['trip_start_time'] = self.trip_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcTripInfo()
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'sub_scene' in d:
            o.sub_scene = d['sub_scene']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trip_end_time' in d:
            o.trip_end_time = d['trip_end_time']
        if 'trip_id' in d:
            o.trip_id = d['trip_id']
        if 'trip_start_time' in d:
            o.trip_start_time = d['trip_start_time']
        return o


