#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GeneralWithholdInfoDTO(object):

    def __init__(self):
        self._agreement_pay_sign = None

    @property
    def agreement_pay_sign(self):
        return self._agreement_pay_sign

    @agreement_pay_sign.setter
    def agreement_pay_sign(self, value):
        self._agreement_pay_sign = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_pay_sign:
            if hasattr(self.agreement_pay_sign, 'to_alipay_dict'):
                params['agreement_pay_sign'] = self.agreement_pay_sign.to_alipay_dict()
            else:
                params['agreement_pay_sign'] = self.agreement_pay_sign
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GeneralWithholdInfoDTO()
        if 'agreement_pay_sign' in d:
            o.agreement_pay_sign = d['agreement_pay_sign']
        return o


