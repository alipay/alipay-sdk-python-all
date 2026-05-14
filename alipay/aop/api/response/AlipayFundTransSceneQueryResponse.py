#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneApplyRecord import SceneApplyRecord


class AlipayFundTransSceneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransSceneQueryResponse, self).__init__()
        self._scene_info_list = None

    @property
    def scene_info_list(self):
        return self._scene_info_list

    @scene_info_list.setter
    def scene_info_list(self, value):
        if isinstance(value, list):
            self._scene_info_list = list()
            for i in value:
                if isinstance(i, SceneApplyRecord):
                    self._scene_info_list.append(i)
                else:
                    self._scene_info_list.append(SceneApplyRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransSceneQueryResponse, self).parse_response_content(response_content)
        if 'scene_info_list' in response:
            self.scene_info_list = response['scene_info_list']
