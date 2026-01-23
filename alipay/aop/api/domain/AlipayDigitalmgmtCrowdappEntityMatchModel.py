#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtCrowdappEntityMatchModel(object):

    def __init__(self):
        self._check_crowd_app_permission = None
        self._check_row_permission = None
        self._crowd_app_ids = None
        self._entity_id = None
        self._operator = None

    @property
    def check_crowd_app_permission(self):
        return self._check_crowd_app_permission

    @check_crowd_app_permission.setter
    def check_crowd_app_permission(self, value):
        self._check_crowd_app_permission = value
    @property
    def check_row_permission(self):
        return self._check_row_permission

    @check_row_permission.setter
    def check_row_permission(self, value):
        self._check_row_permission = value
    @property
    def crowd_app_ids(self):
        return self._crowd_app_ids

    @crowd_app_ids.setter
    def crowd_app_ids(self, value):
        if isinstance(value, list):
            self._crowd_app_ids = list()
            for i in value:
                self._crowd_app_ids.append(i)
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_crowd_app_permission:
            if hasattr(self.check_crowd_app_permission, 'to_alipay_dict'):
                params['check_crowd_app_permission'] = self.check_crowd_app_permission.to_alipay_dict()
            else:
                params['check_crowd_app_permission'] = self.check_crowd_app_permission
        if self.check_row_permission:
            if hasattr(self.check_row_permission, 'to_alipay_dict'):
                params['check_row_permission'] = self.check_row_permission.to_alipay_dict()
            else:
                params['check_row_permission'] = self.check_row_permission
        if self.crowd_app_ids:
            if isinstance(self.crowd_app_ids, list):
                for i in range(0, len(self.crowd_app_ids)):
                    element = self.crowd_app_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crowd_app_ids[i] = element.to_alipay_dict()
            if hasattr(self.crowd_app_ids, 'to_alipay_dict'):
                params['crowd_app_ids'] = self.crowd_app_ids.to_alipay_dict()
            else:
                params['crowd_app_ids'] = self.crowd_app_ids
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtCrowdappEntityMatchModel()
        if 'check_crowd_app_permission' in d:
            o.check_crowd_app_permission = d['check_crowd_app_permission']
        if 'check_row_permission' in d:
            o.check_row_permission = d['check_row_permission']
        if 'crowd_app_ids' in d:
            o.crowd_app_ids = d['crowd_app_ids']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'operator' in d:
            o.operator = d['operator']
        return o


