#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNdeviceWorkstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNdeviceWorkstatusQueryResponse, self).__init__()
        self._bind_status = None
        self._device_sn = None
        self._device_type = None
        self._leads_id = None
        self._operator_contact_number = None
        self._operator_name = None
        self._out_store_id = None
        self._position_id = None
        self._related_device_sn = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def operator_contact_number(self):
        return self._operator_contact_number

    @operator_contact_number.setter
    def operator_contact_number(self, value):
        self._operator_contact_number = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def out_store_id(self):
        return self._out_store_id

    @out_store_id.setter
    def out_store_id(self, value):
        self._out_store_id = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def related_device_sn(self):
        return self._related_device_sn

    @related_device_sn.setter
    def related_device_sn(self, value):
        self._related_device_sn = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNdeviceWorkstatusQueryResponse, self).parse_response_content(response_content)
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'device_sn' in response:
            self.device_sn = response['device_sn']
        if 'device_type' in response:
            self.device_type = response['device_type']
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
        if 'operator_contact_number' in response:
            self.operator_contact_number = response['operator_contact_number']
        if 'operator_name' in response:
            self.operator_name = response['operator_name']
        if 'out_store_id' in response:
            self.out_store_id = response['out_store_id']
        if 'position_id' in response:
            self.position_id = response['position_id']
        if 'related_device_sn' in response:
            self.related_device_sn = response['related_device_sn']
