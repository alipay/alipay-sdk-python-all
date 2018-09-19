#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperatorInfoModel import OperatorInfoModel


class KoubeiMerchantOperatorSearchBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMerchantOperatorSearchBatchqueryResponse, self).__init__()
        self._current_page = None
        self._operator_info_models = None
        self._total_items = None
        self._total_pages = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def operator_info_models(self):
        return self._operator_info_models

    @operator_info_models.setter
    def operator_info_models(self, value):
        if isinstance(value, list):
            self._operator_info_models = list()
            for i in value:
                if isinstance(i, OperatorInfoModel):
                    self._operator_info_models.append(i)
                else:
                    self._operator_info_models.append(OperatorInfoModel.from_alipay_dict(i))
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMerchantOperatorSearchBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'operator_info_models' in response:
            self.operator_info_models = response['operator_info_models']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
