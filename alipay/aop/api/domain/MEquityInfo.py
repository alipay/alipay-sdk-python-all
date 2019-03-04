#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MEquityDisplayInfo import MEquityDisplayInfo
from alipay.aop.api.domain.MEquityUseRule import MEquityUseRule
from alipay.aop.api.domain.MEquityValidInfo import MEquityValidInfo
from alipay.aop.api.domain.MEquityWorthInfo import MEquityWorthInfo


class MEquityInfo(object):

    def __init__(self):
        self._equity_display_info = None
        self._equity_type = None
        self._equity_use_rule = None
        self._equity_valid_info = None
        self._equity_worth_info = None

    @property
    def equity_display_info(self):
        return self._equity_display_info

    @equity_display_info.setter
    def equity_display_info(self, value):
        if isinstance(value, MEquityDisplayInfo):
            self._equity_display_info = value
        else:
            self._equity_display_info = MEquityDisplayInfo.from_alipay_dict(value)
    @property
    def equity_type(self):
        return self._equity_type

    @equity_type.setter
    def equity_type(self, value):
        self._equity_type = value
    @property
    def equity_use_rule(self):
        return self._equity_use_rule

    @equity_use_rule.setter
    def equity_use_rule(self, value):
        if isinstance(value, MEquityUseRule):
            self._equity_use_rule = value
        else:
            self._equity_use_rule = MEquityUseRule.from_alipay_dict(value)
    @property
    def equity_valid_info(self):
        return self._equity_valid_info

    @equity_valid_info.setter
    def equity_valid_info(self, value):
        if isinstance(value, MEquityValidInfo):
            self._equity_valid_info = value
        else:
            self._equity_valid_info = MEquityValidInfo.from_alipay_dict(value)
    @property
    def equity_worth_info(self):
        return self._equity_worth_info

    @equity_worth_info.setter
    def equity_worth_info(self, value):
        if isinstance(value, MEquityWorthInfo):
            self._equity_worth_info = value
        else:
            self._equity_worth_info = MEquityWorthInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.equity_display_info:
            if hasattr(self.equity_display_info, 'to_alipay_dict'):
                params['equity_display_info'] = self.equity_display_info.to_alipay_dict()
            else:
                params['equity_display_info'] = self.equity_display_info
        if self.equity_type:
            if hasattr(self.equity_type, 'to_alipay_dict'):
                params['equity_type'] = self.equity_type.to_alipay_dict()
            else:
                params['equity_type'] = self.equity_type
        if self.equity_use_rule:
            if hasattr(self.equity_use_rule, 'to_alipay_dict'):
                params['equity_use_rule'] = self.equity_use_rule.to_alipay_dict()
            else:
                params['equity_use_rule'] = self.equity_use_rule
        if self.equity_valid_info:
            if hasattr(self.equity_valid_info, 'to_alipay_dict'):
                params['equity_valid_info'] = self.equity_valid_info.to_alipay_dict()
            else:
                params['equity_valid_info'] = self.equity_valid_info
        if self.equity_worth_info:
            if hasattr(self.equity_worth_info, 'to_alipay_dict'):
                params['equity_worth_info'] = self.equity_worth_info.to_alipay_dict()
            else:
                params['equity_worth_info'] = self.equity_worth_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MEquityInfo()
        if 'equity_display_info' in d:
            o.equity_display_info = d['equity_display_info']
        if 'equity_type' in d:
            o.equity_type = d['equity_type']
        if 'equity_use_rule' in d:
            o.equity_use_rule = d['equity_use_rule']
        if 'equity_valid_info' in d:
            o.equity_valid_info = d['equity_valid_info']
        if 'equity_worth_info' in d:
            o.equity_worth_info = d['equity_worth_info']
        return o


