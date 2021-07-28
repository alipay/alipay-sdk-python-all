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


class PaymentApplyResponseDTO(object):

    def __init__(self):
        self._apply_relative_id = None
        self._arrangement_no = None
        self._bill_type = None
        self._customer_name = None
        self._guarantee_noney = None
        self._inst_id = None
        self._inst_name = None
        self._invaccept_receivable_amt = None
        self._invaccept_relevant_amt = None
        self._invoice_receivable_amount = None
        self._invoice_received_amount = None
        self._issued_paid_amount = None
        self._kp_no = None
        self._paid_amount = None
        self._pay_contract_desc = None
        self._pay_contract_item_no = None
        self._payable_amount = None
        self._rt_no = None
        self._settle_status = None
        self._source = None
        self._stage = None
        self._tax_account_no = None
        self._tax_address = None
        self._tax_amount = None
        self._tax_bank_name = None
        self._tax_invoice_title = None
        self._tax_phone_no = None
        self._tax_rate = None
        self._tax_tax_no = None
        self._tax_type = None
        self._tax_type_desc = None
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
    def guarantee_noney(self):
        return self._guarantee_noney

    @guarantee_noney.setter
    def guarantee_noney(self, value):
        self._guarantee_noney = value
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
    def pay_contract_desc(self):
        return self._pay_contract_desc

    @pay_contract_desc.setter
    def pay_contract_desc(self, value):
        self._pay_contract_desc = value
    @property
    def pay_contract_item_no(self):
        return self._pay_contract_item_no

    @pay_contract_item_no.setter
    def pay_contract_item_no(self, value):
        self._pay_contract_item_no = value
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
    def rt_no(self):
        return self._rt_no

    @rt_no.setter
    def rt_no(self, value):
        self._rt_no = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value
    @property
    def tax_account_no(self):
        return self._tax_account_no

    @tax_account_no.setter
    def tax_account_no(self, value):
        self._tax_account_no = value
    @property
    def tax_address(self):
        return self._tax_address

    @tax_address.setter
    def tax_address(self, value):
        self._tax_address = value
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
    def tax_bank_name(self):
        return self._tax_bank_name

    @tax_bank_name.setter
    def tax_bank_name(self, value):
        self._tax_bank_name = value
    @property
    def tax_invoice_title(self):
        return self._tax_invoice_title

    @tax_invoice_title.setter
    def tax_invoice_title(self, value):
        self._tax_invoice_title = value
    @property
    def tax_phone_no(self):
        return self._tax_phone_no

    @tax_phone_no.setter
    def tax_phone_no(self, value):
        self._tax_phone_no = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tax_tax_no(self):
        return self._tax_tax_no

    @tax_tax_no.setter
    def tax_tax_no(self, value):
        self._tax_tax_no = value
    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, value):
        self._tax_type = value
    @property
    def tax_type_desc(self):
        return self._tax_type_desc

    @tax_type_desc.setter
    def tax_type_desc(self, value):
        self._tax_type_desc = value
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
        if self.guarantee_noney:
            if hasattr(self.guarantee_noney, 'to_alipay_dict'):
                params['guarantee_noney'] = self.guarantee_noney.to_alipay_dict()
            else:
                params['guarantee_noney'] = self.guarantee_noney
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
        if self.pay_contract_desc:
            if hasattr(self.pay_contract_desc, 'to_alipay_dict'):
                params['pay_contract_desc'] = self.pay_contract_desc.to_alipay_dict()
            else:
                params['pay_contract_desc'] = self.pay_contract_desc
        if self.pay_contract_item_no:
            if hasattr(self.pay_contract_item_no, 'to_alipay_dict'):
                params['pay_contract_item_no'] = self.pay_contract_item_no.to_alipay_dict()
            else:
                params['pay_contract_item_no'] = self.pay_contract_item_no
        if self.payable_amount:
            if hasattr(self.payable_amount, 'to_alipay_dict'):
                params['payable_amount'] = self.payable_amount.to_alipay_dict()
            else:
                params['payable_amount'] = self.payable_amount
        if self.rt_no:
            if hasattr(self.rt_no, 'to_alipay_dict'):
                params['rt_no'] = self.rt_no.to_alipay_dict()
            else:
                params['rt_no'] = self.rt_no
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
        if self.tax_account_no:
            if hasattr(self.tax_account_no, 'to_alipay_dict'):
                params['tax_account_no'] = self.tax_account_no.to_alipay_dict()
            else:
                params['tax_account_no'] = self.tax_account_no
        if self.tax_address:
            if hasattr(self.tax_address, 'to_alipay_dict'):
                params['tax_address'] = self.tax_address.to_alipay_dict()
            else:
                params['tax_address'] = self.tax_address
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_bank_name:
            if hasattr(self.tax_bank_name, 'to_alipay_dict'):
                params['tax_bank_name'] = self.tax_bank_name.to_alipay_dict()
            else:
                params['tax_bank_name'] = self.tax_bank_name
        if self.tax_invoice_title:
            if hasattr(self.tax_invoice_title, 'to_alipay_dict'):
                params['tax_invoice_title'] = self.tax_invoice_title.to_alipay_dict()
            else:
                params['tax_invoice_title'] = self.tax_invoice_title
        if self.tax_phone_no:
            if hasattr(self.tax_phone_no, 'to_alipay_dict'):
                params['tax_phone_no'] = self.tax_phone_no.to_alipay_dict()
            else:
                params['tax_phone_no'] = self.tax_phone_no
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tax_tax_no:
            if hasattr(self.tax_tax_no, 'to_alipay_dict'):
                params['tax_tax_no'] = self.tax_tax_no.to_alipay_dict()
            else:
                params['tax_tax_no'] = self.tax_tax_no
        if self.tax_type:
            if hasattr(self.tax_type, 'to_alipay_dict'):
                params['tax_type'] = self.tax_type.to_alipay_dict()
            else:
                params['tax_type'] = self.tax_type
        if self.tax_type_desc:
            if hasattr(self.tax_type_desc, 'to_alipay_dict'):
                params['tax_type_desc'] = self.tax_type_desc.to_alipay_dict()
            else:
                params['tax_type_desc'] = self.tax_type_desc
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
        o = PaymentApplyResponseDTO()
        if 'apply_relative_id' in d:
            o.apply_relative_id = d['apply_relative_id']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'guarantee_noney' in d:
            o.guarantee_noney = d['guarantee_noney']
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
        if 'pay_contract_desc' in d:
            o.pay_contract_desc = d['pay_contract_desc']
        if 'pay_contract_item_no' in d:
            o.pay_contract_item_no = d['pay_contract_item_no']
        if 'payable_amount' in d:
            o.payable_amount = d['payable_amount']
        if 'rt_no' in d:
            o.rt_no = d['rt_no']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'source' in d:
            o.source = d['source']
        if 'stage' in d:
            o.stage = d['stage']
        if 'tax_account_no' in d:
            o.tax_account_no = d['tax_account_no']
        if 'tax_address' in d:
            o.tax_address = d['tax_address']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_bank_name' in d:
            o.tax_bank_name = d['tax_bank_name']
        if 'tax_invoice_title' in d:
            o.tax_invoice_title = d['tax_invoice_title']
        if 'tax_phone_no' in d:
            o.tax_phone_no = d['tax_phone_no']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_tax_no' in d:
            o.tax_tax_no = d['tax_tax_no']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        if 'tax_type_desc' in d:
            o.tax_type_desc = d['tax_type_desc']
        if 'to_pay_amount' in d:
            o.to_pay_amount = d['to_pay_amount']
        if 'un_invoice_received_amount' in d:
            o.un_invoice_received_amount = d['un_invoice_received_amount']
        if 'wroteoff_amount' in d:
            o.wroteoff_amount = d['wroteoff_amount']
        return o


