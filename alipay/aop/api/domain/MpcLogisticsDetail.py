#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcLogisticsDetail(object):

    def __init__(self):
        self._occur_time = None
        self._stand_desc = None

    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def stand_desc(self):
        return self._stand_desc

    @stand_desc.setter
    def stand_desc(self, value):
        self._stand_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.occur_time:
            if hasattr(self.occur_time, 'to_alipay_dict'):
                params['occur_time'] = self.occur_time.to_alipay_dict()
            else:
                params['occur_time'] = self.occur_time
        if self.stand_desc:
            if hasattr(self.stand_desc, 'to_alipay_dict'):
                params['stand_desc'] = self.stand_desc.to_alipay_dict()
            else:
                params['stand_desc'] = self.stand_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcLogisticsDetail()
        if 'occur_time' in d:
            o.occur_time = d['occur_time']
        if 'stand_desc' in d:
            o.stand_desc = d['stand_desc']
        return o


