#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceApplyDTO(object):

    def __init__(self):
        self._apply_amount = None
        self._apply_id = None
        self._batch_id = None
        self._invoice_kind = None
        self._invoice_type = None
        self._payee_register_no = None
        self._payer_address = None
        self._payer_bank_account_id = None
        self._payer_bank_name = None
        self._payer_email = None
        self._payer_name = None
        self._payer_phone = None
        self._payer_register_no = None
        self._recieve_mobile = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def payee_register_no(self):
        return self._payee_register_no

    @payee_register_no.setter
    def payee_register_no(self, value):
        self._payee_register_no = value
    @property
    def payer_address(self):
        return self._payer_address

    @payer_address.setter
    def payer_address(self, value):
        self._payer_address = value
    @property
    def payer_bank_account_id(self):
        return self._payer_bank_account_id

    @payer_bank_account_id.setter
    def payer_bank_account_id(self, value):
        self._payer_bank_account_id = value
    @property
    def payer_bank_name(self):
        return self._payer_bank_name

    @payer_bank_name.setter
    def payer_bank_name(self, value):
        self._payer_bank_name = value
    @property
    def payer_email(self):
        return self._payer_email

    @payer_email.setter
    def payer_email(self, value):
        self._payer_email = value
    @property
    def payer_name(self):
        return self._payer_name

    @payer_name.setter
    def payer_name(self, value):
        self._payer_name = value
    @property
    def payer_phone(self):
        return self._payer_phone

    @payer_phone.setter
    def payer_phone(self, value):
        self._payer_phone = value
    @property
    def payer_register_no(self):
        return self._payer_register_no

    @payer_register_no.setter
    def payer_register_no(self, value):
        self._payer_register_no = value
    @property
    def recieve_mobile(self):
        return self._recieve_mobile

    @recieve_mobile.setter
    def recieve_mobile(self, value):
        self._recieve_mobile = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.payee_register_no:
            if hasattr(self.payee_register_no, 'to_alipay_dict'):
                params['payee_register_no'] = self.payee_register_no.to_alipay_dict()
            else:
                params['payee_register_no'] = self.payee_register_no
        if self.payer_address:
            if hasattr(self.payer_address, 'to_alipay_dict'):
                params['payer_address'] = self.payer_address.to_alipay_dict()
            else:
                params['payer_address'] = self.payer_address
        if self.payer_bank_account_id:
            if hasattr(self.payer_bank_account_id, 'to_alipay_dict'):
                params['payer_bank_account_id'] = self.payer_bank_account_id.to_alipay_dict()
            else:
                params['payer_bank_account_id'] = self.payer_bank_account_id
        if self.payer_bank_name:
            if hasattr(self.payer_bank_name, 'to_alipay_dict'):
                params['payer_bank_name'] = self.payer_bank_name.to_alipay_dict()
            else:
                params['payer_bank_name'] = self.payer_bank_name
        if self.payer_email:
            if hasattr(self.payer_email, 'to_alipay_dict'):
                params['payer_email'] = self.payer_email.to_alipay_dict()
            else:
                params['payer_email'] = self.payer_email
        if self.payer_name:
            if hasattr(self.payer_name, 'to_alipay_dict'):
                params['payer_name'] = self.payer_name.to_alipay_dict()
            else:
                params['payer_name'] = self.payer_name
        if self.payer_phone:
            if hasattr(self.payer_phone, 'to_alipay_dict'):
                params['payer_phone'] = self.payer_phone.to_alipay_dict()
            else:
                params['payer_phone'] = self.payer_phone
        if self.payer_register_no:
            if hasattr(self.payer_register_no, 'to_alipay_dict'):
                params['payer_register_no'] = self.payer_register_no.to_alipay_dict()
            else:
                params['payer_register_no'] = self.payer_register_no
        if self.recieve_mobile:
            if hasattr(self.recieve_mobile, 'to_alipay_dict'):
                params['recieve_mobile'] = self.recieve_mobile.to_alipay_dict()
            else:
                params['recieve_mobile'] = self.recieve_mobile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceApplyDTO()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'payee_register_no' in d:
            o.payee_register_no = d['payee_register_no']
        if 'payer_address' in d:
            o.payer_address = d['payer_address']
        if 'payer_bank_account_id' in d:
            o.payer_bank_account_id = d['payer_bank_account_id']
        if 'payer_bank_name' in d:
            o.payer_bank_name = d['payer_bank_name']
        if 'payer_email' in d:
            o.payer_email = d['payer_email']
        if 'payer_name' in d:
            o.payer_name = d['payer_name']
        if 'payer_phone' in d:
            o.payer_phone = d['payer_phone']
        if 'payer_register_no' in d:
            o.payer_register_no = d['payer_register_no']
        if 'recieve_mobile' in d:
            o.recieve_mobile = d['recieve_mobile']
        return o


