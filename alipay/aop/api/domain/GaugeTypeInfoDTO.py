#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GaugeTypeInfoDTO(object):

    def __init__(self):
        self._id = None
        self._name = None
        self._ques_count = None
        self._sub_type = None
        self._type = None

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
    def ques_count(self):
        return self._ques_count

    @ques_count.setter
    def ques_count(self, value):
        self._ques_count = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


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
        if self.ques_count:
            if hasattr(self.ques_count, 'to_alipay_dict'):
                params['ques_count'] = self.ques_count.to_alipay_dict()
            else:
                params['ques_count'] = self.ques_count
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GaugeTypeInfoDTO()
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'ques_count' in d:
            o.ques_count = d['ques_count']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'type' in d:
            o.type = d['type']
        return o


