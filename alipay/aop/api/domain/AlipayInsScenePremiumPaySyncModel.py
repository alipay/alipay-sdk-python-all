#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PremiumPaymentDTO import PremiumPaymentDTO


class AlipayInsScenePremiumPaySyncModel(object):

    def __init__(self):
        self._out_order_id = None
        self._partner_org_id = None
        self._premium_payment = None

    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def premium_payment(self):
        return self._premium_payment

    @premium_payment.setter
    def premium_payment(self, value):
        if isinstance(value, PremiumPaymentDTO):
            self._premium_payment = value
        else:
            self._premium_payment = PremiumPaymentDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.premium_payment:
            if hasattr(self.premium_payment, 'to_alipay_dict'):
                params['premium_payment'] = self.premium_payment.to_alipay_dict()
            else:
                params['premium_payment'] = self.premium_payment
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsScenePremiumPaySyncModel()
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'premium_payment' in d:
            o.premium_payment = d['premium_payment']
        return o


