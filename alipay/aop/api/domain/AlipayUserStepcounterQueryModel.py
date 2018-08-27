#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserStepcounterQueryModel(object):

    def __init__(self):
        self._count_date = None
        self._partner_id = None
        self._time_zone = None
        self._user_id = None

    @property
    def count_date(self):
        return self._count_date

    @count_date.setter
    def count_date(self, value):
        self._count_date = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.count_date:
            if hasattr(self.count_date, 'to_alipay_dict'):
                params['count_date'] = self.count_date.to_alipay_dict()
            else:
                params['count_date'] = self.count_date
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
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
        o = AlipayUserStepcounterQueryModel()
        if 'count_date' in d:
            o.count_date = d['count_date']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


