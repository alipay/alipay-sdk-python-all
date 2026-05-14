#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PubApiConnectorInfo(object):

    def __init__(self):
        self._connector_id = None
        self._connector_name = None
        self._connector_status = None
        self._connector_type = None
        self._current = None
        self._park_no = None
        self._power = None
        self._station_charger_type = None
        self._voltage_lower_limits = None
        self._voltage_upper_limits = None

    @property
    def connector_id(self):
        return self._connector_id

    @connector_id.setter
    def connector_id(self, value):
        self._connector_id = value
    @property
    def connector_name(self):
        return self._connector_name

    @connector_name.setter
    def connector_name(self, value):
        self._connector_name = value
    @property
    def connector_status(self):
        return self._connector_status

    @connector_status.setter
    def connector_status(self, value):
        self._connector_status = value
    @property
    def connector_type(self):
        return self._connector_type

    @connector_type.setter
    def connector_type(self, value):
        self._connector_type = value
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def park_no(self):
        return self._park_no

    @park_no.setter
    def park_no(self, value):
        self._park_no = value
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value
    @property
    def station_charger_type(self):
        return self._station_charger_type

    @station_charger_type.setter
    def station_charger_type(self, value):
        self._station_charger_type = value
    @property
    def voltage_lower_limits(self):
        return self._voltage_lower_limits

    @voltage_lower_limits.setter
    def voltage_lower_limits(self, value):
        self._voltage_lower_limits = value
    @property
    def voltage_upper_limits(self):
        return self._voltage_upper_limits

    @voltage_upper_limits.setter
    def voltage_upper_limits(self, value):
        self._voltage_upper_limits = value


    def to_alipay_dict(self):
        params = dict()
        if self.connector_id:
            if hasattr(self.connector_id, 'to_alipay_dict'):
                params['connector_id'] = self.connector_id.to_alipay_dict()
            else:
                params['connector_id'] = self.connector_id
        if self.connector_name:
            if hasattr(self.connector_name, 'to_alipay_dict'):
                params['connector_name'] = self.connector_name.to_alipay_dict()
            else:
                params['connector_name'] = self.connector_name
        if self.connector_status:
            if hasattr(self.connector_status, 'to_alipay_dict'):
                params['connector_status'] = self.connector_status.to_alipay_dict()
            else:
                params['connector_status'] = self.connector_status
        if self.connector_type:
            if hasattr(self.connector_type, 'to_alipay_dict'):
                params['connector_type'] = self.connector_type.to_alipay_dict()
            else:
                params['connector_type'] = self.connector_type
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.park_no:
            if hasattr(self.park_no, 'to_alipay_dict'):
                params['park_no'] = self.park_no.to_alipay_dict()
            else:
                params['park_no'] = self.park_no
        if self.power:
            if hasattr(self.power, 'to_alipay_dict'):
                params['power'] = self.power.to_alipay_dict()
            else:
                params['power'] = self.power
        if self.station_charger_type:
            if hasattr(self.station_charger_type, 'to_alipay_dict'):
                params['station_charger_type'] = self.station_charger_type.to_alipay_dict()
            else:
                params['station_charger_type'] = self.station_charger_type
        if self.voltage_lower_limits:
            if hasattr(self.voltage_lower_limits, 'to_alipay_dict'):
                params['voltage_lower_limits'] = self.voltage_lower_limits.to_alipay_dict()
            else:
                params['voltage_lower_limits'] = self.voltage_lower_limits
        if self.voltage_upper_limits:
            if hasattr(self.voltage_upper_limits, 'to_alipay_dict'):
                params['voltage_upper_limits'] = self.voltage_upper_limits.to_alipay_dict()
            else:
                params['voltage_upper_limits'] = self.voltage_upper_limits
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PubApiConnectorInfo()
        if 'connector_id' in d:
            o.connector_id = d['connector_id']
        if 'connector_name' in d:
            o.connector_name = d['connector_name']
        if 'connector_status' in d:
            o.connector_status = d['connector_status']
        if 'connector_type' in d:
            o.connector_type = d['connector_type']
        if 'current' in d:
            o.current = d['current']
        if 'park_no' in d:
            o.park_no = d['park_no']
        if 'power' in d:
            o.power = d['power']
        if 'station_charger_type' in d:
            o.station_charger_type = d['station_charger_type']
        if 'voltage_lower_limits' in d:
            o.voltage_lower_limits = d['voltage_lower_limits']
        if 'voltage_upper_limits' in d:
            o.voltage_upper_limits = d['voltage_upper_limits']
        return o


