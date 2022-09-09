#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ClaimAdvancePaymentDTO import ClaimAdvancePaymentDTO


class AlipayInsSceneClaimAdvancepaySyncModel(object):

    def __init__(self):
        self._advance_payment = None
        self._claim_report_no = None
        self._out_order_id = None
        self._partner_org_id = None
        self._policy_no = None

    @property
    def advance_payment(self):
        return self._advance_payment

    @advance_payment.setter
    def advance_payment(self, value):
        if isinstance(value, ClaimAdvancePaymentDTO):
            self._advance_payment = value
        else:
            self._advance_payment = ClaimAdvancePaymentDTO.from_alipay_dict(value)
    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
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
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_payment:
            if hasattr(self.advance_payment, 'to_alipay_dict'):
                params['advance_payment'] = self.advance_payment.to_alipay_dict()
            else:
                params['advance_payment'] = self.advance_payment
        if self.claim_report_no:
            if hasattr(self.claim_report_no, 'to_alipay_dict'):
                params['claim_report_no'] = self.claim_report_no.to_alipay_dict()
            else:
                params['claim_report_no'] = self.claim_report_no
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
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneClaimAdvancepaySyncModel()
        if 'advance_payment' in d:
            o.advance_payment = d['advance_payment']
        if 'claim_report_no' in d:
            o.claim_report_no = d['claim_report_no']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        return o


