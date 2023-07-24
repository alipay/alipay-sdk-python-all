#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApmobileAppApiUsedOverviewDTO(object):

    def __init__(self):
        self._info_name = None
        self._info_type = None

    @property
    def info_name(self):
        return self._info_name

    @info_name.setter
    def info_name(self, value):
        self._info_name = value
    @property
    def info_type(self):
        return self._info_type

    @info_type.setter
    def info_type(self, value):
        self._info_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.info_name:
            if hasattr(self.info_name, 'to_alipay_dict'):
                params['info_name'] = self.info_name.to_alipay_dict()
            else:
                params['info_name'] = self.info_name
        if self.info_type:
            if hasattr(self.info_type, 'to_alipay_dict'):
                params['info_type'] = self.info_type.to_alipay_dict()
            else:
                params['info_type'] = self.info_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppApiUsedOverviewDTO()
        if 'info_name' in d:
            o.info_name = d['info_name']
        if 'info_type' in d:
            o.info_type = d['info_type']
        return o


