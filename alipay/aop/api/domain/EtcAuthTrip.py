#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcAuthTrip(object):

    def __init__(self):
        self._end_station_name = None
        self._end_station_time = None
        self._out_waybill_no = None
        self._pay_time = None
        self._plate_color = None
        self._plate_no = None
        self._start_station_name = None
        self._start_station_time = None
        self._sub_scene = None
        self._total_amount = None
        self._trade_id = None
        self._waybill_no = None

    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def end_station_time(self):
        return self._end_station_time

    @end_station_time.setter
    def end_station_time(self, value):
        self._end_station_time = value
    @property
    def out_waybill_no(self):
        return self._out_waybill_no

    @out_waybill_no.setter
    def out_waybill_no(self, value):
        self._out_waybill_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value
    @property
    def start_station_time(self):
        return self._start_station_time

    @start_station_time.setter
    def start_station_time(self, value):
        self._start_station_time = value
    @property
    def sub_scene(self):
        return self._sub_scene

    @sub_scene.setter
    def sub_scene(self, value):
        self._sub_scene = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.end_station_time:
            if hasattr(self.end_station_time, 'to_alipay_dict'):
                params['end_station_time'] = self.end_station_time.to_alipay_dict()
            else:
                params['end_station_time'] = self.end_station_time
        if self.out_waybill_no:
            if hasattr(self.out_waybill_no, 'to_alipay_dict'):
                params['out_waybill_no'] = self.out_waybill_no.to_alipay_dict()
            else:
                params['out_waybill_no'] = self.out_waybill_no
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        if self.start_station_time:
            if hasattr(self.start_station_time, 'to_alipay_dict'):
                params['start_station_time'] = self.start_station_time.to_alipay_dict()
            else:
                params['start_station_time'] = self.start_station_time
        if self.sub_scene:
            if hasattr(self.sub_scene, 'to_alipay_dict'):
                params['sub_scene'] = self.sub_scene.to_alipay_dict()
            else:
                params['sub_scene'] = self.sub_scene
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcAuthTrip()
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'end_station_time' in d:
            o.end_station_time = d['end_station_time']
        if 'out_waybill_no' in d:
            o.out_waybill_no = d['out_waybill_no']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'start_station_time' in d:
            o.start_station_time = d['start_station_time']
        if 'sub_scene' in d:
            o.sub_scene = d['sub_scene']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


