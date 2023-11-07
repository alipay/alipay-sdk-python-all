#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppItemCategoryConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItemCategoryConsultResponse, self).__init__()
        self._category_error_code = None
        self._category_error_desc = None
        self._category_id = None
        self._category_name = None
        self._status = None

    @property
    def category_error_code(self):
        return self._category_error_code

    @category_error_code.setter
    def category_error_code(self, value):
        self._category_error_code = value
    @property
    def category_error_desc(self):
        return self._category_error_desc

    @category_error_desc.setter
    def category_error_desc(self, value):
        self._category_error_desc = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItemCategoryConsultResponse, self).parse_response_content(response_content)
        if 'category_error_code' in response:
            self.category_error_code = response['category_error_code']
        if 'category_error_desc' in response:
            self.category_error_desc = response['category_error_desc']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'category_name' in response:
            self.category_name = response['category_name']
        if 'status' in response:
            self.status = response['status']
