#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargeConnectorInfo(object):

    def __init__(self):
        self._connector_id = None
        self._connector_name = None
        self._connector_type = None
        self._current = None
        self._national_standard = None
        self._power = None
        self._voltage_lower_limit = None
        self._voltage_upper_limit = None

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
    def national_standard(self):
        return self._national_standard

    @national_standard.setter
    def national_standard(self, value):
        self._national_standard = value
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value
    @property
    def voltage_lower_limit(self):
        return self._voltage_lower_limit

    @voltage_lower_limit.setter
    def voltage_lower_limit(self, value):
        self._voltage_lower_limit = value
    @property
    def voltage_upper_limit(self):
        return self._voltage_upper_limit

    @voltage_upper_limit.setter
    def voltage_upper_limit(self, value):
        self._voltage_upper_limit = value


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
        if self.national_standard:
            if hasattr(self.national_standard, 'to_alipay_dict'):
                params['national_standard'] = self.national_standard.to_alipay_dict()
            else:
                params['national_standard'] = self.national_standard
        if self.power:
            if hasattr(self.power, 'to_alipay_dict'):
                params['power'] = self.power.to_alipay_dict()
            else:
                params['power'] = self.power
        if self.voltage_lower_limit:
            if hasattr(self.voltage_lower_limit, 'to_alipay_dict'):
                params['voltage_lower_limit'] = self.voltage_lower_limit.to_alipay_dict()
            else:
                params['voltage_lower_limit'] = self.voltage_lower_limit
        if self.voltage_upper_limit:
            if hasattr(self.voltage_upper_limit, 'to_alipay_dict'):
                params['voltage_upper_limit'] = self.voltage_upper_limit.to_alipay_dict()
            else:
                params['voltage_upper_limit'] = self.voltage_upper_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargeConnectorInfo()
        if 'connector_id' in d:
            o.connector_id = d['connector_id']
        if 'connector_name' in d:
            o.connector_name = d['connector_name']
        if 'connector_type' in d:
            o.connector_type = d['connector_type']
        if 'current' in d:
            o.current = d['current']
        if 'national_standard' in d:
            o.national_standard = d['national_standard']
        if 'power' in d:
            o.power = d['power']
        if 'voltage_lower_limit' in d:
            o.voltage_lower_limit = d['voltage_lower_limit']
        if 'voltage_upper_limit' in d:
            o.voltage_upper_limit = d['voltage_upper_limit']
        return o


