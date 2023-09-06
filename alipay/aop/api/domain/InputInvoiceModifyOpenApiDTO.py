#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputInvoiceModifyOpenApiDTO(object):

    def __init__(self):
        self._amount = None
        self._authorized_dealer = None
        self._check_sum = None
        self._cipher_text = None
        self._currency = None
        self._effective_tax_amount = None
        self._excluding_tax_amount = None
        self._invoice_code = None
        self._invoice_id = None
        self._invoice_material = None
        self._invoice_no = None
        self._invoice_remark = None
        self._issued_seller_name = None
        self._issued_tax_no = None
        self._machine_code = None
        self._purchaser_bank_info = None
        self._purchaser_code = None
        self._purchaser_contact_info = None
        self._purchaser_country_code = None
        self._purchaser_name = None
        self._purchaser_region_code = None
        self._purchaser_tax_no = None
        self._qr_code_flag = None
        self._related_order = None
        self._seller_bank_info = None
        self._seller_code = None
        self._seller_contact_info = None
        self._seller_country_code = None
        self._seller_name = None
        self._seller_region_code = None
        self._seller_tax_no = None
        self._tax_amount = None
        self._tax_rate = None
        self._waybill_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def authorized_dealer(self):
        return self._authorized_dealer

    @authorized_dealer.setter
    def authorized_dealer(self, value):
        self._authorized_dealer = value
    @property
    def check_sum(self):
        return self._check_sum

    @check_sum.setter
    def check_sum(self, value):
        self._check_sum = value
    @property
    def cipher_text(self):
        return self._cipher_text

    @cipher_text.setter
    def cipher_text(self, value):
        self._cipher_text = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def effective_tax_amount(self):
        return self._effective_tax_amount

    @effective_tax_amount.setter
    def effective_tax_amount(self, value):
        self._effective_tax_amount = value
    @property
    def excluding_tax_amount(self):
        return self._excluding_tax_amount

    @excluding_tax_amount.setter
    def excluding_tax_amount(self, value):
        self._excluding_tax_amount = value
    @property
    def invoice_code(self):
        return self._invoice_code

    @invoice_code.setter
    def invoice_code(self, value):
        self._invoice_code = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_remark(self):
        return self._invoice_remark

    @invoice_remark.setter
    def invoice_remark(self, value):
        self._invoice_remark = value
    @property
    def issued_seller_name(self):
        return self._issued_seller_name

    @issued_seller_name.setter
    def issued_seller_name(self, value):
        self._issued_seller_name = value
    @property
    def issued_tax_no(self):
        return self._issued_tax_no

    @issued_tax_no.setter
    def issued_tax_no(self, value):
        self._issued_tax_no = value
    @property
    def machine_code(self):
        return self._machine_code

    @machine_code.setter
    def machine_code(self, value):
        self._machine_code = value
    @property
    def purchaser_bank_info(self):
        return self._purchaser_bank_info

    @purchaser_bank_info.setter
    def purchaser_bank_info(self, value):
        self._purchaser_bank_info = value
    @property
    def purchaser_code(self):
        return self._purchaser_code

    @purchaser_code.setter
    def purchaser_code(self, value):
        self._purchaser_code = value
    @property
    def purchaser_contact_info(self):
        return self._purchaser_contact_info

    @purchaser_contact_info.setter
    def purchaser_contact_info(self, value):
        self._purchaser_contact_info = value
    @property
    def purchaser_country_code(self):
        return self._purchaser_country_code

    @purchaser_country_code.setter
    def purchaser_country_code(self, value):
        self._purchaser_country_code = value
    @property
    def purchaser_name(self):
        return self._purchaser_name

    @purchaser_name.setter
    def purchaser_name(self, value):
        self._purchaser_name = value
    @property
    def purchaser_region_code(self):
        return self._purchaser_region_code

    @purchaser_region_code.setter
    def purchaser_region_code(self, value):
        self._purchaser_region_code = value
    @property
    def purchaser_tax_no(self):
        return self._purchaser_tax_no

    @purchaser_tax_no.setter
    def purchaser_tax_no(self, value):
        self._purchaser_tax_no = value
    @property
    def qr_code_flag(self):
        return self._qr_code_flag

    @qr_code_flag.setter
    def qr_code_flag(self, value):
        self._qr_code_flag = value
    @property
    def related_order(self):
        return self._related_order

    @related_order.setter
    def related_order(self, value):
        self._related_order = value
    @property
    def seller_bank_info(self):
        return self._seller_bank_info

    @seller_bank_info.setter
    def seller_bank_info(self, value):
        self._seller_bank_info = value
    @property
    def seller_code(self):
        return self._seller_code

    @seller_code.setter
    def seller_code(self, value):
        self._seller_code = value
    @property
    def seller_contact_info(self):
        return self._seller_contact_info

    @seller_contact_info.setter
    def seller_contact_info(self, value):
        self._seller_contact_info = value
    @property
    def seller_country_code(self):
        return self._seller_country_code

    @seller_country_code.setter
    def seller_country_code(self, value):
        self._seller_country_code = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def seller_region_code(self):
        return self._seller_region_code

    @seller_region_code.setter
    def seller_region_code(self, value):
        self._seller_region_code = value
    @property
    def seller_tax_no(self):
        return self._seller_tax_no

    @seller_tax_no.setter
    def seller_tax_no(self, value):
        self._seller_tax_no = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.authorized_dealer:
            if hasattr(self.authorized_dealer, 'to_alipay_dict'):
                params['authorized_dealer'] = self.authorized_dealer.to_alipay_dict()
            else:
                params['authorized_dealer'] = self.authorized_dealer
        if self.check_sum:
            if hasattr(self.check_sum, 'to_alipay_dict'):
                params['check_sum'] = self.check_sum.to_alipay_dict()
            else:
                params['check_sum'] = self.check_sum
        if self.cipher_text:
            if hasattr(self.cipher_text, 'to_alipay_dict'):
                params['cipher_text'] = self.cipher_text.to_alipay_dict()
            else:
                params['cipher_text'] = self.cipher_text
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.effective_tax_amount:
            if hasattr(self.effective_tax_amount, 'to_alipay_dict'):
                params['effective_tax_amount'] = self.effective_tax_amount.to_alipay_dict()
            else:
                params['effective_tax_amount'] = self.effective_tax_amount
        if self.excluding_tax_amount:
            if hasattr(self.excluding_tax_amount, 'to_alipay_dict'):
                params['excluding_tax_amount'] = self.excluding_tax_amount.to_alipay_dict()
            else:
                params['excluding_tax_amount'] = self.excluding_tax_amount
        if self.invoice_code:
            if hasattr(self.invoice_code, 'to_alipay_dict'):
                params['invoice_code'] = self.invoice_code.to_alipay_dict()
            else:
                params['invoice_code'] = self.invoice_code
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_remark:
            if hasattr(self.invoice_remark, 'to_alipay_dict'):
                params['invoice_remark'] = self.invoice_remark.to_alipay_dict()
            else:
                params['invoice_remark'] = self.invoice_remark
        if self.issued_seller_name:
            if hasattr(self.issued_seller_name, 'to_alipay_dict'):
                params['issued_seller_name'] = self.issued_seller_name.to_alipay_dict()
            else:
                params['issued_seller_name'] = self.issued_seller_name
        if self.issued_tax_no:
            if hasattr(self.issued_tax_no, 'to_alipay_dict'):
                params['issued_tax_no'] = self.issued_tax_no.to_alipay_dict()
            else:
                params['issued_tax_no'] = self.issued_tax_no
        if self.machine_code:
            if hasattr(self.machine_code, 'to_alipay_dict'):
                params['machine_code'] = self.machine_code.to_alipay_dict()
            else:
                params['machine_code'] = self.machine_code
        if self.purchaser_bank_info:
            if hasattr(self.purchaser_bank_info, 'to_alipay_dict'):
                params['purchaser_bank_info'] = self.purchaser_bank_info.to_alipay_dict()
            else:
                params['purchaser_bank_info'] = self.purchaser_bank_info
        if self.purchaser_code:
            if hasattr(self.purchaser_code, 'to_alipay_dict'):
                params['purchaser_code'] = self.purchaser_code.to_alipay_dict()
            else:
                params['purchaser_code'] = self.purchaser_code
        if self.purchaser_contact_info:
            if hasattr(self.purchaser_contact_info, 'to_alipay_dict'):
                params['purchaser_contact_info'] = self.purchaser_contact_info.to_alipay_dict()
            else:
                params['purchaser_contact_info'] = self.purchaser_contact_info
        if self.purchaser_country_code:
            if hasattr(self.purchaser_country_code, 'to_alipay_dict'):
                params['purchaser_country_code'] = self.purchaser_country_code.to_alipay_dict()
            else:
                params['purchaser_country_code'] = self.purchaser_country_code
        if self.purchaser_name:
            if hasattr(self.purchaser_name, 'to_alipay_dict'):
                params['purchaser_name'] = self.purchaser_name.to_alipay_dict()
            else:
                params['purchaser_name'] = self.purchaser_name
        if self.purchaser_region_code:
            if hasattr(self.purchaser_region_code, 'to_alipay_dict'):
                params['purchaser_region_code'] = self.purchaser_region_code.to_alipay_dict()
            else:
                params['purchaser_region_code'] = self.purchaser_region_code
        if self.purchaser_tax_no:
            if hasattr(self.purchaser_tax_no, 'to_alipay_dict'):
                params['purchaser_tax_no'] = self.purchaser_tax_no.to_alipay_dict()
            else:
                params['purchaser_tax_no'] = self.purchaser_tax_no
        if self.qr_code_flag:
            if hasattr(self.qr_code_flag, 'to_alipay_dict'):
                params['qr_code_flag'] = self.qr_code_flag.to_alipay_dict()
            else:
                params['qr_code_flag'] = self.qr_code_flag
        if self.related_order:
            if hasattr(self.related_order, 'to_alipay_dict'):
                params['related_order'] = self.related_order.to_alipay_dict()
            else:
                params['related_order'] = self.related_order
        if self.seller_bank_info:
            if hasattr(self.seller_bank_info, 'to_alipay_dict'):
                params['seller_bank_info'] = self.seller_bank_info.to_alipay_dict()
            else:
                params['seller_bank_info'] = self.seller_bank_info
        if self.seller_code:
            if hasattr(self.seller_code, 'to_alipay_dict'):
                params['seller_code'] = self.seller_code.to_alipay_dict()
            else:
                params['seller_code'] = self.seller_code
        if self.seller_contact_info:
            if hasattr(self.seller_contact_info, 'to_alipay_dict'):
                params['seller_contact_info'] = self.seller_contact_info.to_alipay_dict()
            else:
                params['seller_contact_info'] = self.seller_contact_info
        if self.seller_country_code:
            if hasattr(self.seller_country_code, 'to_alipay_dict'):
                params['seller_country_code'] = self.seller_country_code.to_alipay_dict()
            else:
                params['seller_country_code'] = self.seller_country_code
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.seller_region_code:
            if hasattr(self.seller_region_code, 'to_alipay_dict'):
                params['seller_region_code'] = self.seller_region_code.to_alipay_dict()
            else:
                params['seller_region_code'] = self.seller_region_code
        if self.seller_tax_no:
            if hasattr(self.seller_tax_no, 'to_alipay_dict'):
                params['seller_tax_no'] = self.seller_tax_no.to_alipay_dict()
            else:
                params['seller_tax_no'] = self.seller_tax_no
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceModifyOpenApiDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'authorized_dealer' in d:
            o.authorized_dealer = d['authorized_dealer']
        if 'check_sum' in d:
            o.check_sum = d['check_sum']
        if 'cipher_text' in d:
            o.cipher_text = d['cipher_text']
        if 'currency' in d:
            o.currency = d['currency']
        if 'effective_tax_amount' in d:
            o.effective_tax_amount = d['effective_tax_amount']
        if 'excluding_tax_amount' in d:
            o.excluding_tax_amount = d['excluding_tax_amount']
        if 'invoice_code' in d:
            o.invoice_code = d['invoice_code']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_remark' in d:
            o.invoice_remark = d['invoice_remark']
        if 'issued_seller_name' in d:
            o.issued_seller_name = d['issued_seller_name']
        if 'issued_tax_no' in d:
            o.issued_tax_no = d['issued_tax_no']
        if 'machine_code' in d:
            o.machine_code = d['machine_code']
        if 'purchaser_bank_info' in d:
            o.purchaser_bank_info = d['purchaser_bank_info']
        if 'purchaser_code' in d:
            o.purchaser_code = d['purchaser_code']
        if 'purchaser_contact_info' in d:
            o.purchaser_contact_info = d['purchaser_contact_info']
        if 'purchaser_country_code' in d:
            o.purchaser_country_code = d['purchaser_country_code']
        if 'purchaser_name' in d:
            o.purchaser_name = d['purchaser_name']
        if 'purchaser_region_code' in d:
            o.purchaser_region_code = d['purchaser_region_code']
        if 'purchaser_tax_no' in d:
            o.purchaser_tax_no = d['purchaser_tax_no']
        if 'qr_code_flag' in d:
            o.qr_code_flag = d['qr_code_flag']
        if 'related_order' in d:
            o.related_order = d['related_order']
        if 'seller_bank_info' in d:
            o.seller_bank_info = d['seller_bank_info']
        if 'seller_code' in d:
            o.seller_code = d['seller_code']
        if 'seller_contact_info' in d:
            o.seller_contact_info = d['seller_contact_info']
        if 'seller_country_code' in d:
            o.seller_country_code = d['seller_country_code']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'seller_region_code' in d:
            o.seller_region_code = d['seller_region_code']
        if 'seller_tax_no' in d:
            o.seller_tax_no = d['seller_tax_no']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


