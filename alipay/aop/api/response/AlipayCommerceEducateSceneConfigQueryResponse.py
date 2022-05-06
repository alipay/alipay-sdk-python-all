#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneConfigQueryDTO import SceneConfigQueryDTO


class AlipayCommerceEducateSceneConfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneConfigQueryResponse, self).__init__()
        self._scene_config_infos = None

    @property
    def scene_config_infos(self):
        return self._scene_config_infos

    @scene_config_infos.setter
    def scene_config_infos(self, value):
        if isinstance(value, list):
            self._scene_config_infos = list()
            for i in value:
                if isinstance(i, SceneConfigQueryDTO):
                    self._scene_config_infos.append(i)
                else:
                    self._scene_config_infos.append(SceneConfigQueryDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneConfigQueryResponse, self).parse_response_content(response_content)
        if 'scene_config_infos' in response:
            self.scene_config_infos = response['scene_config_infos']
