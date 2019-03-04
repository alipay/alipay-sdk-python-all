#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromotionDetail(object):

    def __init__(self):
        self._id = None
        self._name = None
        self._status = None
        self._unavailable_reason = None
        self._value = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unavailable_reason(self):
        return self._unavailable_reason

    @unavailable_reason.setter
    def unavailable_reason(self, value):
        self._unavailable_reason = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unavailable_reason:
            if hasattr(self.unavailable_reason, 'to_alipay_dict'):
                params['unavailable_reason'] = self.unavailable_reason.to_alipay_dict()
            else:
                params['unavailable_reason'] = self.unavailable_reason
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromotionDetail()
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'status' in d:
            o.status = d['status']
        if 'unavailable_reason' in d:
            o.unavailable_reason = d['unavailable_reason']
        if 'value' in d:
            o.value = d['value']
        return o


