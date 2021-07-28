#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniPublicRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPublicRelationQueryResponse, self).__init__()
        self._public_id = None
        self._public_name = None

    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPublicRelationQueryResponse, self).parse_response_content(response_content)
        if 'public_id' in response:
            self.public_id = response['public_id']
        if 'public_name' in response:
            self.public_name = response['public_name']
