#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundLimit import FundLimit


class AuthBizParam(object):

    def __init__(self):
        self._fund_limit_list = None

    @property
    def fund_limit_list(self):
        return self._fund_limit_list

    @fund_limit_list.setter
    def fund_limit_list(self, value):
        if isinstance(value, list):
            self._fund_limit_list = list()
            for i in value:
                if isinstance(i, FundLimit):
                    self._fund_limit_list.append(i)
                else:
                    self._fund_limit_list.append(FundLimit.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.fund_limit_list:
            if isinstance(self.fund_limit_list, list):
                for i in range(0, len(self.fund_limit_list)):
                    element = self.fund_limit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_limit_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_limit_list, 'to_alipay_dict'):
                params['fund_limit_list'] = self.fund_limit_list.to_alipay_dict()
            else:
                params['fund_limit_list'] = self.fund_limit_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthBizParam()
        if 'fund_limit_list' in d:
            o.fund_limit_list = d['fund_limit_list']
        return o


