#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtTreasuryPaymentAcceptModel(object):

    def __init__(self):
        self._active_or_passive = None
        self._bank_code = None
        self._branch_code = None
        self._charge_bearer = None
        self._creator = None
        self._creditor_account_inner_type = None
        self._creditor_account_name = None
        self._creditor_account_no = None
        self._creditor_address = None
        self._creditor_bic = None
        self._creditor_contact_email = None
        self._creditor_contact_name = None
        self._creditor_contact_phone_number = None
        self._creditor_country = None
        self._creditor_currency = None
        self._creditor_fin_inst_id = None
        self._creditor_iban = None
        self._creditor_inst_abbr = None
        self._creditor_inst_country_code = None
        self._creditor_inst_name = None
        self._creditor_post_code = None
        self._creditor_town_name = None
        self._creditor_type = None
        self._debtor_fin_inst_id = None
        self._event_code = None
        self._expect_payment_date = None
        self._open_api_bop_transaction_code = None
        self._open_api_bop_transaction_code_remark = None
        self._open_api_instructed_amount = None
        self._open_api_instructed_amount_currency_code = None
        self._out_biz_no = None
        self._payment_purpose = None
        self._product_code = None
        self._source = None
        self._tnt_inst_id = None
        self._trans_direction = None
        self._transmitting_bank = None
        self._unstructured = None

    @property
    def active_or_passive(self):
        return self._active_or_passive

    @active_or_passive.setter
    def active_or_passive(self, value):
        self._active_or_passive = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def branch_code(self):
        return self._branch_code

    @branch_code.setter
    def branch_code(self, value):
        self._branch_code = value
    @property
    def charge_bearer(self):
        return self._charge_bearer

    @charge_bearer.setter
    def charge_bearer(self, value):
        self._charge_bearer = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def creditor_account_inner_type(self):
        return self._creditor_account_inner_type

    @creditor_account_inner_type.setter
    def creditor_account_inner_type(self, value):
        self._creditor_account_inner_type = value
    @property
    def creditor_account_name(self):
        return self._creditor_account_name

    @creditor_account_name.setter
    def creditor_account_name(self, value):
        self._creditor_account_name = value
    @property
    def creditor_account_no(self):
        return self._creditor_account_no

    @creditor_account_no.setter
    def creditor_account_no(self, value):
        self._creditor_account_no = value
    @property
    def creditor_address(self):
        return self._creditor_address

    @creditor_address.setter
    def creditor_address(self, value):
        self._creditor_address = value
    @property
    def creditor_bic(self):
        return self._creditor_bic

    @creditor_bic.setter
    def creditor_bic(self, value):
        self._creditor_bic = value
    @property
    def creditor_contact_email(self):
        return self._creditor_contact_email

    @creditor_contact_email.setter
    def creditor_contact_email(self, value):
        self._creditor_contact_email = value
    @property
    def creditor_contact_name(self):
        return self._creditor_contact_name

    @creditor_contact_name.setter
    def creditor_contact_name(self, value):
        self._creditor_contact_name = value
    @property
    def creditor_contact_phone_number(self):
        return self._creditor_contact_phone_number

    @creditor_contact_phone_number.setter
    def creditor_contact_phone_number(self, value):
        self._creditor_contact_phone_number = value
    @property
    def creditor_country(self):
        return self._creditor_country

    @creditor_country.setter
    def creditor_country(self, value):
        self._creditor_country = value
    @property
    def creditor_currency(self):
        return self._creditor_currency

    @creditor_currency.setter
    def creditor_currency(self, value):
        self._creditor_currency = value
    @property
    def creditor_fin_inst_id(self):
        return self._creditor_fin_inst_id

    @creditor_fin_inst_id.setter
    def creditor_fin_inst_id(self, value):
        self._creditor_fin_inst_id = value
    @property
    def creditor_iban(self):
        return self._creditor_iban

    @creditor_iban.setter
    def creditor_iban(self, value):
        self._creditor_iban = value
    @property
    def creditor_inst_abbr(self):
        return self._creditor_inst_abbr

    @creditor_inst_abbr.setter
    def creditor_inst_abbr(self, value):
        self._creditor_inst_abbr = value
    @property
    def creditor_inst_country_code(self):
        return self._creditor_inst_country_code

    @creditor_inst_country_code.setter
    def creditor_inst_country_code(self, value):
        self._creditor_inst_country_code = value
    @property
    def creditor_inst_name(self):
        return self._creditor_inst_name

    @creditor_inst_name.setter
    def creditor_inst_name(self, value):
        self._creditor_inst_name = value
    @property
    def creditor_post_code(self):
        return self._creditor_post_code

    @creditor_post_code.setter
    def creditor_post_code(self, value):
        self._creditor_post_code = value
    @property
    def creditor_town_name(self):
        return self._creditor_town_name

    @creditor_town_name.setter
    def creditor_town_name(self, value):
        self._creditor_town_name = value
    @property
    def creditor_type(self):
        return self._creditor_type

    @creditor_type.setter
    def creditor_type(self, value):
        self._creditor_type = value
    @property
    def debtor_fin_inst_id(self):
        return self._debtor_fin_inst_id

    @debtor_fin_inst_id.setter
    def debtor_fin_inst_id(self, value):
        self._debtor_fin_inst_id = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def expect_payment_date(self):
        return self._expect_payment_date

    @expect_payment_date.setter
    def expect_payment_date(self, value):
        self._expect_payment_date = value
    @property
    def open_api_bop_transaction_code(self):
        return self._open_api_bop_transaction_code

    @open_api_bop_transaction_code.setter
    def open_api_bop_transaction_code(self, value):
        self._open_api_bop_transaction_code = value
    @property
    def open_api_bop_transaction_code_remark(self):
        return self._open_api_bop_transaction_code_remark

    @open_api_bop_transaction_code_remark.setter
    def open_api_bop_transaction_code_remark(self, value):
        self._open_api_bop_transaction_code_remark = value
    @property
    def open_api_instructed_amount(self):
        return self._open_api_instructed_amount

    @open_api_instructed_amount.setter
    def open_api_instructed_amount(self, value):
        self._open_api_instructed_amount = value
    @property
    def open_api_instructed_amount_currency_code(self):
        return self._open_api_instructed_amount_currency_code

    @open_api_instructed_amount_currency_code.setter
    def open_api_instructed_amount_currency_code(self, value):
        self._open_api_instructed_amount_currency_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payment_purpose(self):
        return self._payment_purpose

    @payment_purpose.setter
    def payment_purpose(self, value):
        self._payment_purpose = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def trans_direction(self):
        return self._trans_direction

    @trans_direction.setter
    def trans_direction(self, value):
        self._trans_direction = value
    @property
    def transmitting_bank(self):
        return self._transmitting_bank

    @transmitting_bank.setter
    def transmitting_bank(self, value):
        self._transmitting_bank = value
    @property
    def unstructured(self):
        return self._unstructured

    @unstructured.setter
    def unstructured(self, value):
        self._unstructured = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_or_passive:
            if hasattr(self.active_or_passive, 'to_alipay_dict'):
                params['active_or_passive'] = self.active_or_passive.to_alipay_dict()
            else:
                params['active_or_passive'] = self.active_or_passive
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.branch_code:
            if hasattr(self.branch_code, 'to_alipay_dict'):
                params['branch_code'] = self.branch_code.to_alipay_dict()
            else:
                params['branch_code'] = self.branch_code
        if self.charge_bearer:
            if hasattr(self.charge_bearer, 'to_alipay_dict'):
                params['charge_bearer'] = self.charge_bearer.to_alipay_dict()
            else:
                params['charge_bearer'] = self.charge_bearer
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.creditor_account_inner_type:
            if hasattr(self.creditor_account_inner_type, 'to_alipay_dict'):
                params['creditor_account_inner_type'] = self.creditor_account_inner_type.to_alipay_dict()
            else:
                params['creditor_account_inner_type'] = self.creditor_account_inner_type
        if self.creditor_account_name:
            if hasattr(self.creditor_account_name, 'to_alipay_dict'):
                params['creditor_account_name'] = self.creditor_account_name.to_alipay_dict()
            else:
                params['creditor_account_name'] = self.creditor_account_name
        if self.creditor_account_no:
            if hasattr(self.creditor_account_no, 'to_alipay_dict'):
                params['creditor_account_no'] = self.creditor_account_no.to_alipay_dict()
            else:
                params['creditor_account_no'] = self.creditor_account_no
        if self.creditor_address:
            if hasattr(self.creditor_address, 'to_alipay_dict'):
                params['creditor_address'] = self.creditor_address.to_alipay_dict()
            else:
                params['creditor_address'] = self.creditor_address
        if self.creditor_bic:
            if hasattr(self.creditor_bic, 'to_alipay_dict'):
                params['creditor_bic'] = self.creditor_bic.to_alipay_dict()
            else:
                params['creditor_bic'] = self.creditor_bic
        if self.creditor_contact_email:
            if hasattr(self.creditor_contact_email, 'to_alipay_dict'):
                params['creditor_contact_email'] = self.creditor_contact_email.to_alipay_dict()
            else:
                params['creditor_contact_email'] = self.creditor_contact_email
        if self.creditor_contact_name:
            if hasattr(self.creditor_contact_name, 'to_alipay_dict'):
                params['creditor_contact_name'] = self.creditor_contact_name.to_alipay_dict()
            else:
                params['creditor_contact_name'] = self.creditor_contact_name
        if self.creditor_contact_phone_number:
            if hasattr(self.creditor_contact_phone_number, 'to_alipay_dict'):
                params['creditor_contact_phone_number'] = self.creditor_contact_phone_number.to_alipay_dict()
            else:
                params['creditor_contact_phone_number'] = self.creditor_contact_phone_number
        if self.creditor_country:
            if hasattr(self.creditor_country, 'to_alipay_dict'):
                params['creditor_country'] = self.creditor_country.to_alipay_dict()
            else:
                params['creditor_country'] = self.creditor_country
        if self.creditor_currency:
            if hasattr(self.creditor_currency, 'to_alipay_dict'):
                params['creditor_currency'] = self.creditor_currency.to_alipay_dict()
            else:
                params['creditor_currency'] = self.creditor_currency
        if self.creditor_fin_inst_id:
            if hasattr(self.creditor_fin_inst_id, 'to_alipay_dict'):
                params['creditor_fin_inst_id'] = self.creditor_fin_inst_id.to_alipay_dict()
            else:
                params['creditor_fin_inst_id'] = self.creditor_fin_inst_id
        if self.creditor_iban:
            if hasattr(self.creditor_iban, 'to_alipay_dict'):
                params['creditor_iban'] = self.creditor_iban.to_alipay_dict()
            else:
                params['creditor_iban'] = self.creditor_iban
        if self.creditor_inst_abbr:
            if hasattr(self.creditor_inst_abbr, 'to_alipay_dict'):
                params['creditor_inst_abbr'] = self.creditor_inst_abbr.to_alipay_dict()
            else:
                params['creditor_inst_abbr'] = self.creditor_inst_abbr
        if self.creditor_inst_country_code:
            if hasattr(self.creditor_inst_country_code, 'to_alipay_dict'):
                params['creditor_inst_country_code'] = self.creditor_inst_country_code.to_alipay_dict()
            else:
                params['creditor_inst_country_code'] = self.creditor_inst_country_code
        if self.creditor_inst_name:
            if hasattr(self.creditor_inst_name, 'to_alipay_dict'):
                params['creditor_inst_name'] = self.creditor_inst_name.to_alipay_dict()
            else:
                params['creditor_inst_name'] = self.creditor_inst_name
        if self.creditor_post_code:
            if hasattr(self.creditor_post_code, 'to_alipay_dict'):
                params['creditor_post_code'] = self.creditor_post_code.to_alipay_dict()
            else:
                params['creditor_post_code'] = self.creditor_post_code
        if self.creditor_town_name:
            if hasattr(self.creditor_town_name, 'to_alipay_dict'):
                params['creditor_town_name'] = self.creditor_town_name.to_alipay_dict()
            else:
                params['creditor_town_name'] = self.creditor_town_name
        if self.creditor_type:
            if hasattr(self.creditor_type, 'to_alipay_dict'):
                params['creditor_type'] = self.creditor_type.to_alipay_dict()
            else:
                params['creditor_type'] = self.creditor_type
        if self.debtor_fin_inst_id:
            if hasattr(self.debtor_fin_inst_id, 'to_alipay_dict'):
                params['debtor_fin_inst_id'] = self.debtor_fin_inst_id.to_alipay_dict()
            else:
                params['debtor_fin_inst_id'] = self.debtor_fin_inst_id
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.expect_payment_date:
            if hasattr(self.expect_payment_date, 'to_alipay_dict'):
                params['expect_payment_date'] = self.expect_payment_date.to_alipay_dict()
            else:
                params['expect_payment_date'] = self.expect_payment_date
        if self.open_api_bop_transaction_code:
            if hasattr(self.open_api_bop_transaction_code, 'to_alipay_dict'):
                params['open_api_bop_transaction_code'] = self.open_api_bop_transaction_code.to_alipay_dict()
            else:
                params['open_api_bop_transaction_code'] = self.open_api_bop_transaction_code
        if self.open_api_bop_transaction_code_remark:
            if hasattr(self.open_api_bop_transaction_code_remark, 'to_alipay_dict'):
                params['open_api_bop_transaction_code_remark'] = self.open_api_bop_transaction_code_remark.to_alipay_dict()
            else:
                params['open_api_bop_transaction_code_remark'] = self.open_api_bop_transaction_code_remark
        if self.open_api_instructed_amount:
            if hasattr(self.open_api_instructed_amount, 'to_alipay_dict'):
                params['open_api_instructed_amount'] = self.open_api_instructed_amount.to_alipay_dict()
            else:
                params['open_api_instructed_amount'] = self.open_api_instructed_amount
        if self.open_api_instructed_amount_currency_code:
            if hasattr(self.open_api_instructed_amount_currency_code, 'to_alipay_dict'):
                params['open_api_instructed_amount_currency_code'] = self.open_api_instructed_amount_currency_code.to_alipay_dict()
            else:
                params['open_api_instructed_amount_currency_code'] = self.open_api_instructed_amount_currency_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payment_purpose:
            if hasattr(self.payment_purpose, 'to_alipay_dict'):
                params['payment_purpose'] = self.payment_purpose.to_alipay_dict()
            else:
                params['payment_purpose'] = self.payment_purpose
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.trans_direction:
            if hasattr(self.trans_direction, 'to_alipay_dict'):
                params['trans_direction'] = self.trans_direction.to_alipay_dict()
            else:
                params['trans_direction'] = self.trans_direction
        if self.transmitting_bank:
            if hasattr(self.transmitting_bank, 'to_alipay_dict'):
                params['transmitting_bank'] = self.transmitting_bank.to_alipay_dict()
            else:
                params['transmitting_bank'] = self.transmitting_bank
        if self.unstructured:
            if hasattr(self.unstructured, 'to_alipay_dict'):
                params['unstructured'] = self.unstructured.to_alipay_dict()
            else:
                params['unstructured'] = self.unstructured
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtTreasuryPaymentAcceptModel()
        if 'active_or_passive' in d:
            o.active_or_passive = d['active_or_passive']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'branch_code' in d:
            o.branch_code = d['branch_code']
        if 'charge_bearer' in d:
            o.charge_bearer = d['charge_bearer']
        if 'creator' in d:
            o.creator = d['creator']
        if 'creditor_account_inner_type' in d:
            o.creditor_account_inner_type = d['creditor_account_inner_type']
        if 'creditor_account_name' in d:
            o.creditor_account_name = d['creditor_account_name']
        if 'creditor_account_no' in d:
            o.creditor_account_no = d['creditor_account_no']
        if 'creditor_address' in d:
            o.creditor_address = d['creditor_address']
        if 'creditor_bic' in d:
            o.creditor_bic = d['creditor_bic']
        if 'creditor_contact_email' in d:
            o.creditor_contact_email = d['creditor_contact_email']
        if 'creditor_contact_name' in d:
            o.creditor_contact_name = d['creditor_contact_name']
        if 'creditor_contact_phone_number' in d:
            o.creditor_contact_phone_number = d['creditor_contact_phone_number']
        if 'creditor_country' in d:
            o.creditor_country = d['creditor_country']
        if 'creditor_currency' in d:
            o.creditor_currency = d['creditor_currency']
        if 'creditor_fin_inst_id' in d:
            o.creditor_fin_inst_id = d['creditor_fin_inst_id']
        if 'creditor_iban' in d:
            o.creditor_iban = d['creditor_iban']
        if 'creditor_inst_abbr' in d:
            o.creditor_inst_abbr = d['creditor_inst_abbr']
        if 'creditor_inst_country_code' in d:
            o.creditor_inst_country_code = d['creditor_inst_country_code']
        if 'creditor_inst_name' in d:
            o.creditor_inst_name = d['creditor_inst_name']
        if 'creditor_post_code' in d:
            o.creditor_post_code = d['creditor_post_code']
        if 'creditor_town_name' in d:
            o.creditor_town_name = d['creditor_town_name']
        if 'creditor_type' in d:
            o.creditor_type = d['creditor_type']
        if 'debtor_fin_inst_id' in d:
            o.debtor_fin_inst_id = d['debtor_fin_inst_id']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'expect_payment_date' in d:
            o.expect_payment_date = d['expect_payment_date']
        if 'open_api_bop_transaction_code' in d:
            o.open_api_bop_transaction_code = d['open_api_bop_transaction_code']
        if 'open_api_bop_transaction_code_remark' in d:
            o.open_api_bop_transaction_code_remark = d['open_api_bop_transaction_code_remark']
        if 'open_api_instructed_amount' in d:
            o.open_api_instructed_amount = d['open_api_instructed_amount']
        if 'open_api_instructed_amount_currency_code' in d:
            o.open_api_instructed_amount_currency_code = d['open_api_instructed_amount_currency_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payment_purpose' in d:
            o.payment_purpose = d['payment_purpose']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'source' in d:
            o.source = d['source']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'trans_direction' in d:
            o.trans_direction = d['trans_direction']
        if 'transmitting_bank' in d:
            o.transmitting_bank = d['transmitting_bank']
        if 'unstructured' in d:
            o.unstructured = d['unstructured']
        return o


