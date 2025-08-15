#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentSignFundAuthFreezeInfoDTO import RentSignFundAuthFreezeInfoDTO
from alipay.aop.api.domain.RentSignDeductInfoDTO import RentSignDeductInfoDTO


class RentDoSignInfoDTO(object):

    def __init__(self):
        self._fund_auth_freeze_info = None
        self._rent_deduct_info = None

    @property
    def fund_auth_freeze_info(self):
        return self._fund_auth_freeze_info

    @fund_auth_freeze_info.setter
    def fund_auth_freeze_info(self, value):
        if isinstance(value, RentSignFundAuthFreezeInfoDTO):
            self._fund_auth_freeze_info = value
        else:
            self._fund_auth_freeze_info = RentSignFundAuthFreezeInfoDTO.from_alipay_dict(value)
    @property
    def rent_deduct_info(self):
        return self._rent_deduct_info

    @rent_deduct_info.setter
    def rent_deduct_info(self, value):
        if isinstance(value, RentSignDeductInfoDTO):
            self._rent_deduct_info = value
        else:
            self._rent_deduct_info = RentSignDeductInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        o = RentDoSignInfoDTO()
        if 'fund_auth_freeze_info' in d:
            o.fund_auth_freeze_info = d['fund_auth_freeze_info']
        if 'rent_deduct_info' in d:
            o.rent_deduct_info = d['rent_deduct_info']
        return o


