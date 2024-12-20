#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpBranchDetailInfo(object):

    def __init__(self):
        self._approval_date = None
        self._name = None
        self._old_name = None
        self._register_organ = None
        self._registration_state = None
        self._registry_id = None
        self._tyshxydm = None

    @property
    def approval_date(self):
        return self._approval_date

    @approval_date.setter
    def approval_date(self, value):
        self._approval_date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def old_name(self):
        return self._old_name

    @old_name.setter
    def old_name(self, value):
        if isinstance(value, list):
            self._old_name = list()
            for i in value:
                self._old_name.append(i)
    @property
    def register_organ(self):
        return self._register_organ

    @register_organ.setter
    def register_organ(self, value):
        self._register_organ = value
    @property
    def registration_state(self):
        return self._registration_state

    @registration_state.setter
    def registration_state(self, value):
        self._registration_state = value
    @property
    def registry_id(self):
        return self._registry_id

    @registry_id.setter
    def registry_id(self, value):
        self._registry_id = value
    @property
    def tyshxydm(self):
        return self._tyshxydm

    @tyshxydm.setter
    def tyshxydm(self, value):
        self._tyshxydm = value


    def to_alipay_dict(self):
        params = dict()
        if self.approval_date:
            if hasattr(self.approval_date, 'to_alipay_dict'):
                params['approval_date'] = self.approval_date.to_alipay_dict()
            else:
                params['approval_date'] = self.approval_date
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.old_name:
            if isinstance(self.old_name, list):
                for i in range(0, len(self.old_name)):
                    element = self.old_name[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.old_name[i] = element.to_alipay_dict()
            if hasattr(self.old_name, 'to_alipay_dict'):
                params['old_name'] = self.old_name.to_alipay_dict()
            else:
                params['old_name'] = self.old_name
        if self.register_organ:
            if hasattr(self.register_organ, 'to_alipay_dict'):
                params['register_organ'] = self.register_organ.to_alipay_dict()
            else:
                params['register_organ'] = self.register_organ
        if self.registration_state:
            if hasattr(self.registration_state, 'to_alipay_dict'):
                params['registration_state'] = self.registration_state.to_alipay_dict()
            else:
                params['registration_state'] = self.registration_state
        if self.registry_id:
            if hasattr(self.registry_id, 'to_alipay_dict'):
                params['registry_id'] = self.registry_id.to_alipay_dict()
            else:
                params['registry_id'] = self.registry_id
        if self.tyshxydm:
            if hasattr(self.tyshxydm, 'to_alipay_dict'):
                params['tyshxydm'] = self.tyshxydm.to_alipay_dict()
            else:
                params['tyshxydm'] = self.tyshxydm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpBranchDetailInfo()
        if 'approval_date' in d:
            o.approval_date = d['approval_date']
        if 'name' in d:
            o.name = d['name']
        if 'old_name' in d:
            o.old_name = d['old_name']
        if 'register_organ' in d:
            o.register_organ = d['register_organ']
        if 'registration_state' in d:
            o.registration_state = d['registration_state']
        if 'registry_id' in d:
            o.registry_id = d['registry_id']
        if 'tyshxydm' in d:
            o.tyshxydm = d['tyshxydm']
        return o


