#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtInfoMap import ExtInfoMap


class AlipayCommerceOperationGamemarketingBenefitApplyModel(object):

    def __init__(self):
        self._activity_code = None
        self._benefit_strategy_ext_info = None
        self._platform = None
        self._trade_no = None
        self._user_account = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def benefit_strategy_ext_info(self):
        return self._benefit_strategy_ext_info

    @benefit_strategy_ext_info.setter
    def benefit_strategy_ext_info(self, value):
        if isinstance(value, list):
            self._benefit_strategy_ext_info = list()
            for i in value:
                if isinstance(i, ExtInfoMap):
                    self._benefit_strategy_ext_info.append(i)
                else:
                    self._benefit_strategy_ext_info.append(ExtInfoMap.from_alipay_dict(i))
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_account(self):
        return self._user_account

    @user_account.setter
    def user_account(self, value):
        self._user_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.benefit_strategy_ext_info:
            if isinstance(self.benefit_strategy_ext_info, list):
                for i in range(0, len(self.benefit_strategy_ext_info)):
                    element = self.benefit_strategy_ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_strategy_ext_info[i] = element.to_alipay_dict()
            if hasattr(self.benefit_strategy_ext_info, 'to_alipay_dict'):
                params['benefit_strategy_ext_info'] = self.benefit_strategy_ext_info.to_alipay_dict()
            else:
                params['benefit_strategy_ext_info'] = self.benefit_strategy_ext_info
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_account:
            if hasattr(self.user_account, 'to_alipay_dict'):
                params['user_account'] = self.user_account.to_alipay_dict()
            else:
                params['user_account'] = self.user_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationGamemarketingBenefitApplyModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'benefit_strategy_ext_info' in d:
            o.benefit_strategy_ext_info = d['benefit_strategy_ext_info']
        if 'platform' in d:
            o.platform = d['platform']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_account' in d:
            o.user_account = d['user_account']
        return o


