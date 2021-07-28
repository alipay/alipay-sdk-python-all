#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessPropertyDTO import BusinessPropertyDTO


class AlipayDataDataservicePropertyBusinesspropertyBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataservicePropertyBusinesspropertyBatchqueryResponse, self).__init__()
        self._business_propertys = None

    @property
    def business_propertys(self):
        return self._business_propertys

    @business_propertys.setter
    def business_propertys(self, value):
        if isinstance(value, list):
            self._business_propertys = list()
            for i in value:
                if isinstance(i, BusinessPropertyDTO):
                    self._business_propertys.append(i)
                else:
                    self._business_propertys.append(BusinessPropertyDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataservicePropertyBusinesspropertyBatchqueryResponse, self).parse_response_content(response_content)
        if 'business_propertys' in response:
            self.business_propertys = response['business_propertys']
