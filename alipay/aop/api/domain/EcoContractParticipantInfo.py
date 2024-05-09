#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcoContractParticipantInfo(object):

    def __init__(self):
        self._delete_status = None
        self._name = None
        self._out_user_id = None
        self._role = None
        self._status = None

    @property
    def delete_status(self):
        return self._delete_status

    @delete_status.setter
    def delete_status(self, value):
        self._delete_status = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if isinstance(value, list):
            self._role = list()
            for i in value:
                self._role.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.delete_status:
            if hasattr(self.delete_status, 'to_alipay_dict'):
                params['delete_status'] = self.delete_status.to_alipay_dict()
            else:
                params['delete_status'] = self.delete_status
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.role:
            if isinstance(self.role, list):
                for i in range(0, len(self.role)):
                    element = self.role[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role[i] = element.to_alipay_dict()
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoContractParticipantInfo()
        if 'delete_status' in d:
            o.delete_status = d['delete_status']
        if 'name' in d:
            o.name = d['name']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'role' in d:
            o.role = d['role']
        if 'status' in d:
            o.status = d['status']
        return o


