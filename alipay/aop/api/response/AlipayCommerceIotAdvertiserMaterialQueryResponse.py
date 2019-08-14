#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotAdvertiserMaterialQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotAdvertiserMaterialQueryResponse, self).__init__()
        self._id = None
        self._material_url = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def material_url(self):
        return self._material_url

    @material_url.setter
    def material_url(self, value):
        self._material_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotAdvertiserMaterialQueryResponse, self).parse_response_content(response_content)
        if 'id' in response:
            self.id = response['id']
        if 'material_url' in response:
            self.material_url = response['material_url']
