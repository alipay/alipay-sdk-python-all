#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozIdentificationCustomerCertifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationCustomerCertifyQueryResponse, self).__init__()
        self._attack = None
        self._biz_id = None
        self._img_str = None
        self._result = None

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def img_str(self):
        return self._img_str

    @img_str.setter
    def img_str(self, value):
        self._img_str = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationCustomerCertifyQueryResponse, self).parse_response_content(response_content)
        if 'attack' in response:
            self.attack = response['attack']
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'img_str' in response:
            self.img_str = response['img_str']
        if 'result' in response:
            self.result = response['result']
