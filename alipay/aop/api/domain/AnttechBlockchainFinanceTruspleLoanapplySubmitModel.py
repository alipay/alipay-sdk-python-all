#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BeneficialEntity import BeneficialEntity
from alipay.aop.api.domain.FinAttachment import FinAttachment
from alipay.aop.api.domain.BeneficialEntity import BeneficialEntity
from alipay.aop.api.domain.BankAccount import BankAccount
from alipay.aop.api.domain.TradeInformation import TradeInformation


class AnttechBlockchainFinanceTruspleLoanapplySubmitModel(object):

    def __init__(self):
        self._actual_controllers = None
        self._attachments = None
        self._beneficiaries = None
        self._borrower_type = None
        self._external_credit_grant_id = None
        self._external_loan_id = None
        self._external_loan_request_id = None
        self._external_product_code = None
        self._external_user_id = None
        self._inst_code = None
        self._interest_rate = None
        self._loan_amount = None
        self._loan_amount_currency = None
        self._loan_payment_account_type = None
        self._loan_payment_method = None
        self._loan_purpose = None
        self._loan_quota_type = None
        self._loan_term = None
        self._loan_term_unit = None
        self._penalty_rate = None
        self._rate_unit = None
        self._receive_account = None
        self._regular_repay_day = None
        self._repay_day_type = None
        self._repay_mode = None
        self._trade_info = None

    @property
    def actual_controllers(self):
        return self._actual_controllers

    @actual_controllers.setter
    def actual_controllers(self, value):
        if isinstance(value, list):
            self._actual_controllers = list()
            for i in value:
                if isinstance(i, BeneficialEntity):
                    self._actual_controllers.append(i)
                else:
                    self._actual_controllers.append(BeneficialEntity.from_alipay_dict(i))
    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, FinAttachment):
                    self._attachments.append(i)
                else:
                    self._attachments.append(FinAttachment.from_alipay_dict(i))
    @property
    def beneficiaries(self):
        return self._beneficiaries

    @beneficiaries.setter
    def beneficiaries(self, value):
        if isinstance(value, list):
            self._beneficiaries = list()
            for i in value:
                if isinstance(i, BeneficialEntity):
                    self._beneficiaries.append(i)
                else:
                    self._beneficiaries.append(BeneficialEntity.from_alipay_dict(i))
    @property
    def borrower_type(self):
        return self._borrower_type

    @borrower_type.setter
    def borrower_type(self, value):
        self._borrower_type = value
    @property
    def external_credit_grant_id(self):
        return self._external_credit_grant_id

    @external_credit_grant_id.setter
    def external_credit_grant_id(self, value):
        self._external_credit_grant_id = value
    @property
    def external_loan_id(self):
        return self._external_loan_id

    @external_loan_id.setter
    def external_loan_id(self, value):
        self._external_loan_id = value
    @property
    def external_loan_request_id(self):
        return self._external_loan_request_id

    @external_loan_request_id.setter
    def external_loan_request_id(self, value):
        self._external_loan_request_id = value
    @property
    def external_product_code(self):
        return self._external_product_code

    @external_product_code.setter
    def external_product_code(self, value):
        self._external_product_code = value
    @property
    def external_user_id(self):
        return self._external_user_id

    @external_user_id.setter
    def external_user_id(self, value):
        self._external_user_id = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_amount_currency(self):
        return self._loan_amount_currency

    @loan_amount_currency.setter
    def loan_amount_currency(self, value):
        self._loan_amount_currency = value
    @property
    def loan_payment_account_type(self):
        return self._loan_payment_account_type

    @loan_payment_account_type.setter
    def loan_payment_account_type(self, value):
        self._loan_payment_account_type = value
    @property
    def loan_payment_method(self):
        return self._loan_payment_method

    @loan_payment_method.setter
    def loan_payment_method(self, value):
        self._loan_payment_method = value
    @property
    def loan_purpose(self):
        return self._loan_purpose

    @loan_purpose.setter
    def loan_purpose(self, value):
        self._loan_purpose = value
    @property
    def loan_quota_type(self):
        return self._loan_quota_type

    @loan_quota_type.setter
    def loan_quota_type(self, value):
        self._loan_quota_type = value
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
    def penalty_rate(self):
        return self._penalty_rate

    @penalty_rate.setter
    def penalty_rate(self, value):
        self._penalty_rate = value
    @property
    def rate_unit(self):
        return self._rate_unit

    @rate_unit.setter
    def rate_unit(self, value):
        self._rate_unit = value
    @property
    def receive_account(self):
        return self._receive_account

    @receive_account.setter
    def receive_account(self, value):
        if isinstance(value, BankAccount):
            self._receive_account = value
        else:
            self._receive_account = BankAccount.from_alipay_dict(value)
    @property
    def regular_repay_day(self):
        return self._regular_repay_day

    @regular_repay_day.setter
    def regular_repay_day(self, value):
        self._regular_repay_day = value
    @property
    def repay_day_type(self):
        return self._repay_day_type

    @repay_day_type.setter
    def repay_day_type(self, value):
        self._repay_day_type = value
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value
    @property
    def trade_info(self):
        return self._trade_info

    @trade_info.setter
    def trade_info(self, value):
        if isinstance(value, TradeInformation):
            self._trade_info = value
        else:
            self._trade_info = TradeInformation.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.actual_controllers:
            if isinstance(self.actual_controllers, list):
                for i in range(0, len(self.actual_controllers)):
                    element = self.actual_controllers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.actual_controllers[i] = element.to_alipay_dict()
            if hasattr(self.actual_controllers, 'to_alipay_dict'):
                params['actual_controllers'] = self.actual_controllers.to_alipay_dict()
            else:
                params['actual_controllers'] = self.actual_controllers
        if self.attachments:
            if isinstance(self.attachments, list):
                for i in range(0, len(self.attachments)):
                    element = self.attachments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachments[i] = element.to_alipay_dict()
            if hasattr(self.attachments, 'to_alipay_dict'):
                params['attachments'] = self.attachments.to_alipay_dict()
            else:
                params['attachments'] = self.attachments
        if self.beneficiaries:
            if isinstance(self.beneficiaries, list):
                for i in range(0, len(self.beneficiaries)):
                    element = self.beneficiaries[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.beneficiaries[i] = element.to_alipay_dict()
            if hasattr(self.beneficiaries, 'to_alipay_dict'):
                params['beneficiaries'] = self.beneficiaries.to_alipay_dict()
            else:
                params['beneficiaries'] = self.beneficiaries
        if self.borrower_type:
            if hasattr(self.borrower_type, 'to_alipay_dict'):
                params['borrower_type'] = self.borrower_type.to_alipay_dict()
            else:
                params['borrower_type'] = self.borrower_type
        if self.external_credit_grant_id:
            if hasattr(self.external_credit_grant_id, 'to_alipay_dict'):
                params['external_credit_grant_id'] = self.external_credit_grant_id.to_alipay_dict()
            else:
                params['external_credit_grant_id'] = self.external_credit_grant_id
        if self.external_loan_id:
            if hasattr(self.external_loan_id, 'to_alipay_dict'):
                params['external_loan_id'] = self.external_loan_id.to_alipay_dict()
            else:
                params['external_loan_id'] = self.external_loan_id
        if self.external_loan_request_id:
            if hasattr(self.external_loan_request_id, 'to_alipay_dict'):
                params['external_loan_request_id'] = self.external_loan_request_id.to_alipay_dict()
            else:
                params['external_loan_request_id'] = self.external_loan_request_id
        if self.external_product_code:
            if hasattr(self.external_product_code, 'to_alipay_dict'):
                params['external_product_code'] = self.external_product_code.to_alipay_dict()
            else:
                params['external_product_code'] = self.external_product_code
        if self.external_user_id:
            if hasattr(self.external_user_id, 'to_alipay_dict'):
                params['external_user_id'] = self.external_user_id.to_alipay_dict()
            else:
                params['external_user_id'] = self.external_user_id
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.interest_rate:
            if hasattr(self.interest_rate, 'to_alipay_dict'):
                params['interest_rate'] = self.interest_rate.to_alipay_dict()
            else:
                params['interest_rate'] = self.interest_rate
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.loan_amount_currency:
            if hasattr(self.loan_amount_currency, 'to_alipay_dict'):
                params['loan_amount_currency'] = self.loan_amount_currency.to_alipay_dict()
            else:
                params['loan_amount_currency'] = self.loan_amount_currency
        if self.loan_payment_account_type:
            if hasattr(self.loan_payment_account_type, 'to_alipay_dict'):
                params['loan_payment_account_type'] = self.loan_payment_account_type.to_alipay_dict()
            else:
                params['loan_payment_account_type'] = self.loan_payment_account_type
        if self.loan_payment_method:
            if hasattr(self.loan_payment_method, 'to_alipay_dict'):
                params['loan_payment_method'] = self.loan_payment_method.to_alipay_dict()
            else:
                params['loan_payment_method'] = self.loan_payment_method
        if self.loan_purpose:
            if hasattr(self.loan_purpose, 'to_alipay_dict'):
                params['loan_purpose'] = self.loan_purpose.to_alipay_dict()
            else:
                params['loan_purpose'] = self.loan_purpose
        if self.loan_quota_type:
            if hasattr(self.loan_quota_type, 'to_alipay_dict'):
                params['loan_quota_type'] = self.loan_quota_type.to_alipay_dict()
            else:
                params['loan_quota_type'] = self.loan_quota_type
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
        if self.penalty_rate:
            if hasattr(self.penalty_rate, 'to_alipay_dict'):
                params['penalty_rate'] = self.penalty_rate.to_alipay_dict()
            else:
                params['penalty_rate'] = self.penalty_rate
        if self.rate_unit:
            if hasattr(self.rate_unit, 'to_alipay_dict'):
                params['rate_unit'] = self.rate_unit.to_alipay_dict()
            else:
                params['rate_unit'] = self.rate_unit
        if self.receive_account:
            if hasattr(self.receive_account, 'to_alipay_dict'):
                params['receive_account'] = self.receive_account.to_alipay_dict()
            else:
                params['receive_account'] = self.receive_account
        if self.regular_repay_day:
            if hasattr(self.regular_repay_day, 'to_alipay_dict'):
                params['regular_repay_day'] = self.regular_repay_day.to_alipay_dict()
            else:
                params['regular_repay_day'] = self.regular_repay_day
        if self.repay_day_type:
            if hasattr(self.repay_day_type, 'to_alipay_dict'):
                params['repay_day_type'] = self.repay_day_type.to_alipay_dict()
            else:
                params['repay_day_type'] = self.repay_day_type
        if self.repay_mode:
            if hasattr(self.repay_mode, 'to_alipay_dict'):
                params['repay_mode'] = self.repay_mode.to_alipay_dict()
            else:
                params['repay_mode'] = self.repay_mode
        if self.trade_info:
            if hasattr(self.trade_info, 'to_alipay_dict'):
                params['trade_info'] = self.trade_info.to_alipay_dict()
            else:
                params['trade_info'] = self.trade_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTruspleLoanapplySubmitModel()
        if 'actual_controllers' in d:
            o.actual_controllers = d['actual_controllers']
        if 'attachments' in d:
            o.attachments = d['attachments']
        if 'beneficiaries' in d:
            o.beneficiaries = d['beneficiaries']
        if 'borrower_type' in d:
            o.borrower_type = d['borrower_type']
        if 'external_credit_grant_id' in d:
            o.external_credit_grant_id = d['external_credit_grant_id']
        if 'external_loan_id' in d:
            o.external_loan_id = d['external_loan_id']
        if 'external_loan_request_id' in d:
            o.external_loan_request_id = d['external_loan_request_id']
        if 'external_product_code' in d:
            o.external_product_code = d['external_product_code']
        if 'external_user_id' in d:
            o.external_user_id = d['external_user_id']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'interest_rate' in d:
            o.interest_rate = d['interest_rate']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'loan_amount_currency' in d:
            o.loan_amount_currency = d['loan_amount_currency']
        if 'loan_payment_account_type' in d:
            o.loan_payment_account_type = d['loan_payment_account_type']
        if 'loan_payment_method' in d:
            o.loan_payment_method = d['loan_payment_method']
        if 'loan_purpose' in d:
            o.loan_purpose = d['loan_purpose']
        if 'loan_quota_type' in d:
            o.loan_quota_type = d['loan_quota_type']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'penalty_rate' in d:
            o.penalty_rate = d['penalty_rate']
        if 'rate_unit' in d:
            o.rate_unit = d['rate_unit']
        if 'receive_account' in d:
            o.receive_account = d['receive_account']
        if 'regular_repay_day' in d:
            o.regular_repay_day = d['regular_repay_day']
        if 'repay_day_type' in d:
            o.repay_day_type = d['repay_day_type']
        if 'repay_mode' in d:
            o.repay_mode = d['repay_mode']
        if 'trade_info' in d:
            o.trade_info = d['trade_info']
        return o


