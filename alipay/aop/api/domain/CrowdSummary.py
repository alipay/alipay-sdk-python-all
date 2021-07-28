#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CrowdSummary(object):

    def __init__(self):
        self._crowd_count = None
        self._crowd_id = None
        self._crowd_name = None
        self._status = None

    @property
    def crowd_count(self):
        return self._crowd_count

    @crowd_count.setter
    def crowd_count(self, value):
        self._crowd_count = value
    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_count:
            if hasattr(self.crowd_count, 'to_alipay_dict'):
                params['crowd_count'] = self.crowd_count.to_alipay_dict()
            else:
                params['crowd_count'] = self.crowd_count
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
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
        o = CrowdSummary()
        if 'crowd_count' in d:
            o.crowd_count = d['crowd_count']
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'status' in d:
            o.status = d['status']
        return o


