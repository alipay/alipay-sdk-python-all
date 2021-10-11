#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmpeSceneResponse import AmpeSceneResponse
from alipay.aop.api.domain.AmpeSceneResponse import AmpeSceneResponse


class AlipayOpenMiniAmpeUsersceneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeUsersceneQueryResponse, self).__init__()
        self._disable_scene_info_list = None
        self._enable_scene_info_list = None

    @property
    def disable_scene_info_list(self):
        return self._disable_scene_info_list

    @disable_scene_info_list.setter
    def disable_scene_info_list(self, value):
        if isinstance(value, AmpeSceneResponse):
            self._disable_scene_info_list = value
        else:
            self._disable_scene_info_list = AmpeSceneResponse.from_alipay_dict(value)
    @property
    def enable_scene_info_list(self):
        return self._enable_scene_info_list

    @enable_scene_info_list.setter
    def enable_scene_info_list(self, value):
        if isinstance(value, list):
            self._enable_scene_info_list = list()
            for i in value:
                if isinstance(i, AmpeSceneResponse):
                    self._enable_scene_info_list.append(i)
                else:
                    self._enable_scene_info_list.append(AmpeSceneResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeUsersceneQueryResponse, self).parse_response_content(response_content)
        if 'disable_scene_info_list' in response:
            self.disable_scene_info_list = response['disable_scene_info_list']
        if 'enable_scene_info_list' in response:
            self.enable_scene_info_list = response['enable_scene_info_list']
