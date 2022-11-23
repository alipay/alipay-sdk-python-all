#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApeSelect(object):

    def __init__(self):
        self._id = None
        self._select_id = None
        self._status = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def select_id(self):
        return self._select_id

    @select_id.setter
    def select_id(self, value):
        self._select_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.select_id:
            if hasattr(self.select_id, 'to_alipay_dict'):
                params['select_id'] = self.select_id.to_alipay_dict()
            else:
                params['select_id'] = self.select_id
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
        o = ApeSelect()
        if 'id' in d:
            o.id = d['id']
        if 'select_id' in d:
            o.select_id = d['select_id']
        if 'status' in d:
            o.status = d['status']
        return o


