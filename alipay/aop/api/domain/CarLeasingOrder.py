#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarLeasingOrder(object):

    def __init__(self):
        self._cert_no = None
        self._coc_file = None
        self._company_name = None
        self._dealer_company_name = None
        self._down_payment_percent = None
        self._installment_periods = None
        self._insurance_policy_file = None
        self._invoice_file = None
        self._legal_representative_cert_no = None
        self._legal_representative_name = None
        self._loan_amount = None
        self._mobile = None
        self._name = None
        self._remark = None
        self._sales_contract_file = None
        self._sales_contract_id = None
        self._uscc = None
        self._veh_model = None
        self._veh_price = None
        self._vin = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def coc_file(self):
        return self._coc_file

    @coc_file.setter
    def coc_file(self, value):
        self._coc_file = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def dealer_company_name(self):
        return self._dealer_company_name

    @dealer_company_name.setter
    def dealer_company_name(self, value):
        self._dealer_company_name = value
    @property
    def down_payment_percent(self):
        return self._down_payment_percent

    @down_payment_percent.setter
    def down_payment_percent(self, value):
        self._down_payment_percent = value
    @property
    def installment_periods(self):
        return self._installment_periods

    @installment_periods.setter
    def installment_periods(self, value):
        self._installment_periods = value
    @property
    def insurance_policy_file(self):
        return self._insurance_policy_file

    @insurance_policy_file.setter
    def insurance_policy_file(self, value):
        self._insurance_policy_file = value
    @property
    def invoice_file(self):
        return self._invoice_file

    @invoice_file.setter
    def invoice_file(self, value):
        self._invoice_file = value
    @property
    def legal_representative_cert_no(self):
        return self._legal_representative_cert_no

    @legal_representative_cert_no.setter
    def legal_representative_cert_no(self, value):
        self._legal_representative_cert_no = value
    @property
    def legal_representative_name(self):
        return self._legal_representative_name

    @legal_representative_name.setter
    def legal_representative_name(self, value):
        self._legal_representative_name = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def sales_contract_file(self):
        return self._sales_contract_file

    @sales_contract_file.setter
    def sales_contract_file(self, value):
        self._sales_contract_file = value
    @property
    def sales_contract_id(self):
        return self._sales_contract_id

    @sales_contract_id.setter
    def sales_contract_id(self, value):
        self._sales_contract_id = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value
    @property
    def veh_model(self):
        return self._veh_model

    @veh_model.setter
    def veh_model(self, value):
        self._veh_model = value
    @property
    def veh_price(self):
        return self._veh_price

    @veh_price.setter
    def veh_price(self, value):
        self._veh_price = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.coc_file:
            if hasattr(self.coc_file, 'to_alipay_dict'):
                params['coc_file'] = self.coc_file.to_alipay_dict()
            else:
                params['coc_file'] = self.coc_file
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.dealer_company_name:
            if hasattr(self.dealer_company_name, 'to_alipay_dict'):
                params['dealer_company_name'] = self.dealer_company_name.to_alipay_dict()
            else:
                params['dealer_company_name'] = self.dealer_company_name
        if self.down_payment_percent:
            if hasattr(self.down_payment_percent, 'to_alipay_dict'):
                params['down_payment_percent'] = self.down_payment_percent.to_alipay_dict()
            else:
                params['down_payment_percent'] = self.down_payment_percent
        if self.installment_periods:
            if hasattr(self.installment_periods, 'to_alipay_dict'):
                params['installment_periods'] = self.installment_periods.to_alipay_dict()
            else:
                params['installment_periods'] = self.installment_periods
        if self.insurance_policy_file:
            if hasattr(self.insurance_policy_file, 'to_alipay_dict'):
                params['insurance_policy_file'] = self.insurance_policy_file.to_alipay_dict()
            else:
                params['insurance_policy_file'] = self.insurance_policy_file
        if self.invoice_file:
            if hasattr(self.invoice_file, 'to_alipay_dict'):
                params['invoice_file'] = self.invoice_file.to_alipay_dict()
            else:
                params['invoice_file'] = self.invoice_file
        if self.legal_representative_cert_no:
            if hasattr(self.legal_representative_cert_no, 'to_alipay_dict'):
                params['legal_representative_cert_no'] = self.legal_representative_cert_no.to_alipay_dict()
            else:
                params['legal_representative_cert_no'] = self.legal_representative_cert_no
        if self.legal_representative_name:
            if hasattr(self.legal_representative_name, 'to_alipay_dict'):
                params['legal_representative_name'] = self.legal_representative_name.to_alipay_dict()
            else:
                params['legal_representative_name'] = self.legal_representative_name
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.sales_contract_file:
            if hasattr(self.sales_contract_file, 'to_alipay_dict'):
                params['sales_contract_file'] = self.sales_contract_file.to_alipay_dict()
            else:
                params['sales_contract_file'] = self.sales_contract_file
        if self.sales_contract_id:
            if hasattr(self.sales_contract_id, 'to_alipay_dict'):
                params['sales_contract_id'] = self.sales_contract_id.to_alipay_dict()
            else:
                params['sales_contract_id'] = self.sales_contract_id
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        if self.veh_model:
            if hasattr(self.veh_model, 'to_alipay_dict'):
                params['veh_model'] = self.veh_model.to_alipay_dict()
            else:
                params['veh_model'] = self.veh_model
        if self.veh_price:
            if hasattr(self.veh_price, 'to_alipay_dict'):
                params['veh_price'] = self.veh_price.to_alipay_dict()
            else:
                params['veh_price'] = self.veh_price
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarLeasingOrder()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'coc_file' in d:
            o.coc_file = d['coc_file']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'dealer_company_name' in d:
            o.dealer_company_name = d['dealer_company_name']
        if 'down_payment_percent' in d:
            o.down_payment_percent = d['down_payment_percent']
        if 'installment_periods' in d:
            o.installment_periods = d['installment_periods']
        if 'insurance_policy_file' in d:
            o.insurance_policy_file = d['insurance_policy_file']
        if 'invoice_file' in d:
            o.invoice_file = d['invoice_file']
        if 'legal_representative_cert_no' in d:
            o.legal_representative_cert_no = d['legal_representative_cert_no']
        if 'legal_representative_name' in d:
            o.legal_representative_name = d['legal_representative_name']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'remark' in d:
            o.remark = d['remark']
        if 'sales_contract_file' in d:
            o.sales_contract_file = d['sales_contract_file']
        if 'sales_contract_id' in d:
            o.sales_contract_id = d['sales_contract_id']
        if 'uscc' in d:
            o.uscc = d['uscc']
        if 'veh_model' in d:
            o.veh_model = d['veh_model']
        if 'veh_price' in d:
            o.veh_price = d['veh_price']
        if 'vin' in d:
            o.vin = d['vin']
        return o


