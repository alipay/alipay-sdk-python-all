#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcEnterpriseAddressDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseAddressDeleteResponse, self).__init__()
        self._fail_address_id_list = None

    @property
    def fail_address_id_list(self):
        return self._fail_address_id_list

    @fail_address_id_list.setter
    def fail_address_id_list(self, value):
        if isinstance(value, list):
            self._fail_address_id_list = list()
            for i in value:
                self._fail_address_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseAddressDeleteResponse, self).parse_response_content(response_content)
        if 'fail_address_id_list' in response:
            self.fail_address_id_list = response['fail_address_id_list']
