#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.LoanPayConsultOrder import LoanPayConsultOrder
from alipay.aop.api.domain.LoanPayUser import LoanPayUser


class MybankCreditLoantradeLoanpayAssetConsultModel(object):

    def __init__(self):
        self._alipay_partner_id = None
        self._apply_amt = None
        self._order_info = None
        self._payment_sale_pd_code = None
        self._platform_type = None
        self._sub_platform_type = None
        self._user = None

    @property
    def alipay_partner_id(self):
        return self._alipay_partner_id

    @alipay_partner_id.setter
    def alipay_partner_id(self, value):
        self._alipay_partner_id = value
    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._apply_amt = value
        else:
            self._apply_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        if isinstance(value, list):
            self._order_info = list()
            for i in value:
                if isinstance(i, LoanPayConsultOrder):
                    self._order_info.append(i)
                else:
                    self._order_info.append(LoanPayConsultOrder.from_alipay_dict(i))
    @property
    def payment_sale_pd_code(self):
        return self._payment_sale_pd_code

    @payment_sale_pd_code.setter
    def payment_sale_pd_code(self, value):
        self._payment_sale_pd_code = value
    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    @property
    def sub_platform_type(self):
        return self._sub_platform_type

    @sub_platform_type.setter
    def sub_platform_type(self, value):
        self._sub_platform_type = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, LoanPayUser):
            self._user = value
        else:
            self._user = LoanPayUser.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_partner_id:
            if hasattr(self.alipay_partner_id, 'to_alipay_dict'):
                params['alipay_partner_id'] = self.alipay_partner_id.to_alipay_dict()
            else:
                params['alipay_partner_id'] = self.alipay_partner_id
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.order_info:
            if isinstance(self.order_info, list):
                for i in range(0, len(self.order_info)):
                    element = self.order_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_info[i] = element.to_alipay_dict()
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.payment_sale_pd_code:
            if hasattr(self.payment_sale_pd_code, 'to_alipay_dict'):
                params['payment_sale_pd_code'] = self.payment_sale_pd_code.to_alipay_dict()
            else:
                params['payment_sale_pd_code'] = self.payment_sale_pd_code
        if self.platform_type:
            if hasattr(self.platform_type, 'to_alipay_dict'):
                params['platform_type'] = self.platform_type.to_alipay_dict()
            else:
                params['platform_type'] = self.platform_type
        if self.sub_platform_type:
            if hasattr(self.sub_platform_type, 'to_alipay_dict'):
                params['sub_platform_type'] = self.sub_platform_type.to_alipay_dict()
            else:
                params['sub_platform_type'] = self.sub_platform_type
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeLoanpayAssetConsultModel()
        if 'alipay_partner_id' in d:
            o.alipay_partner_id = d['alipay_partner_id']
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'payment_sale_pd_code' in d:
            o.payment_sale_pd_code = d['payment_sale_pd_code']
        if 'platform_type' in d:
            o.platform_type = d['platform_type']
        if 'sub_platform_type' in d:
            o.sub_platform_type = d['sub_platform_type']
        if 'user' in d:
            o.user = d['user']
        return o


