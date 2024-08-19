#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechAppcoreTemperaturecontrolSubmitModel(object):

    def __init__(self):
        self._company_uscc = None
        self._heating_mode = None
        self._open_id = None
        self._resident_id = None
        self._room_temperature = None
        self._set_temperature = None
        self._set_time = None
        self._user_id = None

    @property
    def company_uscc(self):
        return self._company_uscc

    @company_uscc.setter
    def company_uscc(self, value):
        self._company_uscc = value
    @property
    def heating_mode(self):
        return self._heating_mode

    @heating_mode.setter
    def heating_mode(self, value):
        self._heating_mode = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def resident_id(self):
        return self._resident_id

    @resident_id.setter
    def resident_id(self, value):
        self._resident_id = value
    @property
    def room_temperature(self):
        return self._room_temperature

    @room_temperature.setter
    def room_temperature(self, value):
        self._room_temperature = value
    @property
    def set_temperature(self):
        return self._set_temperature

    @set_temperature.setter
    def set_temperature(self, value):
        self._set_temperature = value
    @property
    def set_time(self):
        return self._set_time

    @set_time.setter
    def set_time(self, value):
        self._set_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_uscc:
            if hasattr(self.company_uscc, 'to_alipay_dict'):
                params['company_uscc'] = self.company_uscc.to_alipay_dict()
            else:
                params['company_uscc'] = self.company_uscc
        if self.heating_mode:
            if hasattr(self.heating_mode, 'to_alipay_dict'):
                params['heating_mode'] = self.heating_mode.to_alipay_dict()
            else:
                params['heating_mode'] = self.heating_mode
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.resident_id:
            if hasattr(self.resident_id, 'to_alipay_dict'):
                params['resident_id'] = self.resident_id.to_alipay_dict()
            else:
                params['resident_id'] = self.resident_id
        if self.room_temperature:
            if hasattr(self.room_temperature, 'to_alipay_dict'):
                params['room_temperature'] = self.room_temperature.to_alipay_dict()
            else:
                params['room_temperature'] = self.room_temperature
        if self.set_temperature:
            if hasattr(self.set_temperature, 'to_alipay_dict'):
                params['set_temperature'] = self.set_temperature.to_alipay_dict()
            else:
                params['set_temperature'] = self.set_temperature
        if self.set_time:
            if hasattr(self.set_time, 'to_alipay_dict'):
                params['set_time'] = self.set_time.to_alipay_dict()
            else:
                params['set_time'] = self.set_time
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
        o = DatadigitalAnttechAppcoreTemperaturecontrolSubmitModel()
        if 'company_uscc' in d:
            o.company_uscc = d['company_uscc']
        if 'heating_mode' in d:
            o.heating_mode = d['heating_mode']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'resident_id' in d:
            o.resident_id = d['resident_id']
        if 'room_temperature' in d:
            o.room_temperature = d['room_temperature']
        if 'set_temperature' in d:
            o.set_temperature = d['set_temperature']
        if 'set_time' in d:
            o.set_time = d['set_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


