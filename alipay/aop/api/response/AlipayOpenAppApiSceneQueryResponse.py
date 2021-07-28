#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AuthFieldSceneDTO import AuthFieldSceneDTO


class AlipayOpenAppApiSceneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppApiSceneQueryResponse, self).__init__()
        self._auth_field_scene = None

    @property
    def auth_field_scene(self):
        return self._auth_field_scene

    @auth_field_scene.setter
    def auth_field_scene(self, value):
        if isinstance(value, list):
            self._auth_field_scene = list()
            for i in value:
                if isinstance(i, AuthFieldSceneDTO):
                    self._auth_field_scene.append(i)
                else:
                    self._auth_field_scene.append(AuthFieldSceneDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppApiSceneQueryResponse, self).parse_response_content(response_content)
        if 'auth_field_scene' in response:
            self.auth_field_scene = response['auth_field_scene']
