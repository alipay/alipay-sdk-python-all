#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class InvoiceBillResponseDTO(object):

    def __init__(self):
        self._apply_relative_id = None
        self._arrangement_no = None
        self._bill_no = None
        self._bill_type = None
        self._customer_name = None
        self._inst_id = None
        self._inst_name = None
        self._invaccept_receivable_amt = None
        self._invaccept_relevant_amt = None
        self._invoice_receivable_amount = None
        self._invoice_received_amount = None
        self._issued_paid_amount = None
        self._kp_no = None
        self._paid_amount = None
        self._payable_amount = None
        self._settle_status = None
        self._tax_amount = None
        self._to_pay_amount = None
        self._un_invoice_received_amount = None
        self._wroteoff_amount = None

    @property
    def apply_relative_id(self):
        return self._apply_relative_id

    @apply_relative_id.setter
    def apply_relative_id(self, value):
        self._apply_relative_id = value
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def invaccept_receivable_amt(self):
        return self._invaccept_receivable_amt

    @invaccept_receivable_amt.setter
    def invaccept_receivable_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invaccept_receivable_amt = value
        else:
            self._invaccept_receivable_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invaccept_relevant_amt(self):
        return self._invaccept_relevant_amt

    @invaccept_relevant_amt.setter
    def invaccept_relevant_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invaccept_relevant_amt = value
        else:
            self._invaccept_relevant_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_receivable_amount(self):
        return self._invoice_receivable_amount

    @invoice_receivable_amount.setter
    def invoice_receivable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_receivable_amount = value
        else:
            self._invoice_receivable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice_received_amount(self):
        return self._invoice_received_amount

    @invoice_received_amount.setter
    def invoice_received_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._invoice_received_amount = value
        else:
            self._invoice_received_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def issued_paid_amount(self):
        return self._issued_paid_amount

    @issued_paid_amount.setter
    def issued_paid_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._issued_paid_amount = value
        else:
            self._issued_paid_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def kp_no(self):
        return self._kp_no

    @kp_no.setter
    def kp_no(self, value):
        self._kp_no = value
    @property
    def paid_amount(self):
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._paid_amount = value
        else:
            self._paid_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def payable_amount(self):
        return self._payable_amount

    @payable_amount.setter
    def payable_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._payable_amount = value
        else:
            self._payable_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_amount = value
        else:
            self._tax_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def to_pay_amount(self):
        return self._to_pay_amount

    @to_pay_amount.setter
    def to_pay_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._to_pay_amount = value
        else:
            self._to_pay_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def un_invoice_received_amount(self):
        return self._un_invoice_received_amount

    @un_invoice_received_amount.setter
    def un_invoice_received_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._un_invoice_received_amount = value
        else:
            self._un_invoice_received_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def wroteoff_amount(self):
        return self._wroteoff_amount

    @wroteoff_amount.setter
    def wroteoff_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._wroteoff_amount = value
        else:
            self._wroteoff_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_relative_id:
            if hasattr(self.apply_relative_id, 'to_alipay_dict'):
                params['apply_relative_id'] = self.apply_relative_id.to_alipay_dict()
            else:
                params['apply_relative_id'] = self.apply_relative_id
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.invaccept_receivable_amt:
            if hasattr(self.invaccept_receivable_amt, 'to_alipay_dict'):
                params['invaccept_receivable_amt'] = self.invaccept_receivable_amt.to_alipay_dict()
            else:
                params['invaccept_receivable_amt'] = self.invaccept_receivable_amt
        if self.invaccept_relevant_amt:
            if hasattr(self.invaccept_relevant_amt, 'to_alipay_dict'):
                params['invaccept_relevant_amt'] = self.invaccept_relevant_amt.to_alipay_dict()
            else:
                params['invaccept_relevant_amt'] = self.invaccept_relevant_amt
        if self.invoice_receivable_amount:
            if hasattr(self.invoice_receivable_amount, 'to_alipay_dict'):
                params['invoice_receivable_amount'] = self.invoice_receivable_amount.to_alipay_dict()
            else:
                params['invoice_receivable_amount'] = self.invoice_receivable_amount
        if self.invoice_received_amount:
            if hasattr(self.invoice_received_amount, 'to_alipay_dict'):
                params['invoice_received_amount'] = self.invoice_received_amount.to_alipay_dict()
            else:
                params['invoice_received_amount'] = self.invoice_received_amount
        if self.issued_paid_amount:
            if hasattr(self.issued_paid_amount, 'to_alipay_dict'):
                params['issued_paid_amount'] = self.issued_paid_amount.to_alipay_dict()
            else:
                params['issued_paid_amount'] = self.issued_paid_amount
        if self.kp_no:
            if hasattr(self.kp_no, 'to_alipay_dict'):
                params['kp_no'] = self.kp_no.to_alipay_dict()
            else:
                params['kp_no'] = self.kp_no
        if self.paid_amount:
            if hasattr(self.paid_amount, 'to_alipay_dict'):
                params['paid_amount'] = self.paid_amount.to_alipay_dict()
            else:
                params['paid_amount'] = self.paid_amount
        if self.payable_amount:
            if hasattr(self.payable_amount, 'to_alipay_dict'):
                params['payable_amount'] = self.payable_amount.to_alipay_dict()
            else:
                params['payable_amount'] = self.payable_amount
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.to_pay_amount:
            if hasattr(self.to_pay_amount, 'to_alipay_dict'):
                params['to_pay_amount'] = self.to_pay_amount.to_alipay_dict()
            else:
                params['to_pay_amount'] = self.to_pay_amount
        if self.un_invoice_received_amount:
            if hasattr(self.un_invoice_received_amount, 'to_alipay_dict'):
                params['un_invoice_received_amount'] = self.un_invoice_received_amount.to_alipay_dict()
            else:
                params['un_invoice_received_amount'] = self.un_invoice_received_amount
        if self.wroteoff_amount:
            if hasattr(self.wroteoff_amount, 'to_alipay_dict'):
                params['wroteoff_amount'] = self.wroteoff_amount.to_alipay_dict()
            else:
                params['wroteoff_amount'] = self.wroteoff_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceBillResponseDTO()
        if 'apply_relative_id' in d:
            o.apply_relative_id = d['apply_relative_id']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'invaccept_receivable_amt' in d:
            o.invaccept_receivable_amt = d['invaccept_receivable_amt']
        if 'invaccept_relevant_amt' in d:
            o.invaccept_relevant_amt = d['invaccept_relevant_amt']
        if 'invoice_receivable_amount' in d:
            o.invoice_receivable_amount = d['invoice_receivable_amount']
        if 'invoice_received_amount' in d:
            o.invoice_received_amount = d['invoice_received_amount']
        if 'issued_paid_amount' in d:
            o.issued_paid_amount = d['issued_paid_amount']
        if 'kp_no' in d:
            o.kp_no = d['kp_no']
        if 'paid_amount' in d:
            o.paid_amount = d['paid_amount']
        if 'payable_amount' in d:
            o.payable_amount = d['payable_amount']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'to_pay_amount' in d:
            o.to_pay_amount = d['to_pay_amount']
        if 'un_invoice_received_amount' in d:
            o.un_invoice_received_amount = d['un_invoice_received_amount']
        if 'wroteoff_amount' in d:
            o.wroteoff_amount = d['wroteoff_amount']
        return o


