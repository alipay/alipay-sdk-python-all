#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceOrderBaseInfo import ServiceOrderBaseInfo


class AlipayCommerceEcServiceOrderBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcServiceOrderBatchqueryResponse, self).__init__()
        self._service_order_base_info_list = None

    @property
    def service_order_base_info_list(self):
        return self._service_order_base_info_list

    @service_order_base_info_list.setter
    def service_order_base_info_list(self, value):
        if isinstance(value, list):
            self._service_order_base_info_list = list()
            for i in value:
                if isinstance(i, ServiceOrderBaseInfo):
                    self._service_order_base_info_list.append(i)
                else:
                    self._service_order_base_info_list.append(ServiceOrderBaseInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcServiceOrderBatchqueryResponse, self).parse_response_content(response_content)
        if 'service_order_base_info_list' in response:
            self.service_order_base_info_list = response['service_order_base_info_list']
