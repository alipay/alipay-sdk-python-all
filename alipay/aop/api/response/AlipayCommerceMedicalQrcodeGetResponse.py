#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalQrcodeGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalQrcodeGetResponse, self).__init__()
        self._city_code = None
        self._city_name = None
        self._ins_city_code = None
        self._ins_city_name = None
        self._qrcode = None
        self._relation_type = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def ins_city_code(self):
        return self._ins_city_code

    @ins_city_code.setter
    def ins_city_code(self, value):
        self._ins_city_code = value
    @property
    def ins_city_name(self):
        return self._ins_city_name

    @ins_city_name.setter
    def ins_city_name(self, value):
        self._ins_city_name = value
    @property
    def qrcode(self):
        return self._qrcode

    @qrcode.setter
    def qrcode(self, value):
        self._qrcode = value
    @property
    def relation_type(self):
        return self._relation_type

    @relation_type.setter
    def relation_type(self, value):
        self._relation_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalQrcodeGetResponse, self).parse_response_content(response_content)
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'city_name' in response:
            self.city_name = response['city_name']
        if 'ins_city_code' in response:
            self.ins_city_code = response['ins_city_code']
        if 'ins_city_name' in response:
            self.ins_city_name = response['ins_city_name']
        if 'qrcode' in response:
            self.qrcode = response['qrcode']
        if 'relation_type' in response:
            self.relation_type = response['relation_type']
