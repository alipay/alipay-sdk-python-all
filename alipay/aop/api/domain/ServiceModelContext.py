#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceModelContext(object):

    def __init__(self):
        self._xp_id = None

    @property
    def xp_id(self):
        return self._xp_id

    @xp_id.setter
    def xp_id(self, value):
        self._xp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.xp_id:
            if hasattr(self.xp_id, 'to_alipay_dict'):
                params['xp_id'] = self.xp_id.to_alipay_dict()
            else:
                params['xp_id'] = self.xp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceModelContext()
        if 'xp_id' in d:
            o.xp_id = d['xp_id']
        return o


