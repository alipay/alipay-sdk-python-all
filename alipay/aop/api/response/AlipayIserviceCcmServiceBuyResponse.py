#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCcmServiceBuyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmServiceBuyResponse, self).__init__()
        self._service_instance_id = None
        self._tenant_id = None

    @property
    def service_instance_id(self):
        return self._service_instance_id

    @service_instance_id.setter
    def service_instance_id(self, value):
        self._service_instance_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmServiceBuyResponse, self).parse_response_content(response_content)
        if 'service_instance_id' in response:
            self.service_instance_id = response['service_instance_id']
        if 'tenant_id' in response:
            self.tenant_id = response['tenant_id']
