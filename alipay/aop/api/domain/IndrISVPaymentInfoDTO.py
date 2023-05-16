#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrMoneyDTO import IndrMoneyDTO
from alipay.aop.api.domain.IndrISVImageDTO import IndrISVImageDTO


class IndrISVPaymentInfoDTO(object):

    def __init__(self):
        self._amount = None
        self._beneficiary_account_id = None
        self._beneficiary_id = None
        self._certificate_list = None
        self._post_script = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, IndrMoneyDTO):
            self._amount = value
        else:
            self._amount = IndrMoneyDTO.from_alipay_dict(value)
    @property
    def beneficiary_account_id(self):
        return self._beneficiary_account_id

    @beneficiary_account_id.setter
    def beneficiary_account_id(self, value):
        self._beneficiary_account_id = value
    @property
    def beneficiary_id(self):
        return self._beneficiary_id

    @beneficiary_id.setter
    def beneficiary_id(self, value):
        self._beneficiary_id = value
    @property
    def certificate_list(self):
        return self._certificate_list

    @certificate_list.setter
    def certificate_list(self, value):
        if isinstance(value, IndrISVImageDTO):
            self._certificate_list = value
        else:
            self._certificate_list = IndrISVImageDTO.from_alipay_dict(value)
    @property
    def post_script(self):
        return self._post_script

    @post_script.setter
    def post_script(self, value):
        self._post_script = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.beneficiary_account_id:
            if hasattr(self.beneficiary_account_id, 'to_alipay_dict'):
                params['beneficiary_account_id'] = self.beneficiary_account_id.to_alipay_dict()
            else:
                params['beneficiary_account_id'] = self.beneficiary_account_id
        if self.beneficiary_id:
            if hasattr(self.beneficiary_id, 'to_alipay_dict'):
                params['beneficiary_id'] = self.beneficiary_id.to_alipay_dict()
            else:
                params['beneficiary_id'] = self.beneficiary_id
        if self.certificate_list:
            if hasattr(self.certificate_list, 'to_alipay_dict'):
                params['certificate_list'] = self.certificate_list.to_alipay_dict()
            else:
                params['certificate_list'] = self.certificate_list
        if self.post_script:
            if hasattr(self.post_script, 'to_alipay_dict'):
                params['post_script'] = self.post_script.to_alipay_dict()
            else:
                params['post_script'] = self.post_script
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrISVPaymentInfoDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'beneficiary_account_id' in d:
            o.beneficiary_account_id = d['beneficiary_account_id']
        if 'beneficiary_id' in d:
            o.beneficiary_id = d['beneficiary_id']
        if 'certificate_list' in d:
            o.certificate_list = d['certificate_list']
        if 'post_script' in d:
            o.post_script = d['post_script']
        return o


