#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcInoviceRepeatTradeList(object):

    def __init__(self):
        self._allowance = None
        self._consumer_trans_type = None
        self._end_station_name = None
        self._end_time = None
        self._invoice_progress_status = None
        self._plate_color = None
        self._plate_no = None
        self._start_station_name = None
        self._start_time = None
        self._total_amount = None

    @property
    def allowance(self):
        return self._allowance

    @allowance.setter
    def allowance(self, value):
        self._allowance = value
    @property
    def consumer_trans_type(self):
        return self._consumer_trans_type

    @consumer_trans_type.setter
    def consumer_trans_type(self, value):
        self._consumer_trans_type = value
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
    def invoice_progress_status(self):
        return self._invoice_progress_status

    @invoice_progress_status.setter
    def invoice_progress_status(self, value):
        self._invoice_progress_status = value
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
        if self.allowance:
            if hasattr(self.allowance, 'to_alipay_dict'):
                params['allowance'] = self.allowance.to_alipay_dict()
            else:
                params['allowance'] = self.allowance
        if self.consumer_trans_type:
            if hasattr(self.consumer_trans_type, 'to_alipay_dict'):
                params['consumer_trans_type'] = self.consumer_trans_type.to_alipay_dict()
            else:
                params['consumer_trans_type'] = self.consumer_trans_type
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
        if self.invoice_progress_status:
            if hasattr(self.invoice_progress_status, 'to_alipay_dict'):
                params['invoice_progress_status'] = self.invoice_progress_status.to_alipay_dict()
            else:
                params['invoice_progress_status'] = self.invoice_progress_status
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
        o = EtcInoviceRepeatTradeList()
        if 'allowance' in d:
            o.allowance = d['allowance']
        if 'consumer_trans_type' in d:
            o.consumer_trans_type = d['consumer_trans_type']
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'invoice_progress_status' in d:
            o.invoice_progress_status = d['invoice_progress_status']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


