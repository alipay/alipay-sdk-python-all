#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceProductInfo import ServiceProductInfo


class AlipayEbppInvoiceEnterpriseserviceBindserviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseserviceBindserviceQueryResponse, self).__init__()
        self._service_product_list = None

    @property
    def service_product_list(self):
        return self._service_product_list

    @service_product_list.setter
    def service_product_list(self, value):
        if isinstance(value, list):
            self._service_product_list = list()
            for i in value:
                if isinstance(i, ServiceProductInfo):
                    self._service_product_list.append(i)
                else:
                    self._service_product_list.append(ServiceProductInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseserviceBindserviceQueryResponse, self).parse_response_content(response_content)
        if 'service_product_list' in response:
            self.service_product_list = response['service_product_list']
