#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelDetailParams(object):

    def __init__(self):
        self._card_group_name = None
        self._credit_risk_info = None
        self._gov_subsidy = None
        self._inst_subsidy = None
        self._marketing_flag = None
        self._refuse_code = None
        self._user_has_sign = None

    @property
    def card_group_name(self):
        return self._card_group_name

    @card_group_name.setter
    def card_group_name(self, value):
        self._card_group_name = value
    @property
    def credit_risk_info(self):
        return self._credit_risk_info

    @credit_risk_info.setter
    def credit_risk_info(self, value):
        self._credit_risk_info = value
    @property
    def gov_subsidy(self):
        return self._gov_subsidy

    @gov_subsidy.setter
    def gov_subsidy(self, value):
        self._gov_subsidy = value
    @property
    def inst_subsidy(self):
        return self._inst_subsidy

    @inst_subsidy.setter
    def inst_subsidy(self, value):
        self._inst_subsidy = value
    @property
    def marketing_flag(self):
        return self._marketing_flag

    @marketing_flag.setter
    def marketing_flag(self, value):
        self._marketing_flag = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def user_has_sign(self):
        return self._user_has_sign

    @user_has_sign.setter
    def user_has_sign(self, value):
        self._user_has_sign = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_group_name:
            if hasattr(self.card_group_name, 'to_alipay_dict'):
                params['card_group_name'] = self.card_group_name.to_alipay_dict()
            else:
                params['card_group_name'] = self.card_group_name
        if self.credit_risk_info:
            if hasattr(self.credit_risk_info, 'to_alipay_dict'):
                params['credit_risk_info'] = self.credit_risk_info.to_alipay_dict()
            else:
                params['credit_risk_info'] = self.credit_risk_info
        if self.gov_subsidy:
            if hasattr(self.gov_subsidy, 'to_alipay_dict'):
                params['gov_subsidy'] = self.gov_subsidy.to_alipay_dict()
            else:
                params['gov_subsidy'] = self.gov_subsidy
        if self.inst_subsidy:
            if hasattr(self.inst_subsidy, 'to_alipay_dict'):
                params['inst_subsidy'] = self.inst_subsidy.to_alipay_dict()
            else:
                params['inst_subsidy'] = self.inst_subsidy
        if self.marketing_flag:
            if hasattr(self.marketing_flag, 'to_alipay_dict'):
                params['marketing_flag'] = self.marketing_flag.to_alipay_dict()
            else:
                params['marketing_flag'] = self.marketing_flag
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        if self.user_has_sign:
            if hasattr(self.user_has_sign, 'to_alipay_dict'):
                params['user_has_sign'] = self.user_has_sign.to_alipay_dict()
            else:
                params['user_has_sign'] = self.user_has_sign
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelDetailParams()
        if 'card_group_name' in d:
            o.card_group_name = d['card_group_name']
        if 'credit_risk_info' in d:
            o.credit_risk_info = d['credit_risk_info']
        if 'gov_subsidy' in d:
            o.gov_subsidy = d['gov_subsidy']
        if 'inst_subsidy' in d:
            o.inst_subsidy = d['inst_subsidy']
        if 'marketing_flag' in d:
            o.marketing_flag = d['marketing_flag']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        if 'user_has_sign' in d:
            o.user_has_sign = d['user_has_sign']
        return o


