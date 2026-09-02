#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportExpresswayCardtripSyncModel(object):

    def __init__(self):
        self._biz_time = None
        self._end_station_name = None
        self._end_time = None
        self._isv_id = None
        self._out_biz_no = None
        self._out_trip_id = None
        self._pay_type = None
        self._plate_color = None
        self._plate_no = None
        self._service_url = None
        self._start_station_name = None
        self._start_time = None
        self._total_amount = None
        self._trade_no = None
        self._trade_status = None
        self._trip_id = None
        self._trip_status = None
        self._user_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_trip_id(self):
        return self._out_trip_id

    @out_trip_id.setter
    def out_trip_id(self, value):
        self._out_trip_id = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
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
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
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
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trip_id(self):
        return self._trip_id

    @trip_id.setter
    def trip_id(self, value):
        self._trip_id = value
    @property
    def trip_status(self):
        return self._trip_status

    @trip_status.setter
    def trip_status(self, value):
        self._trip_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.isv_id:
            if hasattr(self.isv_id, 'to_alipay_dict'):
                params['isv_id'] = self.isv_id.to_alipay_dict()
            else:
                params['isv_id'] = self.isv_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_trip_id:
            if hasattr(self.out_trip_id, 'to_alipay_dict'):
                params['out_trip_id'] = self.out_trip_id.to_alipay_dict()
            else:
                params['out_trip_id'] = self.out_trip_id
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
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
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        if self.trade_status:
            if hasattr(self.trade_status, 'to_alipay_dict'):
                params['trade_status'] = self.trade_status.to_alipay_dict()
            else:
                params['trade_status'] = self.trade_status
        if self.trip_id:
            if hasattr(self.trip_id, 'to_alipay_dict'):
                params['trip_id'] = self.trip_id.to_alipay_dict()
            else:
                params['trip_id'] = self.trip_id
        if self.trip_status:
            if hasattr(self.trip_status, 'to_alipay_dict'):
                params['trip_status'] = self.trip_status.to_alipay_dict()
            else:
                params['trip_status'] = self.trip_status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportExpresswayCardtripSyncModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'isv_id' in d:
            o.isv_id = d['isv_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_trip_id' in d:
            o.out_trip_id = d['out_trip_id']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'service_url' in d:
            o.service_url = d['service_url']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_status' in d:
            o.trade_status = d['trade_status']
        if 'trip_id' in d:
            o.trip_id = d['trip_id']
        if 'trip_status' in d:
            o.trip_status = d['trip_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


