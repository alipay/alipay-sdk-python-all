#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QueryInvoiceInfoByOuOpenApiDTO import QueryInvoiceInfoByOuOpenApiDTO


class AlipayBossFncInvoiceInfoQueryModel(object):

    def __init__(self):
        self._query_invoice_info_by_ou_open_api_dto = None

    @property
    def query_invoice_info_by_ou_open_api_dto(self):
        return self._query_invoice_info_by_ou_open_api_dto

    @query_invoice_info_by_ou_open_api_dto.setter
    def query_invoice_info_by_ou_open_api_dto(self, value):
        if isinstance(value, QueryInvoiceInfoByOuOpenApiDTO):
            self._query_invoice_info_by_ou_open_api_dto = value
        else:
            self._query_invoice_info_by_ou_open_api_dto = QueryInvoiceInfoByOuOpenApiDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.query_invoice_info_by_ou_open_api_dto:
            if hasattr(self.query_invoice_info_by_ou_open_api_dto, 'to_alipay_dict'):
                params['query_invoice_info_by_ou_open_api_dto'] = self.query_invoice_info_by_ou_open_api_dto.to_alipay_dict()
            else:
                params['query_invoice_info_by_ou_open_api_dto'] = self.query_invoice_info_by_ou_open_api_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoiceInfoQueryModel()
        if 'query_invoice_info_by_ou_open_api_dto' in d:
            o.query_invoice_info_by_ou_open_api_dto = d['query_invoice_info_by_ou_open_api_dto']
        return o


