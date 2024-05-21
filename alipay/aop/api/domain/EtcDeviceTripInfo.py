#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcDeviceTripInfo(object):

    def __init__(self):
        self._biz_no = None
        self._end_station_id_hex = None
        self._end_time = None
        self._start_station_id_hex = None
        self._start_time = None
        self._total_amount = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def end_station_id_hex(self):
        return self._end_station_id_hex

    @end_station_id_hex.setter
    def end_station_id_hex(self, value):
        self._end_station_id_hex = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def start_station_id_hex(self):
        return self._start_station_id_hex

    @start_station_id_hex.setter
    def start_station_id_hex(self, value):
        self._start_station_id_hex = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.end_station_id_hex:
            if hasattr(self.end_station_id_hex, 'to_alipay_dict'):
                params['end_station_id_hex'] = self.end_station_id_hex.to_alipay_dict()
            else:
                params['end_station_id_hex'] = self.end_station_id_hex
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.start_station_id_hex:
            if hasattr(self.start_station_id_hex, 'to_alipay_dict'):
                params['start_station_id_hex'] = self.start_station_id_hex.to_alipay_dict()
            else:
                params['start_station_id_hex'] = self.start_station_id_hex
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcDeviceTripInfo()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'end_station_id_hex' in d:
            o.end_station_id_hex = d['end_station_id_hex']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'start_station_id_hex' in d:
            o.start_station_id_hex = d['start_station_id_hex']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


