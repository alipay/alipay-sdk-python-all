#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerLoanNotMatchData import ConsumerLoanNotMatchData


class ConsumerLoanUserAccountCheckData(object):

    def __init__(self):
        self._not_match_data = None

    @property
    def not_match_data(self):
        return self._not_match_data

    @not_match_data.setter
    def not_match_data(self, value):
        if isinstance(value, ConsumerLoanNotMatchData):
            self._not_match_data = value
        else:
            self._not_match_data = ConsumerLoanNotMatchData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.not_match_data:
            if hasattr(self.not_match_data, 'to_alipay_dict'):
                params['not_match_data'] = self.not_match_data.to_alipay_dict()
            else:
                params['not_match_data'] = self.not_match_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanUserAccountCheckData()
        if 'not_match_data' in d:
            o.not_match_data = d['not_match_data']
        return o


