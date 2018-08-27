#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PersonnalBankAccountInfo(object):

    def __init__(self):
        self._personal_bank_account_mobile = None
        self._personal_bank_card_no = None
        self._personal_bank_holder_certno = None
        self._personal_bank_holder_name = None

    @property
    def personal_bank_account_mobile(self):
        return self._personal_bank_account_mobile

    @personal_bank_account_mobile.setter
    def personal_bank_account_mobile(self, value):
        self._personal_bank_account_mobile = value
    @property
    def personal_bank_card_no(self):
        return self._personal_bank_card_no

    @personal_bank_card_no.setter
    def personal_bank_card_no(self, value):
        self._personal_bank_card_no = value
    @property
    def personal_bank_holder_certno(self):
        return self._personal_bank_holder_certno

    @personal_bank_holder_certno.setter
    def personal_bank_holder_certno(self, value):
        self._personal_bank_holder_certno = value
    @property
    def personal_bank_holder_name(self):
        return self._personal_bank_holder_name

    @personal_bank_holder_name.setter
    def personal_bank_holder_name(self, value):
        self._personal_bank_holder_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.personal_bank_account_mobile:
            if hasattr(self.personal_bank_account_mobile, 'to_alipay_dict'):
                params['personal_bank_account_mobile'] = self.personal_bank_account_mobile.to_alipay_dict()
            else:
                params['personal_bank_account_mobile'] = self.personal_bank_account_mobile
        if self.personal_bank_card_no:
            if hasattr(self.personal_bank_card_no, 'to_alipay_dict'):
                params['personal_bank_card_no'] = self.personal_bank_card_no.to_alipay_dict()
            else:
                params['personal_bank_card_no'] = self.personal_bank_card_no
        if self.personal_bank_holder_certno:
            if hasattr(self.personal_bank_holder_certno, 'to_alipay_dict'):
                params['personal_bank_holder_certno'] = self.personal_bank_holder_certno.to_alipay_dict()
            else:
                params['personal_bank_holder_certno'] = self.personal_bank_holder_certno
        if self.personal_bank_holder_name:
            if hasattr(self.personal_bank_holder_name, 'to_alipay_dict'):
                params['personal_bank_holder_name'] = self.personal_bank_holder_name.to_alipay_dict()
            else:
                params['personal_bank_holder_name'] = self.personal_bank_holder_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PersonnalBankAccountInfo()
        if 'personal_bank_account_mobile' in d:
            o.personal_bank_account_mobile = d['personal_bank_account_mobile']
        if 'personal_bank_card_no' in d:
            o.personal_bank_card_no = d['personal_bank_card_no']
        if 'personal_bank_holder_certno' in d:
            o.personal_bank_holder_certno = d['personal_bank_holder_certno']
        if 'personal_bank_holder_name' in d:
            o.personal_bank_holder_name = d['personal_bank_holder_name']
        return o


