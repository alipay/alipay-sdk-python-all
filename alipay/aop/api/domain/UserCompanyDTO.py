#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserCompanyDTO(object):

    def __init__(self):
        self._entity_id = None
        self._entity_name = None
        self._passport_id = None
        self._work_order_permission = None

    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def work_order_permission(self):
        return self._work_order_permission

    @work_order_permission.setter
    def work_order_permission(self, value):
        self._work_order_permission = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.work_order_permission:
            if hasattr(self.work_order_permission, 'to_alipay_dict'):
                params['work_order_permission'] = self.work_order_permission.to_alipay_dict()
            else:
                params['work_order_permission'] = self.work_order_permission
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserCompanyDTO()
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'work_order_permission' in d:
            o.work_order_permission = d['work_order_permission']
        return o


