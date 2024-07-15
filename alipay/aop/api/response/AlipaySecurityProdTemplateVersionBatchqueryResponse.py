#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PageDTO import PageDTO


class AlipaySecurityProdTemplateVersionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateVersionBatchqueryResponse, self).__init__()
        self._page_dto = None

    @property
    def page_dto(self):
        return self._page_dto

    @page_dto.setter
    def page_dto(self, value):
        if isinstance(value, PageDTO):
            self._page_dto = value
        else:
            self._page_dto = PageDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateVersionBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_dto' in response:
            self.page_dto = response['page_dto']
