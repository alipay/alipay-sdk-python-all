#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanSideloanlendLendApplyModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._bank_card_id = None
        self._extension = None
        self._loan_amount = None
        self._loan_apply_no = None
        self._loan_purpose = None
        self._loan_term = None
        self._loan_term_unit = None
        self._open_id = None
        self._product_code = None
        self._repayment_day = None
        self._repayment_method = None
        self._verify_id = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def bank_card_id(self):
        return self._bank_card_id

    @bank_card_id.setter
    def bank_card_id(self, value):
        self._bank_card_id = value
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value
    @property
    def loan_purpose(self):
        return self._loan_purpose

    @loan_purpose.setter
    def loan_purpose(self, value):
        self._loan_purpose = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def loan_term_unit(self):
        return self._loan_term_unit

    @loan_term_unit.setter
    def loan_term_unit(self, value):
        self._loan_term_unit = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def repayment_day(self):
        return self._repayment_day

    @repayment_day.setter
    def repayment_day(self, value):
        self._repayment_day = value
    @property
    def repayment_method(self):
        return self._repayment_method

    @repayment_method.setter
    def repayment_method(self, value):
        self._repayment_method = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.bank_card_id:
            if hasattr(self.bank_card_id, 'to_alipay_dict'):
                params['bank_card_id'] = self.bank_card_id.to_alipay_dict()
            else:
                params['bank_card_id'] = self.bank_card_id
        if self.extension:
            if hasattr(self.extension, 'to_alipay_dict'):
                params['extension'] = self.extension.to_alipay_dict()
            else:
                params['extension'] = self.extension
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.loan_apply_no:
            if hasattr(self.loan_apply_no, 'to_alipay_dict'):
                params['loan_apply_no'] = self.loan_apply_no.to_alipay_dict()
            else:
                params['loan_apply_no'] = self.loan_apply_no
        if self.loan_purpose:
            if hasattr(self.loan_purpose, 'to_alipay_dict'):
                params['loan_purpose'] = self.loan_purpose.to_alipay_dict()
            else:
                params['loan_purpose'] = self.loan_purpose
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.loan_term_unit:
            if hasattr(self.loan_term_unit, 'to_alipay_dict'):
                params['loan_term_unit'] = self.loan_term_unit.to_alipay_dict()
            else:
                params['loan_term_unit'] = self.loan_term_unit
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.repayment_day:
            if hasattr(self.repayment_day, 'to_alipay_dict'):
                params['repayment_day'] = self.repayment_day.to_alipay_dict()
            else:
                params['repayment_day'] = self.repayment_day
        if self.repayment_method:
            if hasattr(self.repayment_method, 'to_alipay_dict'):
                params['repayment_method'] = self.repayment_method.to_alipay_dict()
            else:
                params['repayment_method'] = self.repayment_method
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanSideloanlendLendApplyModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'bank_card_id' in d:
            o.bank_card_id = d['bank_card_id']
        if 'extension' in d:
            o.extension = d['extension']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'loan_apply_no' in d:
            o.loan_apply_no = d['loan_apply_no']
        if 'loan_purpose' in d:
            o.loan_purpose = d['loan_purpose']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'repayment_day' in d:
            o.repayment_day = d['repayment_day']
        if 'repayment_method' in d:
            o.repayment_method = d['repayment_method']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


