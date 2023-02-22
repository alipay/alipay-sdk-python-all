#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherUseTimeRuleInfo import VoucherUseTimeRuleInfo
from alipay.aop.api.domain.VoucherUseTimeRuleInfo import VoucherUseTimeRuleInfo


class TimeRestrictInfo(object):

    def __init__(self):
        self._disable_period_info = None
        self._usable_period_info = None

    @property
    def disable_period_info(self):
        return self._disable_period_info

    @disable_period_info.setter
    def disable_period_info(self, value):
        if isinstance(value, list):
            self._disable_period_info = list()
            for i in value:
                if isinstance(i, VoucherUseTimeRuleInfo):
                    self._disable_period_info.append(i)
                else:
                    self._disable_period_info.append(VoucherUseTimeRuleInfo.from_alipay_dict(i))
    @property
    def usable_period_info(self):
        return self._usable_period_info

    @usable_period_info.setter
    def usable_period_info(self, value):
        if isinstance(value, list):
            self._usable_period_info = list()
            for i in value:
                if isinstance(i, VoucherUseTimeRuleInfo):
                    self._usable_period_info.append(i)
                else:
                    self._usable_period_info.append(VoucherUseTimeRuleInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.disable_period_info:
            if isinstance(self.disable_period_info, list):
                for i in range(0, len(self.disable_period_info)):
                    element = self.disable_period_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disable_period_info[i] = element.to_alipay_dict()
            if hasattr(self.disable_period_info, 'to_alipay_dict'):
                params['disable_period_info'] = self.disable_period_info.to_alipay_dict()
            else:
                params['disable_period_info'] = self.disable_period_info
        if self.usable_period_info:
            if isinstance(self.usable_period_info, list):
                for i in range(0, len(self.usable_period_info)):
                    element = self.usable_period_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.usable_period_info[i] = element.to_alipay_dict()
            if hasattr(self.usable_period_info, 'to_alipay_dict'):
                params['usable_period_info'] = self.usable_period_info.to_alipay_dict()
            else:
                params['usable_period_info'] = self.usable_period_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TimeRestrictInfo()
        if 'disable_period_info' in d:
            o.disable_period_info = d['disable_period_info']
        if 'usable_period_info' in d:
            o.usable_period_info = d['usable_period_info']
        return o


