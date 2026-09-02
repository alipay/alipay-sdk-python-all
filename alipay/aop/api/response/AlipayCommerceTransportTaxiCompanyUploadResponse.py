#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ImportFailItem import ImportFailItem


class AlipayCommerceTransportTaxiCompanyUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTaxiCompanyUploadResponse, self).__init__()
        self._fail_count = None
        self._fail_items = None
        self._success_count = None

    @property
    def fail_count(self):
        return self._fail_count

    @fail_count.setter
    def fail_count(self, value):
        self._fail_count = value
    @property
    def fail_items(self):
        return self._fail_items

    @fail_items.setter
    def fail_items(self, value):
        if isinstance(value, list):
            self._fail_items = list()
            for i in value:
                if isinstance(i, ImportFailItem):
                    self._fail_items.append(i)
                else:
                    self._fail_items.append(ImportFailItem.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTaxiCompanyUploadResponse, self).parse_response_content(response_content)
        if 'fail_count' in response:
            self.fail_count = response['fail_count']
        if 'fail_items' in response:
            self.fail_items = response['fail_items']
        if 'success_count' in response:
            self.success_count = response['success_count']
