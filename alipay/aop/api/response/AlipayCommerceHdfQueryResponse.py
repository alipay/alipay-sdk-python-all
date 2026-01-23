#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHdfQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHdfQueryResponse, self).__init__()
        self._hdf_user_id = None

    @property
    def hdf_user_id(self):
        return self._hdf_user_id

    @hdf_user_id.setter
    def hdf_user_id(self, value):
        self._hdf_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHdfQueryResponse, self).parse_response_content(response_content)
        if 'hdf_user_id' in response:
            self.hdf_user_id = response['hdf_user_id']
