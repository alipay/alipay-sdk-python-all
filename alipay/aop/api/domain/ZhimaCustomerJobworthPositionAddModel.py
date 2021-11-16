#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JobWorthPositionInfo import JobWorthPositionInfo


class ZhimaCustomerJobworthPositionAddModel(object):

    def __init__(self):
        self._jobworth_position_info = None

    @property
    def jobworth_position_info(self):
        return self._jobworth_position_info

    @jobworth_position_info.setter
    def jobworth_position_info(self, value):
        if isinstance(value, JobWorthPositionInfo):
            self._jobworth_position_info = value
        else:
            self._jobworth_position_info = JobWorthPositionInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.jobworth_position_info:
            if hasattr(self.jobworth_position_info, 'to_alipay_dict'):
                params['jobworth_position_info'] = self.jobworth_position_info.to_alipay_dict()
            else:
                params['jobworth_position_info'] = self.jobworth_position_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerJobworthPositionAddModel()
        if 'jobworth_position_info' in d:
            o.jobworth_position_info = d['jobworth_position_info']
        return o


