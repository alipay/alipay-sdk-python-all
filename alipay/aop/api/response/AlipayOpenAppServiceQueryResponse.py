#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppServiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServiceQueryResponse, self).__init__()
        self._reject_reason = None
        self._service_code = None
        self._service_xml = None
        self._status = None
        self._template_type = None
        self._user_service_delivery_type = None

    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_xml(self):
        return self._service_xml

    @service_xml.setter
    def service_xml(self, value):
        self._service_xml = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value
    @property
    def user_service_delivery_type(self):
        return self._user_service_delivery_type

    @user_service_delivery_type.setter
    def user_service_delivery_type(self, value):
        self._user_service_delivery_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServiceQueryResponse, self).parse_response_content(response_content)
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'service_code' in response:
            self.service_code = response['service_code']
        if 'service_xml' in response:
            self.service_xml = response['service_xml']
        if 'status' in response:
            self.status = response['status']
        if 'template_type' in response:
            self.template_type = response['template_type']
        if 'user_service_delivery_type' in response:
            self.user_service_delivery_type = response['user_service_delivery_type']
