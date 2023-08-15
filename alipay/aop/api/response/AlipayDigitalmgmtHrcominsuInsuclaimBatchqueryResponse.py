#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsuClaimVo import InsuClaimVo


class AlipayDigitalmgmtHrcominsuInsuclaimBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrcominsuInsuclaimBatchqueryResponse, self).__init__()
        self._current_page = None
        self._insu_claim_vos = None
        self._page_size = None
        self._total_count = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def insu_claim_vos(self):
        return self._insu_claim_vos

    @insu_claim_vos.setter
    def insu_claim_vos(self, value):
        if isinstance(value, list):
            self._insu_claim_vos = list()
            for i in value:
                if isinstance(i, InsuClaimVo):
                    self._insu_claim_vos.append(i)
                else:
                    self._insu_claim_vos.append(InsuClaimVo.from_alipay_dict(i))
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrcominsuInsuclaimBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'insu_claim_vos' in response:
            self.insu_claim_vos = response['insu_claim_vos']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
