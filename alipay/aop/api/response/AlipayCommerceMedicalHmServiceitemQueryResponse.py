#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceItemInfo import ServiceItemInfo


class AlipayCommerceMedicalHmServiceitemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmServiceitemQueryResponse, self).__init__()
        self._service_item_list = None

    @property
    def service_item_list(self):
        return self._service_item_list

    @service_item_list.setter
    def service_item_list(self, value):
        if isinstance(value, list):
            self._service_item_list = list()
            for i in value:
                if isinstance(i, ServiceItemInfo):
                    self._service_item_list.append(i)
                else:
                    self._service_item_list.append(ServiceItemInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmServiceitemQueryResponse, self).parse_response_content(response_content)
        if 'service_item_list' in response:
            self.service_item_list = response['service_item_list']
