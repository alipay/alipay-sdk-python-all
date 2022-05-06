#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargeOrderInfo(object):

    def __init__(self):
        self._connector_id = None
        self._equipment_id = None
        self._station_id = None
        self._trade_time = None

    @property
    def connector_id(self):
        return self._connector_id

    @connector_id.setter
    def connector_id(self, value):
        self._connector_id = value
    @property
    def equipment_id(self):
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, value):
        self._equipment_id = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.connector_id:
            if hasattr(self.connector_id, 'to_alipay_dict'):
                params['connector_id'] = self.connector_id.to_alipay_dict()
            else:
                params['connector_id'] = self.connector_id
        if self.equipment_id:
            if hasattr(self.equipment_id, 'to_alipay_dict'):
                params['equipment_id'] = self.equipment_id.to_alipay_dict()
            else:
                params['equipment_id'] = self.equipment_id
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargeOrderInfo()
        if 'connector_id' in d:
            o.connector_id = d['connector_id']
        if 'equipment_id' in d:
            o.equipment_id = d['equipment_id']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


