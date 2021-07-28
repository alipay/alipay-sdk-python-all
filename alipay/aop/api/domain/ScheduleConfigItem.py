#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScheduleConfigItem(object):

    def __init__(self):
        self._config_name = None
        self._date = None
        self._id = None

    @property
    def config_name(self):
        return self._config_name

    @config_name.setter
    def config_name(self, value):
        self._config_name = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.config_name:
            if hasattr(self.config_name, 'to_alipay_dict'):
                params['config_name'] = self.config_name.to_alipay_dict()
            else:
                params['config_name'] = self.config_name
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScheduleConfigItem()
        if 'config_name' in d:
            o.config_name = d['config_name']
        if 'date' in d:
            o.date = d['date']
        if 'id' in d:
            o.id = d['id']
        return o


