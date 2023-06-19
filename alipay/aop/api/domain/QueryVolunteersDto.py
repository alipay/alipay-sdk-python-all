#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryVolunteersDto(object):

    def __init__(self):
        self._hours = None
        self._id = None

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.hours:
            if hasattr(self.hours, 'to_alipay_dict'):
                params['hours'] = self.hours.to_alipay_dict()
            else:
                params['hours'] = self.hours
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryVolunteersDto()
        if 'hours' in d:
            o.hours = d['hours']
        if 'id' in d:
            o.id = d['id']
        return o


