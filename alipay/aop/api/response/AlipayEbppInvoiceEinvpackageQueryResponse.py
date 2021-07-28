#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PackageItemOpenInfo import PackageItemOpenInfo


class AlipayEbppInvoiceEinvpackageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEinvpackageQueryResponse, self).__init__()
        self._package_item_info_list = None

    @property
    def package_item_info_list(self):
        return self._package_item_info_list

    @package_item_info_list.setter
    def package_item_info_list(self, value):
        if isinstance(value, list):
            self._package_item_info_list = list()
            for i in value:
                if isinstance(i, PackageItemOpenInfo):
                    self._package_item_info_list.append(i)
                else:
                    self._package_item_info_list.append(PackageItemOpenInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEinvpackageQueryResponse, self).parse_response_content(response_content)
        if 'package_item_info_list' in response:
            self.package_item_info_list = response['package_item_info_list']
