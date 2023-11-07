#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UpdateCustomerChannelAccountRequest(object):

    def __init__(self):
        self._binding_status = None
        self._delete_flag = None
        self._id = None
        self._operator = None

    @property
    def binding_status(self):
        return self._binding_status

    @binding_status.setter
    def binding_status(self, value):
        self._binding_status = value
    @property
    def delete_flag(self):
        return self._delete_flag

    @delete_flag.setter
    def delete_flag(self, value):
        self._delete_flag = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.binding_status:
            if hasattr(self.binding_status, 'to_alipay_dict'):
                params['binding_status'] = self.binding_status.to_alipay_dict()
            else:
                params['binding_status'] = self.binding_status
        if self.delete_flag:
            if hasattr(self.delete_flag, 'to_alipay_dict'):
                params['delete_flag'] = self.delete_flag.to_alipay_dict()
            else:
                params['delete_flag'] = self.delete_flag
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
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
        o = UpdateCustomerChannelAccountRequest()
        if 'binding_status' in d:
            o.binding_status = d['binding_status']
        if 'delete_flag' in d:
            o.delete_flag = d['delete_flag']
        if 'id' in d:
            o.id = d['id']
        if 'operator' in d:
            o.operator = d['operator']
        return o


