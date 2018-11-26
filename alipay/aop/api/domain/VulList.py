#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VulList(object):

    def __init__(self):
        self._coin = None
        self._level = None
        self._name = None
        self._status = None
        self._submit_time = None
        self._vul_id = None

    @property
    def coin(self):
        return self._coin

    @coin.setter
    def coin(self, value):
        self._coin = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def submit_time(self):
        return self._submit_time

    @submit_time.setter
    def submit_time(self, value):
        self._submit_time = value
    @property
    def vul_id(self):
        return self._vul_id

    @vul_id.setter
    def vul_id(self, value):
        self._vul_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.coin:
            if hasattr(self.coin, 'to_alipay_dict'):
                params['coin'] = self.coin.to_alipay_dict()
            else:
                params['coin'] = self.coin
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.submit_time:
            if hasattr(self.submit_time, 'to_alipay_dict'):
                params['submit_time'] = self.submit_time.to_alipay_dict()
            else:
                params['submit_time'] = self.submit_time
        if self.vul_id:
            if hasattr(self.vul_id, 'to_alipay_dict'):
                params['vul_id'] = self.vul_id.to_alipay_dict()
            else:
                params['vul_id'] = self.vul_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VulList()
        if 'coin' in d:
            o.coin = d['coin']
        if 'level' in d:
            o.level = d['level']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        if 'submit_time' in d:
            o.submit_time = d['submit_time']
        if 'vul_id' in d:
            o.vul_id = d['vul_id']
        return o


