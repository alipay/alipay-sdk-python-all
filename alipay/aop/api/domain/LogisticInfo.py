#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticInfo(object):

    def __init__(self):
        self._channel = None
        self._detail = None
        self._logistic_id = None
        self._ship_area = None
        self._ship_period = None
        self._status = None
        self._stop_update_time = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def logistic_id(self):
        return self._logistic_id

    @logistic_id.setter
    def logistic_id(self, value):
        self._logistic_id = value
    @property
    def ship_area(self):
        return self._ship_area

    @ship_area.setter
    def ship_area(self, value):
        self._ship_area = value
    @property
    def ship_period(self):
        return self._ship_period

    @ship_period.setter
    def ship_period(self, value):
        self._ship_period = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def stop_update_time(self):
        return self._stop_update_time

    @stop_update_time.setter
    def stop_update_time(self, value):
        self._stop_update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.logistic_id:
            if hasattr(self.logistic_id, 'to_alipay_dict'):
                params['logistic_id'] = self.logistic_id.to_alipay_dict()
            else:
                params['logistic_id'] = self.logistic_id
        if self.ship_area:
            if hasattr(self.ship_area, 'to_alipay_dict'):
                params['ship_area'] = self.ship_area.to_alipay_dict()
            else:
                params['ship_area'] = self.ship_area
        if self.ship_period:
            if hasattr(self.ship_period, 'to_alipay_dict'):
                params['ship_period'] = self.ship_period.to_alipay_dict()
            else:
                params['ship_period'] = self.ship_period
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.stop_update_time:
            if hasattr(self.stop_update_time, 'to_alipay_dict'):
                params['stop_update_time'] = self.stop_update_time.to_alipay_dict()
            else:
                params['stop_update_time'] = self.stop_update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticInfo()
        if 'channel' in d:
            o.channel = d['channel']
        if 'detail' in d:
            o.detail = d['detail']
        if 'logistic_id' in d:
            o.logistic_id = d['logistic_id']
        if 'ship_area' in d:
            o.ship_area = d['ship_area']
        if 'ship_period' in d:
            o.ship_period = d['ship_period']
        if 'status' in d:
            o.status = d['status']
        if 'stop_update_time' in d:
            o.stop_update_time = d['stop_update_time']
        return o


