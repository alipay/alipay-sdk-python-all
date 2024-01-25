#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OBCompanyDTO import OBCompanyDTO


class AnttechOceanbaseCompanyBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseCompanyBatchqueryResponse, self).__init__()
        self._company_list = None

    @property
    def company_list(self):
        return self._company_list

    @company_list.setter
    def company_list(self, value):
        if isinstance(value, list):
            self._company_list = list()
            for i in value:
                if isinstance(i, OBCompanyDTO):
                    self._company_list.append(i)
                else:
                    self._company_list.append(OBCompanyDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseCompanyBatchqueryResponse, self).parse_response_content(response_content)
        if 'company_list' in response:
            self.company_list = response['company_list']
