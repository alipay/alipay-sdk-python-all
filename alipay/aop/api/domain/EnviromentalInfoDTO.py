#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnviromentalInfoDTO(object):

    def __init__(self):
        self._environmental = None
        self._environmental_ext = None

    @property
    def environmental(self):
        return self._environmental

    @environmental.setter
    def environmental(self, value):
        self._environmental = value
    @property
    def environmental_ext(self):
        return self._environmental_ext

    @environmental_ext.setter
    def environmental_ext(self, value):
        self._environmental_ext = value


    def to_alipay_dict(self):
        params = dict()
        if self.environmental:
            if hasattr(self.environmental, 'to_alipay_dict'):
                params['environmental'] = self.environmental.to_alipay_dict()
            else:
                params['environmental'] = self.environmental
        if self.environmental_ext:
            if hasattr(self.environmental_ext, 'to_alipay_dict'):
                params['environmental_ext'] = self.environmental_ext.to_alipay_dict()
            else:
                params['environmental_ext'] = self.environmental_ext
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnviromentalInfoDTO()
        if 'environmental' in d:
            o.environmental = d['environmental']
        if 'environmental_ext' in d:
            o.environmental_ext = d['environmental_ext']
        return o


