#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MapTypeParam import MapTypeParam
from alipay.aop.api.domain.PayContractItemDTO import PayContractItemDTO


class PayContractDTO(object):

    def __init__(self):
        self._account_ext_info = None
        self._account_name = None
        self._account_no = None
        self._account_type = None
        self._agreement_no = None
        self._agreement_source = None
        self._biz_pdcode = None
        self._branch_name = None
        self._company_code = None
        self._currency = None
        self._idempotent_no = None
        self._ip_role_id = None
        self._ip_role_source = None
        self._pay_contract_items = None
        self._payment_type = None
        self._pd_code = None
        self._sales_product_code = None
        self._source = None

    @property
    def account_ext_info(self):
        return self._account_ext_info

    @account_ext_info.setter
    def account_ext_info(self, value):
        if isinstance(value, MapTypeParam):
            self._account_ext_info = value
        else:
            self._account_ext_info = MapTypeParam.from_alipay_dict(value)
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_source(self):
        return self._agreement_source

    @agreement_source.setter
    def agreement_source(self, value):
        self._agreement_source = value
    @property
    def biz_pdcode(self):
        return self._biz_pdcode

    @biz_pdcode.setter
    def biz_pdcode(self, value):
        self._biz_pdcode = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def idempotent_no(self):
        return self._idempotent_no

    @idempotent_no.setter
    def idempotent_no(self, value):
        self._idempotent_no = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def ip_role_source(self):
        return self._ip_role_source

    @ip_role_source.setter
    def ip_role_source(self, value):
        self._ip_role_source = value
    @property
    def pay_contract_items(self):
        return self._pay_contract_items

    @pay_contract_items.setter
    def pay_contract_items(self, value):
        if isinstance(value, list):
            self._pay_contract_items = list()
            for i in value:
                if isinstance(i, PayContractItemDTO):
                    self._pay_contract_items.append(i)
                else:
                    self._pay_contract_items.append(PayContractItemDTO.from_alipay_dict(i))
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_ext_info:
            if hasattr(self.account_ext_info, 'to_alipay_dict'):
                params['account_ext_info'] = self.account_ext_info.to_alipay_dict()
            else:
                params['account_ext_info'] = self.account_ext_info
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.agreement_source:
            if hasattr(self.agreement_source, 'to_alipay_dict'):
                params['agreement_source'] = self.agreement_source.to_alipay_dict()
            else:
                params['agreement_source'] = self.agreement_source
        if self.biz_pdcode:
            if hasattr(self.biz_pdcode, 'to_alipay_dict'):
                params['biz_pdcode'] = self.biz_pdcode.to_alipay_dict()
            else:
                params['biz_pdcode'] = self.biz_pdcode
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.idempotent_no:
            if hasattr(self.idempotent_no, 'to_alipay_dict'):
                params['idempotent_no'] = self.idempotent_no.to_alipay_dict()
            else:
                params['idempotent_no'] = self.idempotent_no
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.ip_role_source:
            if hasattr(self.ip_role_source, 'to_alipay_dict'):
                params['ip_role_source'] = self.ip_role_source.to_alipay_dict()
            else:
                params['ip_role_source'] = self.ip_role_source
        if self.pay_contract_items:
            if isinstance(self.pay_contract_items, list):
                for i in range(0, len(self.pay_contract_items)):
                    element = self.pay_contract_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_contract_items[i] = element.to_alipay_dict()
            if hasattr(self.pay_contract_items, 'to_alipay_dict'):
                params['pay_contract_items'] = self.pay_contract_items.to_alipay_dict()
            else:
                params['pay_contract_items'] = self.pay_contract_items
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayContractDTO()
        if 'account_ext_info' in d:
            o.account_ext_info = d['account_ext_info']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_source' in d:
            o.agreement_source = d['agreement_source']
        if 'biz_pdcode' in d:
            o.biz_pdcode = d['biz_pdcode']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'idempotent_no' in d:
            o.idempotent_no = d['idempotent_no']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'ip_role_source' in d:
            o.ip_role_source = d['ip_role_source']
        if 'pay_contract_items' in d:
            o.pay_contract_items = d['pay_contract_items']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        if 'source' in d:
            o.source = d['source']
        return o


