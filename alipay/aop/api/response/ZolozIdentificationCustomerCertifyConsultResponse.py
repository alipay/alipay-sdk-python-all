#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZolozIdentificationCustomerCertifyConsultResponse(AlipayResponse):

    def __init__(self):
        super(ZolozIdentificationCustomerCertifyConsultResponse, self).__init__()
        self._biz_id = None
        self._img_str = None

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

    def parse_response_content(self, response_content):
        response = super(ZolozIdentificationCustomerCertifyConsultResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'img_str' in response:
            self.img_str = response['img_str']
