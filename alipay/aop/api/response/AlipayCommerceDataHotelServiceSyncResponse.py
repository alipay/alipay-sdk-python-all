#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceDataHotelServiceSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataHotelServiceSyncResponse, self).__init__()
        self._audit_msg = None
        self._audit_status = None
        self._hotel_app_id = None
        self._hotel_id = None
        self._outer_hotel_id = None
        self._service_id = None
        self._service_name = None
        self._service_status = None
        self._service_url = None

    @property
    def audit_msg(self):
        return self._audit_msg

    @audit_msg.setter
    def audit_msg(self, value):
        self._audit_msg = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def hotel_app_id(self):
        return self._hotel_app_id

    @hotel_app_id.setter
    def hotel_app_id(self, value):
        self._hotel_app_id = value
    @property
    def hotel_id(self):
        return self._hotel_id

    @hotel_id.setter
    def hotel_id(self, value):
        self._hotel_id = value
    @property
    def outer_hotel_id(self):
        return self._outer_hotel_id

    @outer_hotel_id.setter
    def outer_hotel_id(self, value):
        self._outer_hotel_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataHotelServiceSyncResponse, self).parse_response_content(response_content)
        if 'audit_msg' in response:
            self.audit_msg = response['audit_msg']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'hotel_app_id' in response:
            self.hotel_app_id = response['hotel_app_id']
        if 'hotel_id' in response:
            self.hotel_id = response['hotel_id']
        if 'outer_hotel_id' in response:
            self.outer_hotel_id = response['outer_hotel_id']
        if 'service_id' in response:
            self.service_id = response['service_id']
        if 'service_name' in response:
            self.service_name = response['service_name']
        if 'service_status' in response:
            self.service_status = response['service_status']
        if 'service_url' in response:
            self.service_url = response['service_url']
