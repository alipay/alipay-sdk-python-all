#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceMailInfoOrderDTO(object):

    def __init__(self):
        self._invoice_ids = None
        self._invoice_mail_date = None
        self._mail_company_name = None
        self._mail_reason = None
        self._mail_type = None
        self._operator = None
        self._recipient_address = None
        self._recipient_name = None
        self._recipient_phone_number = None
        self._sender_address = None
        self._sender_name = None
        self._sender_phone_number = None
        self._tracking_number = None

    @property
    def invoice_ids(self):
        return self._invoice_ids

    @invoice_ids.setter
    def invoice_ids(self, value):
        if isinstance(value, list):
            self._invoice_ids = list()
            for i in value:
                self._invoice_ids.append(i)
    @property
    def invoice_mail_date(self):
        return self._invoice_mail_date

    @invoice_mail_date.setter
    def invoice_mail_date(self, value):
        self._invoice_mail_date = value
    @property
    def mail_company_name(self):
        return self._mail_company_name

    @mail_company_name.setter
    def mail_company_name(self, value):
        self._mail_company_name = value
    @property
    def mail_reason(self):
        return self._mail_reason

    @mail_reason.setter
    def mail_reason(self, value):
        self._mail_reason = value
    @property
    def mail_type(self):
        return self._mail_type

    @mail_type.setter
    def mail_type(self, value):
        self._mail_type = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def recipient_address(self):
        return self._recipient_address

    @recipient_address.setter
    def recipient_address(self, value):
        self._recipient_address = value
    @property
    def recipient_name(self):
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, value):
        self._recipient_name = value
    @property
    def recipient_phone_number(self):
        return self._recipient_phone_number

    @recipient_phone_number.setter
    def recipient_phone_number(self, value):
        self._recipient_phone_number = value
    @property
    def sender_address(self):
        return self._sender_address

    @sender_address.setter
    def sender_address(self, value):
        self._sender_address = value
    @property
    def sender_name(self):
        return self._sender_name

    @sender_name.setter
    def sender_name(self, value):
        self._sender_name = value
    @property
    def sender_phone_number(self):
        return self._sender_phone_number

    @sender_phone_number.setter
    def sender_phone_number(self, value):
        self._sender_phone_number = value
    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, value):
        self._tracking_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_ids:
            if isinstance(self.invoice_ids, list):
                for i in range(0, len(self.invoice_ids)):
                    element = self.invoice_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_ids[i] = element.to_alipay_dict()
            if hasattr(self.invoice_ids, 'to_alipay_dict'):
                params['invoice_ids'] = self.invoice_ids.to_alipay_dict()
            else:
                params['invoice_ids'] = self.invoice_ids
        if self.invoice_mail_date:
            if hasattr(self.invoice_mail_date, 'to_alipay_dict'):
                params['invoice_mail_date'] = self.invoice_mail_date.to_alipay_dict()
            else:
                params['invoice_mail_date'] = self.invoice_mail_date
        if self.mail_company_name:
            if hasattr(self.mail_company_name, 'to_alipay_dict'):
                params['mail_company_name'] = self.mail_company_name.to_alipay_dict()
            else:
                params['mail_company_name'] = self.mail_company_name
        if self.mail_reason:
            if hasattr(self.mail_reason, 'to_alipay_dict'):
                params['mail_reason'] = self.mail_reason.to_alipay_dict()
            else:
                params['mail_reason'] = self.mail_reason
        if self.mail_type:
            if hasattr(self.mail_type, 'to_alipay_dict'):
                params['mail_type'] = self.mail_type.to_alipay_dict()
            else:
                params['mail_type'] = self.mail_type
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.recipient_address:
            if hasattr(self.recipient_address, 'to_alipay_dict'):
                params['recipient_address'] = self.recipient_address.to_alipay_dict()
            else:
                params['recipient_address'] = self.recipient_address
        if self.recipient_name:
            if hasattr(self.recipient_name, 'to_alipay_dict'):
                params['recipient_name'] = self.recipient_name.to_alipay_dict()
            else:
                params['recipient_name'] = self.recipient_name
        if self.recipient_phone_number:
            if hasattr(self.recipient_phone_number, 'to_alipay_dict'):
                params['recipient_phone_number'] = self.recipient_phone_number.to_alipay_dict()
            else:
                params['recipient_phone_number'] = self.recipient_phone_number
        if self.sender_address:
            if hasattr(self.sender_address, 'to_alipay_dict'):
                params['sender_address'] = self.sender_address.to_alipay_dict()
            else:
                params['sender_address'] = self.sender_address
        if self.sender_name:
            if hasattr(self.sender_name, 'to_alipay_dict'):
                params['sender_name'] = self.sender_name.to_alipay_dict()
            else:
                params['sender_name'] = self.sender_name
        if self.sender_phone_number:
            if hasattr(self.sender_phone_number, 'to_alipay_dict'):
                params['sender_phone_number'] = self.sender_phone_number.to_alipay_dict()
            else:
                params['sender_phone_number'] = self.sender_phone_number
        if self.tracking_number:
            if hasattr(self.tracking_number, 'to_alipay_dict'):
                params['tracking_number'] = self.tracking_number.to_alipay_dict()
            else:
                params['tracking_number'] = self.tracking_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceMailInfoOrderDTO()
        if 'invoice_ids' in d:
            o.invoice_ids = d['invoice_ids']
        if 'invoice_mail_date' in d:
            o.invoice_mail_date = d['invoice_mail_date']
        if 'mail_company_name' in d:
            o.mail_company_name = d['mail_company_name']
        if 'mail_reason' in d:
            o.mail_reason = d['mail_reason']
        if 'mail_type' in d:
            o.mail_type = d['mail_type']
        if 'operator' in d:
            o.operator = d['operator']
        if 'recipient_address' in d:
            o.recipient_address = d['recipient_address']
        if 'recipient_name' in d:
            o.recipient_name = d['recipient_name']
        if 'recipient_phone_number' in d:
            o.recipient_phone_number = d['recipient_phone_number']
        if 'sender_address' in d:
            o.sender_address = d['sender_address']
        if 'sender_name' in d:
            o.sender_name = d['sender_name']
        if 'sender_phone_number' in d:
            o.sender_phone_number = d['sender_phone_number']
        if 'tracking_number' in d:
            o.tracking_number = d['tracking_number']
        return o


