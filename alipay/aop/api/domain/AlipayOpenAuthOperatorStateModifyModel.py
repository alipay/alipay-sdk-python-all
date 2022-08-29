#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthOperatorStateModifyModel(object):

    def __init__(self):
        self._action = None
        self._operator_ids = None
        self._tenant_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def operator_ids(self):
        return self._operator_ids

    @operator_ids.setter
    def operator_ids(self, value):
        if isinstance(value, list):
            self._operator_ids = list()
            for i in value:
                self._operator_ids.append(i)
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.operator_ids:
            if isinstance(self.operator_ids, list):
                for i in range(0, len(self.operator_ids)):
                    element = self.operator_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operator_ids[i] = element.to_alipay_dict()
            if hasattr(self.operator_ids, 'to_alipay_dict'):
                params['operator_ids'] = self.operator_ids.to_alipay_dict()
            else:
                params['operator_ids'] = self.operator_ids
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthOperatorStateModifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'operator_ids' in d:
            o.operator_ids = d['operator_ids']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


