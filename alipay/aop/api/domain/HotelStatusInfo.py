#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelStatusInfo(object):

    def __init__(self):
        self._target_id = None

    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HotelStatusInfo()
        if 'target_id' in d:
            o.target_id = d['target_id']
        return o


