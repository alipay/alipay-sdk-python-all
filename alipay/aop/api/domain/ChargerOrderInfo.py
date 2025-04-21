#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargerOrderInfo(object):

    def __init__(self):
        self._charging_end_time = None
        self._charging_start_time = None
        self._connector_id = None
        self._elec_amount = None
        self._out_trade_no = None
        self._power = None
        self._service_amount = None
        self._station_id = None
        self._total_amount = None

    @property
    def charging_end_time(self):
        return self._charging_end_time

    @charging_end_time.setter
    def charging_end_time(self, value):
        self._charging_end_time = value
    @property
    def charging_start_time(self):
        return self._charging_start_time

    @charging_start_time.setter
    def charging_start_time(self, value):
        self._charging_start_time = value
    @property
    def connector_id(self):
        return self._connector_id

    @connector_id.setter
    def connector_id(self, value):
        self._connector_id = value
    @property
    def elec_amount(self):
        return self._elec_amount

    @elec_amount.setter
    def elec_amount(self, value):
        self._elec_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.charging_end_time:
            if hasattr(self.charging_end_time, 'to_alipay_dict'):
                params['charging_end_time'] = self.charging_end_time.to_alipay_dict()
            else:
                params['charging_end_time'] = self.charging_end_time
        if self.charging_start_time:
            if hasattr(self.charging_start_time, 'to_alipay_dict'):
                params['charging_start_time'] = self.charging_start_time.to_alipay_dict()
            else:
                params['charging_start_time'] = self.charging_start_time
        if self.connector_id:
            if hasattr(self.connector_id, 'to_alipay_dict'):
                params['connector_id'] = self.connector_id.to_alipay_dict()
            else:
                params['connector_id'] = self.connector_id
        if self.elec_amount:
            if hasattr(self.elec_amount, 'to_alipay_dict'):
                params['elec_amount'] = self.elec_amount.to_alipay_dict()
            else:
                params['elec_amount'] = self.elec_amount
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.power:
            if hasattr(self.power, 'to_alipay_dict'):
                params['power'] = self.power.to_alipay_dict()
            else:
                params['power'] = self.power
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
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
        o = ChargerOrderInfo()
        if 'charging_end_time' in d:
            o.charging_end_time = d['charging_end_time']
        if 'charging_start_time' in d:
            o.charging_start_time = d['charging_start_time']
        if 'connector_id' in d:
            o.connector_id = d['connector_id']
        if 'elec_amount' in d:
            o.elec_amount = d['elec_amount']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'power' in d:
            o.power = d['power']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


