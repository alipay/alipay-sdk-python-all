#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgentStatisticDataItemOpenVO(object):

    def __init__(self):
        self._statistic_num = None
        self._statistic_type = None

    @property
    def statistic_num(self):
        return self._statistic_num

    @statistic_num.setter
    def statistic_num(self, value):
        self._statistic_num = value
    @property
    def statistic_type(self):
        return self._statistic_type

    @statistic_type.setter
    def statistic_type(self, value):
        self._statistic_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.statistic_num:
            if hasattr(self.statistic_num, 'to_alipay_dict'):
                params['statistic_num'] = self.statistic_num.to_alipay_dict()
            else:
                params['statistic_num'] = self.statistic_num
        if self.statistic_type:
            if hasattr(self.statistic_type, 'to_alipay_dict'):
                params['statistic_type'] = self.statistic_type.to_alipay_dict()
            else:
                params['statistic_type'] = self.statistic_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgentStatisticDataItemOpenVO()
        if 'statistic_num' in d:
            o.statistic_num = d['statistic_num']
        if 'statistic_type' in d:
            o.statistic_type = d['statistic_type']
        return o


