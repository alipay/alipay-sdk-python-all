#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementPermissionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementPermissionCreateResponse, self).__init__()
        self._deduct_permission = None
        self._effective_time_end = None
        self._effective_time_start = None

    @property
    def deduct_permission(self):
        return self._deduct_permission

    @deduct_permission.setter
    def deduct_permission(self, value):
        self._deduct_permission = value
    @property
    def effective_time_end(self):
        return self._effective_time_end

    @effective_time_end.setter
    def effective_time_end(self, value):
        self._effective_time_end = value
    @property
    def effective_time_start(self):
        return self._effective_time_start

    @effective_time_start.setter
    def effective_time_start(self, value):
        self._effective_time_start = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementPermissionCreateResponse, self).parse_response_content(response_content)
        if 'deduct_permission' in response:
            self.deduct_permission = response['deduct_permission']
        if 'effective_time_end' in response:
            self.effective_time_end = response['effective_time_end']
        if 'effective_time_start' in response:
            self.effective_time_start = response['effective_time_start']
