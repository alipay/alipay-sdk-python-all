#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinanceMemberInfo import FinanceMemberInfo
from alipay.aop.api.domain.FinanceCreditItem import FinanceCreditItem
from alipay.aop.api.domain.FinanceInvoiceInfo import FinanceInvoiceInfo
from alipay.aop.api.domain.FinancePurchaseInfo import FinancePurchaseInfo
from alipay.aop.api.domain.FinanceMemberInfo import FinanceMemberInfo


class FinanceReceivableInfo(object):

    def __init__(self):
        self._amount = None
        self._core_business_info = None
        self._credit_ids = None
        self._credit_idxs = None
        self._currency = None
        self._expire_date = None
        self._invoice_list = None
        self._memo = None
        self._out_asset_id = None
        self._purchase = None
        self._supplier_info = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def core_business_info(self):
        return self._core_business_info

    @core_business_info.setter
    def core_business_info(self, value):
        if isinstance(value, FinanceMemberInfo):
            self._core_business_info = value
        else:
            self._core_business_info = FinanceMemberInfo.from_alipay_dict(value)
    @property
    def credit_ids(self):
        return self._credit_ids

    @credit_ids.setter
    def credit_ids(self, value):
        if isinstance(value, list):
            self._credit_ids = list()
            for i in value:
                self._credit_ids.append(i)
    @property
    def credit_idxs(self):
        return self._credit_idxs

    @credit_idxs.setter
    def credit_idxs(self, value):
        if isinstance(value, list):
            self._credit_idxs = list()
            for i in value:
                if isinstance(i, FinanceCreditItem):
                    self._credit_idxs.append(i)
                else:
                    self._credit_idxs.append(FinanceCreditItem.from_alipay_dict(i))
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def invoice_list(self):
        return self._invoice_list

    @invoice_list.setter
    def invoice_list(self, value):
        if isinstance(value, list):
            self._invoice_list = list()
            for i in value:
                if isinstance(i, FinanceInvoiceInfo):
                    self._invoice_list.append(i)
                else:
                    self._invoice_list.append(FinanceInvoiceInfo.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_asset_id(self):
        return self._out_asset_id

    @out_asset_id.setter
    def out_asset_id(self, value):
        self._out_asset_id = value
    @property
    def purchase(self):
        return self._purchase

    @purchase.setter
    def purchase(self, value):
        if isinstance(value, FinancePurchaseInfo):
            self._purchase = value
        else:
            self._purchase = FinancePurchaseInfo.from_alipay_dict(value)
    @property
    def supplier_info(self):
        return self._supplier_info

    @supplier_info.setter
    def supplier_info(self, value):
        if isinstance(value, FinanceMemberInfo):
            self._supplier_info = value
        else:
            self._supplier_info = FinanceMemberInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.core_business_info:
            if hasattr(self.core_business_info, 'to_alipay_dict'):
                params['core_business_info'] = self.core_business_info.to_alipay_dict()
            else:
                params['core_business_info'] = self.core_business_info
        if self.credit_ids:
            if isinstance(self.credit_ids, list):
                for i in range(0, len(self.credit_ids)):
                    element = self.credit_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_ids[i] = element.to_alipay_dict()
            if hasattr(self.credit_ids, 'to_alipay_dict'):
                params['credit_ids'] = self.credit_ids.to_alipay_dict()
            else:
                params['credit_ids'] = self.credit_ids
        if self.credit_idxs:
            if isinstance(self.credit_idxs, list):
                for i in range(0, len(self.credit_idxs)):
                    element = self.credit_idxs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_idxs[i] = element.to_alipay_dict()
            if hasattr(self.credit_idxs, 'to_alipay_dict'):
                params['credit_idxs'] = self.credit_idxs.to_alipay_dict()
            else:
                params['credit_idxs'] = self.credit_idxs
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.invoice_list:
            if isinstance(self.invoice_list, list):
                for i in range(0, len(self.invoice_list)):
                    element = self.invoice_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_list, 'to_alipay_dict'):
                params['invoice_list'] = self.invoice_list.to_alipay_dict()
            else:
                params['invoice_list'] = self.invoice_list
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_asset_id:
            if hasattr(self.out_asset_id, 'to_alipay_dict'):
                params['out_asset_id'] = self.out_asset_id.to_alipay_dict()
            else:
                params['out_asset_id'] = self.out_asset_id
        if self.purchase:
            if hasattr(self.purchase, 'to_alipay_dict'):
                params['purchase'] = self.purchase.to_alipay_dict()
            else:
                params['purchase'] = self.purchase
        if self.supplier_info:
            if hasattr(self.supplier_info, 'to_alipay_dict'):
                params['supplier_info'] = self.supplier_info.to_alipay_dict()
            else:
                params['supplier_info'] = self.supplier_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinanceReceivableInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'core_business_info' in d:
            o.core_business_info = d['core_business_info']
        if 'credit_ids' in d:
            o.credit_ids = d['credit_ids']
        if 'credit_idxs' in d:
            o.credit_idxs = d['credit_idxs']
        if 'currency' in d:
            o.currency = d['currency']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'invoice_list' in d:
            o.invoice_list = d['invoice_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_asset_id' in d:
            o.out_asset_id = d['out_asset_id']
        if 'purchase' in d:
            o.purchase = d['purchase']
        if 'supplier_info' in d:
            o.supplier_info = d['supplier_info']
        return o


