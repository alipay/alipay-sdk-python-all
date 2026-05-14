#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailPromoactivitySaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailPromoactivitySaveResponse, self).__init__()
        self._activity_type = None
        self._operate_type = None
        self._response_list = None

    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def response_list(self):
        return self._response_list

    @response_list.setter
    def response_list(self, value):
        self._response_list = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailPromoactivitySaveResponse, self).parse_response_content(response_content)
        if 'activity_type' in response:
            self.activity_type = response['activity_type']
        if 'operate_type' in response:
            self.operate_type = response['operate_type']
        if 'response_list' in response:
            self.response_list = response['response_list']
