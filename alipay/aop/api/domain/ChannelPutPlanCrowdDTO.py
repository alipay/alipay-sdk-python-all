#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelPutPlanCrowdDTO(object):

    def __init__(self):
        self._ext_crowd_key = None
        self._id = None
        self._name = None

    @property
    def ext_crowd_key(self):
        return self._ext_crowd_key

    @ext_crowd_key.setter
    def ext_crowd_key(self, value):
        self._ext_crowd_key = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.ext_crowd_key:
            if hasattr(self.ext_crowd_key, 'to_alipay_dict'):
                params['ext_crowd_key'] = self.ext_crowd_key.to_alipay_dict()
            else:
                params['ext_crowd_key'] = self.ext_crowd_key
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelPutPlanCrowdDTO()
        if 'ext_crowd_key' in d:
            o.ext_crowd_key = d['ext_crowd_key']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        return o


