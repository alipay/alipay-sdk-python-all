#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrustAccountInfo import TrustAccountInfo
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo


class AnttechBlockchainFinanceTvpBillBatchqueryModel(object):

    def __init__(self):
        self._page_index = None
        self._page_size = None
        self._payee_account = None
        self._payee_entity = None
        self._payer_entity = None
        self._product_code = None
        self._query_date = None

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        if isinstance(value, TrustAccountInfo):
            self._payee_account = value
        else:
            self._payee_account = TrustAccountInfo.from_alipay_dict(value)
    @property
    def payee_entity(self):
        return self._payee_entity

    @payee_entity.setter
    def payee_entity(self, value):
        if isinstance(value, TrustEntityInfo):
            self._payee_entity = value
        else:
            self._payee_entity = TrustEntityInfo.from_alipay_dict(value)
    @property
    def payer_entity(self):
        return self._payer_entity

    @payer_entity.setter
    def payer_entity(self, value):
        if isinstance(value, TrustEntityInfo):
            self._payer_entity = value
        else:
            self._payer_entity = TrustEntityInfo.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def query_date(self):
        return self._query_date

    @query_date.setter
    def query_date(self, value):
        self._query_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payee_entity:
            if hasattr(self.payee_entity, 'to_alipay_dict'):
                params['payee_entity'] = self.payee_entity.to_alipay_dict()
            else:
                params['payee_entity'] = self.payee_entity
        if self.payer_entity:
            if hasattr(self.payer_entity, 'to_alipay_dict'):
                params['payer_entity'] = self.payer_entity.to_alipay_dict()
            else:
                params['payer_entity'] = self.payer_entity
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.query_date:
            if hasattr(self.query_date, 'to_alipay_dict'):
                params['query_date'] = self.query_date.to_alipay_dict()
            else:
                params['query_date'] = self.query_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTvpBillBatchqueryModel()
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_entity' in d:
            o.payee_entity = d['payee_entity']
        if 'payer_entity' in d:
            o.payer_entity = d['payer_entity']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'query_date' in d:
            o.query_date = d['query_date']
        return o


