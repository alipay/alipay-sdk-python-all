#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantCreditserviceDetailModifyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantCreditserviceDetailModifyResponse, self).__init__()
        self._credit_service_id = None
        self._version_no = None

    @property
    def credit_service_id(self):
        return self._credit_service_id

    @credit_service_id.setter
    def credit_service_id(self, value):
        self._credit_service_id = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantCreditserviceDetailModifyResponse, self).parse_response_content(response_content)
        if 'credit_service_id' in response:
            self.credit_service_id = response['credit_service_id']
        if 'version_no' in response:
            self.version_no = response['version_no']
