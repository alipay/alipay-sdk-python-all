#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderExtInfoDTO(object):

    def __init__(self):
        self._door_time = None

    @property
    def door_time(self):
        return self._door_time

    @door_time.setter
    def door_time(self, value):
        self._door_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.door_time:
            if hasattr(self.door_time, 'to_alipay_dict'):
                params['door_time'] = self.door_time.to_alipay_dict()
            else:
                params['door_time'] = self.door_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderExtInfoDTO()
        if 'door_time' in d:
            o.door_time = d['door_time']
        return o


