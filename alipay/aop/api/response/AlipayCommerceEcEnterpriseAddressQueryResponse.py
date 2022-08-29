#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AddressInfoDTO import AddressInfoDTO


class AlipayCommerceEcEnterpriseAddressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcEnterpriseAddressQueryResponse, self).__init__()
        self._current_page = None
        self._enterprise_address_info_list = None
        self._total_num = None
        self._total_pages = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def enterprise_address_info_list(self):
        return self._enterprise_address_info_list

    @enterprise_address_info_list.setter
    def enterprise_address_info_list(self, value):
        if isinstance(value, list):
            self._enterprise_address_info_list = list()
            for i in value:
                if isinstance(i, AddressInfoDTO):
                    self._enterprise_address_info_list.append(i)
                else:
                    self._enterprise_address_info_list.append(AddressInfoDTO.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcEnterpriseAddressQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'enterprise_address_info_list' in response:
            self.enterprise_address_info_list = response['enterprise_address_info_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
