#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseObglobalQuotationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalQuotationQueryResponse, self).__init__()
        self._quotation_desc_list = None

    @property
    def quotation_desc_list(self):
        return self._quotation_desc_list

    @quotation_desc_list.setter
    def quotation_desc_list(self, value):
        if isinstance(value, list):
            self._quotation_desc_list = list()
            for i in value:
                self._quotation_desc_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalQuotationQueryResponse, self).parse_response_content(response_content)
        if 'quotation_desc_list' in response:
            self.quotation_desc_list = response['quotation_desc_list']
