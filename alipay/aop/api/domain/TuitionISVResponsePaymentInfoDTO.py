#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO


class TuitionISVResponsePaymentInfoDTO(object):

    def __init__(self):
        self._account_name = None
        self._account_no = None
        self._amount = None
        self._bank_code = None
        self._country = None
        self._deadline = None
        self._payer_identity_card_number = None
        self._payer_phone_number = None
        self._post_script = None
        self._school_name = None
        self._swift_code = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
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
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
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
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def swift_code(self):
        return self._swift_code

    @swift_code.setter
    def swift_code(self, value):
        self._swift_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
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
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.swift_code:
            if hasattr(self.swift_code, 'to_alipay_dict'):
                params['swift_code'] = self.swift_code.to_alipay_dict()
            else:
                params['swift_code'] = self.swift_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVResponsePaymentInfoDTO()
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'country' in d:
            o.country = d['country']
        if 'deadline' in d:
            o.deadline = d['deadline']
        if 'payer_identity_card_number' in d:
            o.payer_identity_card_number = d['payer_identity_card_number']
        if 'payer_phone_number' in d:
            o.payer_phone_number = d['payer_phone_number']
        if 'post_script' in d:
            o.post_script = d['post_script']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'swift_code' in d:
            o.swift_code = d['swift_code']
        return o


