#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderUserinfoExpoDeleteModel(object):

    def __init__(self):
        self._identity_card = None
        self._phone = None
        self._time_uuid = None

    @property
    def identity_card(self):
        return self._identity_card

    @identity_card.setter
    def identity_card(self, value):
        self._identity_card = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def time_uuid(self):
        return self._time_uuid

    @time_uuid.setter
    def time_uuid(self, value):
        self._time_uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_card:
            if hasattr(self.identity_card, 'to_alipay_dict'):
                params['identity_card'] = self.identity_card.to_alipay_dict()
            else:
                params['identity_card'] = self.identity_card
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.time_uuid:
            if hasattr(self.time_uuid, 'to_alipay_dict'):
                params['time_uuid'] = self.time_uuid.to_alipay_dict()
            else:
                params['time_uuid'] = self.time_uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderUserinfoExpoDeleteModel()
        if 'identity_card' in d:
            o.identity_card = d['identity_card']
        if 'phone' in d:
            o.phone = d['phone']
        if 'time_uuid' in d:
            o.time_uuid = d['time_uuid']
        return o


