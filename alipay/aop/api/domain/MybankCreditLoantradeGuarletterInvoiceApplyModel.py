#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO


class MybankCreditLoantradeGuarletterInvoiceApplyModel(object):

    def __init__(self):
        self._address = None
        self._apply_user_cert_no = None
        self._apply_user_name = None
        self._bank_card_no = None
        self._bank_name = None
        self._contact_mobile = None
        self._guar_order_no = None
        self._invoice_amt = None
        self._invoice_type = None
        self._phone = None
        self._receive_email = None
        self._request_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def apply_user_cert_no(self):
        return self._apply_user_cert_no

    @apply_user_cert_no.setter
    def apply_user_cert_no(self, value):
        self._apply_user_cert_no = value
    @property
    def apply_user_name(self):
        return self._apply_user_name

    @apply_user_name.setter
    def apply_user_name(self, value):
        self._apply_user_name = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def guar_order_no(self):
        return self._guar_order_no

    @guar_order_no.setter
    def guar_order_no(self, value):
        self._guar_order_no = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._invoice_amt = value
        else:
            self._invoice_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def receive_email(self):
        return self._receive_email

    @receive_email.setter
    def receive_email(self, value):
        self._receive_email = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.apply_user_cert_no:
            if hasattr(self.apply_user_cert_no, 'to_alipay_dict'):
                params['apply_user_cert_no'] = self.apply_user_cert_no.to_alipay_dict()
            else:
                params['apply_user_cert_no'] = self.apply_user_cert_no
        if self.apply_user_name:
            if hasattr(self.apply_user_name, 'to_alipay_dict'):
                params['apply_user_name'] = self.apply_user_name.to_alipay_dict()
            else:
                params['apply_user_name'] = self.apply_user_name
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.guar_order_no:
            if hasattr(self.guar_order_no, 'to_alipay_dict'):
                params['guar_order_no'] = self.guar_order_no.to_alipay_dict()
            else:
                params['guar_order_no'] = self.guar_order_no
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.receive_email:
            if hasattr(self.receive_email, 'to_alipay_dict'):
                params['receive_email'] = self.receive_email.to_alipay_dict()
            else:
                params['receive_email'] = self.receive_email
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeGuarletterInvoiceApplyModel()
        if 'address' in d:
            o.address = d['address']
        if 'apply_user_cert_no' in d:
            o.apply_user_cert_no = d['apply_user_cert_no']
        if 'apply_user_name' in d:
            o.apply_user_name = d['apply_user_name']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'guar_order_no' in d:
            o.guar_order_no = d['guar_order_no']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'receive_email' in d:
            o.receive_email = d['receive_email']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


