#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditGoInfo import CreditGoInfo


class CreditInfoDTO(object):

    def __init__(self):
        self._acceptance_jump_url = None
        self._credit_deposit_period_pay_type = None
        self._credit_go_info = None
        self._credit_product_code = None
        self._no_need_verify_identity = None
        self._out_agreement_no = None
        self._zm_service_id = None

    @property
    def acceptance_jump_url(self):
        return self._acceptance_jump_url

    @acceptance_jump_url.setter
    def acceptance_jump_url(self, value):
        self._acceptance_jump_url = value
    @property
    def credit_deposit_period_pay_type(self):
        return self._credit_deposit_period_pay_type

    @credit_deposit_period_pay_type.setter
    def credit_deposit_period_pay_type(self, value):
        self._credit_deposit_period_pay_type = value
    @property
    def credit_go_info(self):
        return self._credit_go_info

    @credit_go_info.setter
    def credit_go_info(self, value):
        if isinstance(value, CreditGoInfo):
            self._credit_go_info = value
        else:
            self._credit_go_info = CreditGoInfo.from_alipay_dict(value)
    @property
    def credit_product_code(self):
        return self._credit_product_code

    @credit_product_code.setter
    def credit_product_code(self, value):
        self._credit_product_code = value
    @property
    def no_need_verify_identity(self):
        return self._no_need_verify_identity

    @no_need_verify_identity.setter
    def no_need_verify_identity(self, value):
        self._no_need_verify_identity = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_jump_url:
            if hasattr(self.acceptance_jump_url, 'to_alipay_dict'):
                params['acceptance_jump_url'] = self.acceptance_jump_url.to_alipay_dict()
            else:
                params['acceptance_jump_url'] = self.acceptance_jump_url
        if self.credit_deposit_period_pay_type:
            if hasattr(self.credit_deposit_period_pay_type, 'to_alipay_dict'):
                params['credit_deposit_period_pay_type'] = self.credit_deposit_period_pay_type.to_alipay_dict()
            else:
                params['credit_deposit_period_pay_type'] = self.credit_deposit_period_pay_type
        if self.credit_go_info:
            if hasattr(self.credit_go_info, 'to_alipay_dict'):
                params['credit_go_info'] = self.credit_go_info.to_alipay_dict()
            else:
                params['credit_go_info'] = self.credit_go_info
        if self.credit_product_code:
            if hasattr(self.credit_product_code, 'to_alipay_dict'):
                params['credit_product_code'] = self.credit_product_code.to_alipay_dict()
            else:
                params['credit_product_code'] = self.credit_product_code
        if self.no_need_verify_identity:
            if hasattr(self.no_need_verify_identity, 'to_alipay_dict'):
                params['no_need_verify_identity'] = self.no_need_verify_identity.to_alipay_dict()
            else:
                params['no_need_verify_identity'] = self.no_need_verify_identity
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditInfoDTO()
        if 'acceptance_jump_url' in d:
            o.acceptance_jump_url = d['acceptance_jump_url']
        if 'credit_deposit_period_pay_type' in d:
            o.credit_deposit_period_pay_type = d['credit_deposit_period_pay_type']
        if 'credit_go_info' in d:
            o.credit_go_info = d['credit_go_info']
        if 'credit_product_code' in d:
            o.credit_product_code = d['credit_product_code']
        if 'no_need_verify_identity' in d:
            o.no_need_verify_identity = d['no_need_verify_identity']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o


