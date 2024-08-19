#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PartnerDTO import PartnerDTO


class AlipayTradeEpayprodProductApplyModel(object):

    def __init__(self):
        self._cooperation_mode = None
        self._partner_info = None
        self._pay_solution = None

    @property
    def cooperation_mode(self):
        return self._cooperation_mode

    @cooperation_mode.setter
    def cooperation_mode(self, value):
        self._cooperation_mode = value
    @property
    def partner_info(self):
        return self._partner_info

    @partner_info.setter
    def partner_info(self, value):
        if isinstance(value, PartnerDTO):
            self._partner_info = value
        else:
            self._partner_info = PartnerDTO.from_alipay_dict(value)
    @property
    def pay_solution(self):
        return self._pay_solution

    @pay_solution.setter
    def pay_solution(self, value):
        self._pay_solution = value


    def to_alipay_dict(self):
        params = dict()
        if self.cooperation_mode:
            if hasattr(self.cooperation_mode, 'to_alipay_dict'):
                params['cooperation_mode'] = self.cooperation_mode.to_alipay_dict()
            else:
                params['cooperation_mode'] = self.cooperation_mode
        if self.partner_info:
            if hasattr(self.partner_info, 'to_alipay_dict'):
                params['partner_info'] = self.partner_info.to_alipay_dict()
            else:
                params['partner_info'] = self.partner_info
        if self.pay_solution:
            if hasattr(self.pay_solution, 'to_alipay_dict'):
                params['pay_solution'] = self.pay_solution.to_alipay_dict()
            else:
                params['pay_solution'] = self.pay_solution
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeEpayprodProductApplyModel()
        if 'cooperation_mode' in d:
            o.cooperation_mode = d['cooperation_mode']
        if 'partner_info' in d:
            o.partner_info = d['partner_info']
        if 'pay_solution' in d:
            o.pay_solution = d['pay_solution']
        return o


