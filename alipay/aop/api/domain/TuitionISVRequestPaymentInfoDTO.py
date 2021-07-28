#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO


class TuitionISVRequestPaymentInfoDTO(object):

    def __init__(self):
        self._account_id = None
        self._amount = None
        self._certificate_list = None
        self._deadline = None
        self._payer_identity_card_number = None
        self._payer_phone_number = None
        self._post_script = None
        self._school_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, TuitionMoneyDTO):
            self._amount = value
        else:
            self._amount = TuitionMoneyDTO.from_alipay_dict(value)
    @property
    def certificate_list(self):
        return self._certificate_list

    @certificate_list.setter
    def certificate_list(self, value):
        self._certificate_list = value
    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value
    @property
    def payer_identity_card_number(self):
        return self._payer_identity_card_number

    @payer_identity_card_number.setter
    def payer_identity_card_number(self, value):
        self._payer_identity_card_number = value
    @property
    def payer_phone_number(self):
        return self._payer_phone_number

    @payer_phone_number.setter
    def payer_phone_number(self, value):
        self._payer_phone_number = value
    @property
    def post_script(self):
        return self._post_script

    @post_script.setter
    def post_script(self, value):
        self._post_script = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.certificate_list:
            if hasattr(self.certificate_list, 'to_alipay_dict'):
                params['certificate_list'] = self.certificate_list.to_alipay_dict()
            else:
                params['certificate_list'] = self.certificate_list
        if self.deadline:
            if hasattr(self.deadline, 'to_alipay_dict'):
                params['deadline'] = self.deadline.to_alipay_dict()
            else:
                params['deadline'] = self.deadline
        if self.payer_identity_card_number:
            if hasattr(self.payer_identity_card_number, 'to_alipay_dict'):
                params['payer_identity_card_number'] = self.payer_identity_card_number.to_alipay_dict()
            else:
                params['payer_identity_card_number'] = self.payer_identity_card_number
        if self.payer_phone_number:
            if hasattr(self.payer_phone_number, 'to_alipay_dict'):
                params['payer_phone_number'] = self.payer_phone_number.to_alipay_dict()
            else:
                params['payer_phone_number'] = self.payer_phone_number
        if self.post_script:
            if hasattr(self.post_script, 'to_alipay_dict'):
                params['post_script'] = self.post_script.to_alipay_dict()
            else:
                params['post_script'] = self.post_script
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVRequestPaymentInfoDTO()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'amount' in d:
            o.amount = d['amount']
        if 'certificate_list' in d:
            o.certificate_list = d['certificate_list']
        if 'deadline' in d:
            o.deadline = d['deadline']
        if 'payer_identity_card_number' in d:
            o.payer_identity_card_number = d['payer_identity_card_number']
        if 'payer_phone_number' in d:
            o.payer_phone_number = d['payer_phone_number']
        if 'post_script' in d:
            o.post_script = d['post_script']
        if 'school_id' in d:
            o.school_id = d['school_id']
        return o


