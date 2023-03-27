#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlcollectioncenterUserDTO import AlcollectioncenterUserDTO
from alipay.aop.api.domain.AlcollectioncenterUserDTO import AlcollectioncenterUserDTO
from alipay.aop.api.domain.AlcollectioncenterUserDTO import AlcollectioncenterUserDTO
from alipay.aop.api.domain.AlcollectioncenterUserDTO import AlcollectioncenterUserDTO
from alipay.aop.api.domain.AlcollectioncenterUserDTO import AlcollectioncenterUserDTO


class OurSubjectInfoDTO(object):

    def __init__(self):
        self._bank_code = None
        self._deposit_bank = None
        self._entity_id = None
        self._operator = None
        self._ou_code = None
        self._our_bank_account = None
        self._our_biz_bu = None
        self._our_biz_principal = None
        self._our_contact_email = None
        self._our_contact_name = None
        self._our_contact_no = None
        self._our_contact_phone = None
        self._our_finance_principal = None
        self._our_middle_ground_principal = None
        self._our_payee_account_name = None
        self._our_settle_principal = None
        self._our_subject = None
        self._our_subject_id = None

    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def deposit_bank(self):
        return self._deposit_bank

    @deposit_bank.setter
    def deposit_bank(self, value):
        self._deposit_bank = value
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        if isinstance(value, AlcollectioncenterUserDTO):
            self._operator = value
        else:
            self._operator = AlcollectioncenterUserDTO.from_alipay_dict(value)
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def our_bank_account(self):
        return self._our_bank_account

    @our_bank_account.setter
    def our_bank_account(self, value):
        self._our_bank_account = value
    @property
    def our_biz_bu(self):
        return self._our_biz_bu

    @our_biz_bu.setter
    def our_biz_bu(self, value):
        self._our_biz_bu = value
    @property
    def our_biz_principal(self):
        return self._our_biz_principal

    @our_biz_principal.setter
    def our_biz_principal(self, value):
        if isinstance(value, AlcollectioncenterUserDTO):
            self._our_biz_principal = value
        else:
            self._our_biz_principal = AlcollectioncenterUserDTO.from_alipay_dict(value)
    @property
    def our_contact_email(self):
        return self._our_contact_email

    @our_contact_email.setter
    def our_contact_email(self, value):
        self._our_contact_email = value
    @property
    def our_contact_name(self):
        return self._our_contact_name

    @our_contact_name.setter
    def our_contact_name(self, value):
        self._our_contact_name = value
    @property
    def our_contact_no(self):
        return self._our_contact_no

    @our_contact_no.setter
    def our_contact_no(self, value):
        self._our_contact_no = value
    @property
    def our_contact_phone(self):
        return self._our_contact_phone

    @our_contact_phone.setter
    def our_contact_phone(self, value):
        self._our_contact_phone = value
    @property
    def our_finance_principal(self):
        return self._our_finance_principal

    @our_finance_principal.setter
    def our_finance_principal(self, value):
        if isinstance(value, AlcollectioncenterUserDTO):
            self._our_finance_principal = value
        else:
            self._our_finance_principal = AlcollectioncenterUserDTO.from_alipay_dict(value)
    @property
    def our_middle_ground_principal(self):
        return self._our_middle_ground_principal

    @our_middle_ground_principal.setter
    def our_middle_ground_principal(self, value):
        if isinstance(value, AlcollectioncenterUserDTO):
            self._our_middle_ground_principal = value
        else:
            self._our_middle_ground_principal = AlcollectioncenterUserDTO.from_alipay_dict(value)
    @property
    def our_payee_account_name(self):
        return self._our_payee_account_name

    @our_payee_account_name.setter
    def our_payee_account_name(self, value):
        self._our_payee_account_name = value
    @property
    def our_settle_principal(self):
        return self._our_settle_principal

    @our_settle_principal.setter
    def our_settle_principal(self, value):
        if isinstance(value, AlcollectioncenterUserDTO):
            self._our_settle_principal = value
        else:
            self._our_settle_principal = AlcollectioncenterUserDTO.from_alipay_dict(value)
    @property
    def our_subject(self):
        return self._our_subject

    @our_subject.setter
    def our_subject(self, value):
        self._our_subject = value
    @property
    def our_subject_id(self):
        return self._our_subject_id

    @our_subject_id.setter
    def our_subject_id(self, value):
        self._our_subject_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.deposit_bank:
            if hasattr(self.deposit_bank, 'to_alipay_dict'):
                params['deposit_bank'] = self.deposit_bank.to_alipay_dict()
            else:
                params['deposit_bank'] = self.deposit_bank
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.our_bank_account:
            if hasattr(self.our_bank_account, 'to_alipay_dict'):
                params['our_bank_account'] = self.our_bank_account.to_alipay_dict()
            else:
                params['our_bank_account'] = self.our_bank_account
        if self.our_biz_bu:
            if hasattr(self.our_biz_bu, 'to_alipay_dict'):
                params['our_biz_bu'] = self.our_biz_bu.to_alipay_dict()
            else:
                params['our_biz_bu'] = self.our_biz_bu
        if self.our_biz_principal:
            if hasattr(self.our_biz_principal, 'to_alipay_dict'):
                params['our_biz_principal'] = self.our_biz_principal.to_alipay_dict()
            else:
                params['our_biz_principal'] = self.our_biz_principal
        if self.our_contact_email:
            if hasattr(self.our_contact_email, 'to_alipay_dict'):
                params['our_contact_email'] = self.our_contact_email.to_alipay_dict()
            else:
                params['our_contact_email'] = self.our_contact_email
        if self.our_contact_name:
            if hasattr(self.our_contact_name, 'to_alipay_dict'):
                params['our_contact_name'] = self.our_contact_name.to_alipay_dict()
            else:
                params['our_contact_name'] = self.our_contact_name
        if self.our_contact_no:
            if hasattr(self.our_contact_no, 'to_alipay_dict'):
                params['our_contact_no'] = self.our_contact_no.to_alipay_dict()
            else:
                params['our_contact_no'] = self.our_contact_no
        if self.our_contact_phone:
            if hasattr(self.our_contact_phone, 'to_alipay_dict'):
                params['our_contact_phone'] = self.our_contact_phone.to_alipay_dict()
            else:
                params['our_contact_phone'] = self.our_contact_phone
        if self.our_finance_principal:
            if hasattr(self.our_finance_principal, 'to_alipay_dict'):
                params['our_finance_principal'] = self.our_finance_principal.to_alipay_dict()
            else:
                params['our_finance_principal'] = self.our_finance_principal
        if self.our_middle_ground_principal:
            if hasattr(self.our_middle_ground_principal, 'to_alipay_dict'):
                params['our_middle_ground_principal'] = self.our_middle_ground_principal.to_alipay_dict()
            else:
                params['our_middle_ground_principal'] = self.our_middle_ground_principal
        if self.our_payee_account_name:
            if hasattr(self.our_payee_account_name, 'to_alipay_dict'):
                params['our_payee_account_name'] = self.our_payee_account_name.to_alipay_dict()
            else:
                params['our_payee_account_name'] = self.our_payee_account_name
        if self.our_settle_principal:
            if hasattr(self.our_settle_principal, 'to_alipay_dict'):
                params['our_settle_principal'] = self.our_settle_principal.to_alipay_dict()
            else:
                params['our_settle_principal'] = self.our_settle_principal
        if self.our_subject:
            if hasattr(self.our_subject, 'to_alipay_dict'):
                params['our_subject'] = self.our_subject.to_alipay_dict()
            else:
                params['our_subject'] = self.our_subject
        if self.our_subject_id:
            if hasattr(self.our_subject_id, 'to_alipay_dict'):
                params['our_subject_id'] = self.our_subject_id.to_alipay_dict()
            else:
                params['our_subject_id'] = self.our_subject_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OurSubjectInfoDTO()
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'deposit_bank' in d:
            o.deposit_bank = d['deposit_bank']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'our_bank_account' in d:
            o.our_bank_account = d['our_bank_account']
        if 'our_biz_bu' in d:
            o.our_biz_bu = d['our_biz_bu']
        if 'our_biz_principal' in d:
            o.our_biz_principal = d['our_biz_principal']
        if 'our_contact_email' in d:
            o.our_contact_email = d['our_contact_email']
        if 'our_contact_name' in d:
            o.our_contact_name = d['our_contact_name']
        if 'our_contact_no' in d:
            o.our_contact_no = d['our_contact_no']
        if 'our_contact_phone' in d:
            o.our_contact_phone = d['our_contact_phone']
        if 'our_finance_principal' in d:
            o.our_finance_principal = d['our_finance_principal']
        if 'our_middle_ground_principal' in d:
            o.our_middle_ground_principal = d['our_middle_ground_principal']
        if 'our_payee_account_name' in d:
            o.our_payee_account_name = d['our_payee_account_name']
        if 'our_settle_principal' in d:
            o.our_settle_principal = d['our_settle_principal']
        if 'our_subject' in d:
            o.our_subject = d['our_subject']
        if 'our_subject_id' in d:
            o.our_subject_id = d['our_subject_id']
        return o


