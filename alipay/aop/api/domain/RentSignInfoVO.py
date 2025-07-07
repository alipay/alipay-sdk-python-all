#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentCreditInfoVO import RentCreditInfoVO
from alipay.aop.api.domain.RentFundAuthFreezeInfoVO import RentFundAuthFreezeInfoVO
from alipay.aop.api.domain.RentDeductInfoVO import RentDeductInfoVO


class RentSignInfoVO(object):

    def __init__(self):
        self._credit_info = None
        self._fund_auth_freeze_info = None
        self._rent_deduct_info = None

    @property
    def credit_info(self):
        return self._credit_info

    @credit_info.setter
    def credit_info(self, value):
        if isinstance(value, RentCreditInfoVO):
            self._credit_info = value
        else:
            self._credit_info = RentCreditInfoVO.from_alipay_dict(value)
    @property
    def fund_auth_freeze_info(self):
        return self._fund_auth_freeze_info

    @fund_auth_freeze_info.setter
    def fund_auth_freeze_info(self, value):
        if isinstance(value, RentFundAuthFreezeInfoVO):
            self._fund_auth_freeze_info = value
        else:
            self._fund_auth_freeze_info = RentFundAuthFreezeInfoVO.from_alipay_dict(value)
    @property
    def rent_deduct_info(self):
        return self._rent_deduct_info

    @rent_deduct_info.setter
    def rent_deduct_info(self, value):
        if isinstance(value, RentDeductInfoVO):
            self._rent_deduct_info = value
        else:
            self._rent_deduct_info = RentDeductInfoVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.credit_info:
            if hasattr(self.credit_info, 'to_alipay_dict'):
                params['credit_info'] = self.credit_info.to_alipay_dict()
            else:
                params['credit_info'] = self.credit_info
        if self.fund_auth_freeze_info:
            if hasattr(self.fund_auth_freeze_info, 'to_alipay_dict'):
                params['fund_auth_freeze_info'] = self.fund_auth_freeze_info.to_alipay_dict()
            else:
                params['fund_auth_freeze_info'] = self.fund_auth_freeze_info
        if self.rent_deduct_info:
            if hasattr(self.rent_deduct_info, 'to_alipay_dict'):
                params['rent_deduct_info'] = self.rent_deduct_info.to_alipay_dict()
            else:
                params['rent_deduct_info'] = self.rent_deduct_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentSignInfoVO()
        if 'credit_info' in d:
            o.credit_info = d['credit_info']
        if 'fund_auth_freeze_info' in d:
            o.fund_auth_freeze_info = d['fund_auth_freeze_info']
        if 'rent_deduct_info' in d:
            o.rent_deduct_info = d['rent_deduct_info']
        return o


