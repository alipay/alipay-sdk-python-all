#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCharityForestSendModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_time = None
        self._energy = None
        self._energy_type = None
        self._source = None
        self._user_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = value
    @property
    def energy_type(self):
        return self._energy_type

    @energy_type.setter
    def energy_type(self, value):
        self._energy_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.energy:
            if hasattr(self.energy, 'to_alipay_dict'):
                params['energy'] = self.energy.to_alipay_dict()
            else:
                params['energy'] = self.energy
        if self.energy_type:
            if hasattr(self.energy_type, 'to_alipay_dict'):
                params['energy_type'] = self.energy_type.to_alipay_dict()
            else:
                params['energy_type'] = self.energy_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipayUserCharityForestSendModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'energy' in d:
            o.energy = d['energy']
        if 'energy_type' in d:
            o.energy_type = d['energy_type']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


