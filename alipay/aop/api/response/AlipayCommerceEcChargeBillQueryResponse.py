#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceFeeInfo import ServiceFeeInfo


class AlipayCommerceEcChargeBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcChargeBillQueryResponse, self).__init__()
        self._service_fee_list = None

    @property
    def service_fee_list(self):
        return self._service_fee_list

    @service_fee_list.setter
    def service_fee_list(self, value):
        if isinstance(value, list):
            self._service_fee_list = list()
            for i in value:
                if isinstance(i, ServiceFeeInfo):
                    self._service_fee_list.append(i)
                else:
                    self._service_fee_list.append(ServiceFeeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcChargeBillQueryResponse, self).parse_response_content(response_content)
        if 'service_fee_list' in response:
            self.service_fee_list = response['service_fee_list']
