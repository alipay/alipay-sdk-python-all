#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceItem import ServiceItem


class AlipayCommerceMedicalHmItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHmItemQueryResponse, self).__init__()
        self._has_free = None
        self._has_more = None
        self._page_no = None
        self._page_size = None
        self._service_item_list = None
        self._service_package_id = None
        self._service_package_name = None
        self._service_package_order_id = None
        self._total_count = None
        self._total_pages = None

    @property
    def has_free(self):
        return self._has_free

    @has_free.setter
    def has_free(self, value):
        self._has_free = value
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def service_item_list(self):
        return self._service_item_list

    @service_item_list.setter
    def service_item_list(self, value):
        if isinstance(value, list):
            self._service_item_list = list()
            for i in value:
                if isinstance(i, ServiceItem):
                    self._service_item_list.append(i)
                else:
                    self._service_item_list.append(ServiceItem.from_alipay_dict(i))
    @property
    def service_package_id(self):
        return self._service_package_id

    @service_package_id.setter
    def service_package_id(self, value):
        self._service_package_id = value
    @property
    def service_package_name(self):
        return self._service_package_name

    @service_package_name.setter
    def service_package_name(self, value):
        self._service_package_name = value
    @property
    def service_package_order_id(self):
        return self._service_package_order_id

    @service_package_order_id.setter
    def service_package_order_id(self, value):
        self._service_package_order_id = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHmItemQueryResponse, self).parse_response_content(response_content)
        if 'has_free' in response:
            self.has_free = response['has_free']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'service_item_list' in response:
            self.service_item_list = response['service_item_list']
        if 'service_package_id' in response:
            self.service_package_id = response['service_package_id']
        if 'service_package_name' in response:
            self.service_package_name = response['service_package_name']
        if 'service_package_order_id' in response:
            self.service_package_order_id = response['service_package_order_id']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
