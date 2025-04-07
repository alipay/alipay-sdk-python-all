#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentLoanConsultResult(object):

    def __init__(self):
        self._consult_result = None
        self._invest_pid = None

    @property
    def consult_result(self):
        return self._consult_result

    @consult_result.setter
    def consult_result(self, value):
        self._consult_result = value
    @property
    def invest_pid(self):
        return self._invest_pid

    @invest_pid.setter
    def invest_pid(self, value):
        self._invest_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_result:
            if hasattr(self.consult_result, 'to_alipay_dict'):
                params['consult_result'] = self.consult_result.to_alipay_dict()
            else:
                params['consult_result'] = self.consult_result
        if self.invest_pid:
            if hasattr(self.invest_pid, 'to_alipay_dict'):
                params['invest_pid'] = self.invest_pid.to_alipay_dict()
            else:
                params['invest_pid'] = self.invest_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentLoanConsultResult()
        if 'consult_result' in d:
            o.consult_result = d['consult_result']
        if 'invest_pid' in d:
            o.invest_pid = d['invest_pid']
        return o


