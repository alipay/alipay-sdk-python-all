#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailBenefitscopeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailBenefitscopeQueryResponse, self).__init__()
        self._activity_id = None
        self._activity_scope_list = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_scope_list(self):
        return self._activity_scope_list

    @activity_scope_list.setter
    def activity_scope_list(self, value):
        if isinstance(value, list):
            self._activity_scope_list = list()
            for i in value:
                self._activity_scope_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailBenefitscopeQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_scope_list' in response:
            self.activity_scope_list = response['activity_scope_list']
