#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentSupplementaryInfoDTO(object):

    def __init__(self):
        self._real_create_time = None

    @property
    def real_create_time(self):
        return self._real_create_time

    @real_create_time.setter
    def real_create_time(self, value):
        self._real_create_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.real_create_time:
            if hasattr(self.real_create_time, 'to_alipay_dict'):
                params['real_create_time'] = self.real_create_time.to_alipay_dict()
            else:
                params['real_create_time'] = self.real_create_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentSupplementaryInfoDTO()
        if 'real_create_time' in d:
            o.real_create_time = d['real_create_time']
        return o


