#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryNucleicremindSubscribeModifyModel(object):

    def __init__(self):
        self._city_code = None
        self._open_id = None
        self._reminder_hour_list = None
        self._status = None
        self._user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def reminder_hour_list(self):
        return self._reminder_hour_list

    @reminder_hour_list.setter
    def reminder_hour_list(self, value):
        if isinstance(value, list):
            self._reminder_hour_list = list()
            for i in value:
                self._reminder_hour_list.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.reminder_hour_list:
            if isinstance(self.reminder_hour_list, list):
                for i in range(0, len(self.reminder_hour_list)):
                    element = self.reminder_hour_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.reminder_hour_list[i] = element.to_alipay_dict()
            if hasattr(self.reminder_hour_list, 'to_alipay_dict'):
                params['reminder_hour_list'] = self.reminder_hour_list.to_alipay_dict()
            else:
                params['reminder_hour_list'] = self.reminder_hour_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayEbppIndustryNucleicremindSubscribeModifyModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'reminder_hour_list' in d:
            o.reminder_hour_list = d['reminder_hour_list']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


