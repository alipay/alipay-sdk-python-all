#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsassetprodPetprofileDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsassetprodPetprofileDeleteResponse, self).__init__()
        self._delete_flag = None

    @property
    def delete_flag(self):
        return self._delete_flag

    @delete_flag.setter
    def delete_flag(self, value):
        self._delete_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsassetprodPetprofileDeleteResponse, self).parse_response_content(response_content)
        if 'delete_flag' in response:
            self.delete_flag = response['delete_flag']
