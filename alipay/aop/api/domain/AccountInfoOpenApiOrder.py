#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountInfoOpenApiOrder(object):

    def __init__(self):
        self._account_code = None
        self._account_desc = None
        self._accounting_date = None
        self._accounting_month = None
        self._accounting_type_code = None
        self._amount = None
        self._amount_beq = None
        self._budget_dept_code = None
        self._budget_dept_desc = None
        self._company_code = None
        self._company_desc = None
        self._cost_center_code = None
        self._cost_center_desc = None
        self._currency = None
        self._currency_beq = None
        self._detail_code = None
        self._detail_desc = None
        self._industry_code = None
        self._industry_desc = None
        self._inter_company_code = None
        self._inter_company_desc = None
        self._je_line_desc = None
        self._product_code = None
        self._product_desc = None
        self._project_code = None
        self._project_desc = None
        self._region_code = None
        self._region_desc = None
        self._spare_code_1 = None
        self._spare_code_2 = None
        self._spare_desc_1 = None
        self._spare_desc_2 = None
        self._voucher_no = None

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, value):
        self._account_code = value
    @property
    def account_desc(self):
        return self._account_desc

    @account_desc.setter
    def account_desc(self, value):
        self._account_desc = value
    @property
    def accounting_date(self):
        return self._accounting_date

    @accounting_date.setter
    def accounting_date(self, value):
        self._accounting_date = value
    @property
    def accounting_month(self):
        return self._accounting_month

    @accounting_month.setter
    def accounting_month(self, value):
        self._accounting_month = value
    @property
    def accounting_type_code(self):
        return self._accounting_type_code

    @accounting_type_code.setter
    def accounting_type_code(self, value):
        self._accounting_type_code = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def amount_beq(self):
        return self._amount_beq

    @amount_beq.setter
    def amount_beq(self, value):
        self._amount_beq = value
    @property
    def budget_dept_code(self):
        return self._budget_dept_code

    @budget_dept_code.setter
    def budget_dept_code(self, value):
        self._budget_dept_code = value
    @property
    def budget_dept_desc(self):
        return self._budget_dept_desc

    @budget_dept_desc.setter
    def budget_dept_desc(self, value):
        self._budget_dept_desc = value
    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def company_desc(self):
        return self._company_desc

    @company_desc.setter
    def company_desc(self, value):
        self._company_desc = value
    @property
    def cost_center_code(self):
        return self._cost_center_code

    @cost_center_code.setter
    def cost_center_code(self, value):
        self._cost_center_code = value
    @property
    def cost_center_desc(self):
        return self._cost_center_desc

    @cost_center_desc.setter
    def cost_center_desc(self, value):
        self._cost_center_desc = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def currency_beq(self):
        return self._currency_beq

    @currency_beq.setter
    def currency_beq(self, value):
        self._currency_beq = value
    @property
    def detail_code(self):
        return self._detail_code

    @detail_code.setter
    def detail_code(self, value):
        self._detail_code = value
    @property
    def detail_desc(self):
        return self._detail_desc

    @detail_desc.setter
    def detail_desc(self, value):
        self._detail_desc = value
    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def industry_desc(self):
        return self._industry_desc

    @industry_desc.setter
    def industry_desc(self, value):
        self._industry_desc = value
    @property
    def inter_company_code(self):
        return self._inter_company_code

    @inter_company_code.setter
    def inter_company_code(self, value):
        self._inter_company_code = value
    @property
    def inter_company_desc(self):
        return self._inter_company_desc

    @inter_company_desc.setter
    def inter_company_desc(self, value):
        self._inter_company_desc = value
    @property
    def je_line_desc(self):
        return self._je_line_desc

    @je_line_desc.setter
    def je_line_desc(self, value):
        self._je_line_desc = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_desc(self):
        return self._product_desc

    @product_desc.setter
    def product_desc(self, value):
        self._product_desc = value
    @property
    def project_code(self):
        return self._project_code

    @project_code.setter
    def project_code(self, value):
        self._project_code = value
    @property
    def project_desc(self):
        return self._project_desc

    @project_desc.setter
    def project_desc(self, value):
        self._project_desc = value
    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value
    @property
    def region_desc(self):
        return self._region_desc

    @region_desc.setter
    def region_desc(self, value):
        self._region_desc = value
    @property
    def spare_code_1(self):
        return self._spare_code_1

    @spare_code_1.setter
    def spare_code_1(self, value):
        self._spare_code_1 = value
    @property
    def spare_code_2(self):
        return self._spare_code_2

    @spare_code_2.setter
    def spare_code_2(self, value):
        self._spare_code_2 = value
    @property
    def spare_desc_1(self):
        return self._spare_desc_1

    @spare_desc_1.setter
    def spare_desc_1(self, value):
        self._spare_desc_1 = value
    @property
    def spare_desc_2(self):
        return self._spare_desc_2

    @spare_desc_2.setter
    def spare_desc_2(self, value):
        self._spare_desc_2 = value
    @property
    def voucher_no(self):
        return self._voucher_no

    @voucher_no.setter
    def voucher_no(self, value):
        self._voucher_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_code:
            if hasattr(self.account_code, 'to_alipay_dict'):
                params['account_code'] = self.account_code.to_alipay_dict()
            else:
                params['account_code'] = self.account_code
        if self.account_desc:
            if hasattr(self.account_desc, 'to_alipay_dict'):
                params['account_desc'] = self.account_desc.to_alipay_dict()
            else:
                params['account_desc'] = self.account_desc
        if self.accounting_date:
            if hasattr(self.accounting_date, 'to_alipay_dict'):
                params['accounting_date'] = self.accounting_date.to_alipay_dict()
            else:
                params['accounting_date'] = self.accounting_date
        if self.accounting_month:
            if hasattr(self.accounting_month, 'to_alipay_dict'):
                params['accounting_month'] = self.accounting_month.to_alipay_dict()
            else:
                params['accounting_month'] = self.accounting_month
        if self.accounting_type_code:
            if hasattr(self.accounting_type_code, 'to_alipay_dict'):
                params['accounting_type_code'] = self.accounting_type_code.to_alipay_dict()
            else:
                params['accounting_type_code'] = self.accounting_type_code
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.amount_beq:
            if hasattr(self.amount_beq, 'to_alipay_dict'):
                params['amount_beq'] = self.amount_beq.to_alipay_dict()
            else:
                params['amount_beq'] = self.amount_beq
        if self.budget_dept_code:
            if hasattr(self.budget_dept_code, 'to_alipay_dict'):
                params['budget_dept_code'] = self.budget_dept_code.to_alipay_dict()
            else:
                params['budget_dept_code'] = self.budget_dept_code
        if self.budget_dept_desc:
            if hasattr(self.budget_dept_desc, 'to_alipay_dict'):
                params['budget_dept_desc'] = self.budget_dept_desc.to_alipay_dict()
            else:
                params['budget_dept_desc'] = self.budget_dept_desc
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.company_desc:
            if hasattr(self.company_desc, 'to_alipay_dict'):
                params['company_desc'] = self.company_desc.to_alipay_dict()
            else:
                params['company_desc'] = self.company_desc
        if self.cost_center_code:
            if hasattr(self.cost_center_code, 'to_alipay_dict'):
                params['cost_center_code'] = self.cost_center_code.to_alipay_dict()
            else:
                params['cost_center_code'] = self.cost_center_code
        if self.cost_center_desc:
            if hasattr(self.cost_center_desc, 'to_alipay_dict'):
                params['cost_center_desc'] = self.cost_center_desc.to_alipay_dict()
            else:
                params['cost_center_desc'] = self.cost_center_desc
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.currency_beq:
            if hasattr(self.currency_beq, 'to_alipay_dict'):
                params['currency_beq'] = self.currency_beq.to_alipay_dict()
            else:
                params['currency_beq'] = self.currency_beq
        if self.detail_code:
            if hasattr(self.detail_code, 'to_alipay_dict'):
                params['detail_code'] = self.detail_code.to_alipay_dict()
            else:
                params['detail_code'] = self.detail_code
        if self.detail_desc:
            if hasattr(self.detail_desc, 'to_alipay_dict'):
                params['detail_desc'] = self.detail_desc.to_alipay_dict()
            else:
                params['detail_desc'] = self.detail_desc
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.industry_desc:
            if hasattr(self.industry_desc, 'to_alipay_dict'):
                params['industry_desc'] = self.industry_desc.to_alipay_dict()
            else:
                params['industry_desc'] = self.industry_desc
        if self.inter_company_code:
            if hasattr(self.inter_company_code, 'to_alipay_dict'):
                params['inter_company_code'] = self.inter_company_code.to_alipay_dict()
            else:
                params['inter_company_code'] = self.inter_company_code
        if self.inter_company_desc:
            if hasattr(self.inter_company_desc, 'to_alipay_dict'):
                params['inter_company_desc'] = self.inter_company_desc.to_alipay_dict()
            else:
                params['inter_company_desc'] = self.inter_company_desc
        if self.je_line_desc:
            if hasattr(self.je_line_desc, 'to_alipay_dict'):
                params['je_line_desc'] = self.je_line_desc.to_alipay_dict()
            else:
                params['je_line_desc'] = self.je_line_desc
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_desc:
            if hasattr(self.product_desc, 'to_alipay_dict'):
                params['product_desc'] = self.product_desc.to_alipay_dict()
            else:
                params['product_desc'] = self.product_desc
        if self.project_code:
            if hasattr(self.project_code, 'to_alipay_dict'):
                params['project_code'] = self.project_code.to_alipay_dict()
            else:
                params['project_code'] = self.project_code
        if self.project_desc:
            if hasattr(self.project_desc, 'to_alipay_dict'):
                params['project_desc'] = self.project_desc.to_alipay_dict()
            else:
                params['project_desc'] = self.project_desc
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        if self.region_desc:
            if hasattr(self.region_desc, 'to_alipay_dict'):
                params['region_desc'] = self.region_desc.to_alipay_dict()
            else:
                params['region_desc'] = self.region_desc
        if self.spare_code_1:
            if hasattr(self.spare_code_1, 'to_alipay_dict'):
                params['spare_code_1'] = self.spare_code_1.to_alipay_dict()
            else:
                params['spare_code_1'] = self.spare_code_1
        if self.spare_code_2:
            if hasattr(self.spare_code_2, 'to_alipay_dict'):
                params['spare_code_2'] = self.spare_code_2.to_alipay_dict()
            else:
                params['spare_code_2'] = self.spare_code_2
        if self.spare_desc_1:
            if hasattr(self.spare_desc_1, 'to_alipay_dict'):
                params['spare_desc_1'] = self.spare_desc_1.to_alipay_dict()
            else:
                params['spare_desc_1'] = self.spare_desc_1
        if self.spare_desc_2:
            if hasattr(self.spare_desc_2, 'to_alipay_dict'):
                params['spare_desc_2'] = self.spare_desc_2.to_alipay_dict()
            else:
                params['spare_desc_2'] = self.spare_desc_2
        if self.voucher_no:
            if hasattr(self.voucher_no, 'to_alipay_dict'):
                params['voucher_no'] = self.voucher_no.to_alipay_dict()
            else:
                params['voucher_no'] = self.voucher_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountInfoOpenApiOrder()
        if 'account_code' in d:
            o.account_code = d['account_code']
        if 'account_desc' in d:
            o.account_desc = d['account_desc']
        if 'accounting_date' in d:
            o.accounting_date = d['accounting_date']
        if 'accounting_month' in d:
            o.accounting_month = d['accounting_month']
        if 'accounting_type_code' in d:
            o.accounting_type_code = d['accounting_type_code']
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_beq' in d:
            o.amount_beq = d['amount_beq']
        if 'budget_dept_code' in d:
            o.budget_dept_code = d['budget_dept_code']
        if 'budget_dept_desc' in d:
            o.budget_dept_desc = d['budget_dept_desc']
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'company_desc' in d:
            o.company_desc = d['company_desc']
        if 'cost_center_code' in d:
            o.cost_center_code = d['cost_center_code']
        if 'cost_center_desc' in d:
            o.cost_center_desc = d['cost_center_desc']
        if 'currency' in d:
            o.currency = d['currency']
        if 'currency_beq' in d:
            o.currency_beq = d['currency_beq']
        if 'detail_code' in d:
            o.detail_code = d['detail_code']
        if 'detail_desc' in d:
            o.detail_desc = d['detail_desc']
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'industry_desc' in d:
            o.industry_desc = d['industry_desc']
        if 'inter_company_code' in d:
            o.inter_company_code = d['inter_company_code']
        if 'inter_company_desc' in d:
            o.inter_company_desc = d['inter_company_desc']
        if 'je_line_desc' in d:
            o.je_line_desc = d['je_line_desc']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_desc' in d:
            o.product_desc = d['product_desc']
        if 'project_code' in d:
            o.project_code = d['project_code']
        if 'project_desc' in d:
            o.project_desc = d['project_desc']
        if 'region_code' in d:
            o.region_code = d['region_code']
        if 'region_desc' in d:
            o.region_desc = d['region_desc']
        if 'spare_code_1' in d:
            o.spare_code_1 = d['spare_code_1']
        if 'spare_code_2' in d:
            o.spare_code_2 = d['spare_code_2']
        if 'spare_desc_1' in d:
            o.spare_desc_1 = d['spare_desc_1']
        if 'spare_desc_2' in d:
            o.spare_desc_2 = d['spare_desc_2']
        if 'voucher_no' in d:
            o.voucher_no = d['voucher_no']
        return o


