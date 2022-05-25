#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpOpporDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpOpporDetailQueryResponse, self).__init__()
        self._address = None
        self._leads_id = None
        self._name = None
        self._oppor_id = None
        self._out_biz_no = None
        self._phone = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def oppor_id(self):
        return self._oppor_id

    @oppor_id.setter
    def oppor_id(self, value):
        self._oppor_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpOpporDetailQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
        if 'name' in response:
            self.name = response['name']
        if 'oppor_id' in response:
            self.oppor_id = response['oppor_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'phone' in response:
            self.phone = response['phone']
        if 'status' in response:
            self.status = response['status']
