#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceAbility(object):

    def __init__(self):
        self._service_ability_key = None
        self._service_ability_value = None

    @property
    def service_ability_key(self):
        return self._service_ability_key

    @service_ability_key.setter
    def service_ability_key(self, value):
        self._service_ability_key = value
    @property
    def service_ability_value(self):
        return self._service_ability_value

    @service_ability_value.setter
    def service_ability_value(self, value):
        self._service_ability_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_ability_key:
            if hasattr(self.service_ability_key, 'to_alipay_dict'):
                params['service_ability_key'] = self.service_ability_key.to_alipay_dict()
            else:
                params['service_ability_key'] = self.service_ability_key
        if self.service_ability_value:
            if hasattr(self.service_ability_value, 'to_alipay_dict'):
                params['service_ability_value'] = self.service_ability_value.to_alipay_dict()
            else:
                params['service_ability_value'] = self.service_ability_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceAbility()
        if 'service_ability_key' in d:
            o.service_ability_key = d['service_ability_key']
        if 'service_ability_value' in d:
            o.service_ability_value = d['service_ability_value']
        return o


