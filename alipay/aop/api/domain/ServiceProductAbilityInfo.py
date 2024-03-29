#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceProductAbilityInfo(object):

    def __init__(self):
        self._id = None
        self._service_ability = None
        self._service_ability_name = None
        self._service_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def service_ability(self):
        return self._service_ability

    @service_ability.setter
    def service_ability(self, value):
        self._service_ability = value
    @property
    def service_ability_name(self):
        return self._service_ability_name

    @service_ability_name.setter
    def service_ability_name(self, value):
        self._service_ability_name = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.service_ability:
            if hasattr(self.service_ability, 'to_alipay_dict'):
                params['service_ability'] = self.service_ability.to_alipay_dict()
            else:
                params['service_ability'] = self.service_ability
        if self.service_ability_name:
            if hasattr(self.service_ability_name, 'to_alipay_dict'):
                params['service_ability_name'] = self.service_ability_name.to_alipay_dict()
            else:
                params['service_ability_name'] = self.service_ability_name
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceProductAbilityInfo()
        if 'id' in d:
            o.id = d['id']
        if 'service_ability' in d:
            o.service_ability = d['service_ability']
        if 'service_ability_name' in d:
            o.service_ability_name = d['service_ability_name']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


