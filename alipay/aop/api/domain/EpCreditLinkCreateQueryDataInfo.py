#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditRateResult import CreditRateResult


class EpCreditLinkCreateQueryDataInfo(object):

    def __init__(self):
        self._cr_result = None

    @property
    def cr_result(self):
        return self._cr_result

    @cr_result.setter
    def cr_result(self, value):
        if isinstance(value, CreditRateResult):
            self._cr_result = value
        else:
            self._cr_result = CreditRateResult.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.cr_result:
            if hasattr(self.cr_result, 'to_alipay_dict'):
                params['cr_result'] = self.cr_result.to_alipay_dict()
            else:
                params['cr_result'] = self.cr_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpCreditLinkCreateQueryDataInfo()
        if 'cr_result' in d:
            o.cr_result = d['cr_result']
        return o


