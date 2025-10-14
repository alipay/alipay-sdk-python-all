#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneResult import SceneResult


class AlipayTradeCrowdConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCrowdConsultResponse, self).__init__()
        self._activity_code_list = None
        self._promoted_user = None
        self._scene_result = None

    @property
    def activity_code_list(self):
        return self._activity_code_list

    @activity_code_list.setter
    def activity_code_list(self, value):
        if isinstance(value, list):
            self._activity_code_list = list()
            for i in value:
                self._activity_code_list.append(i)
    @property
    def promoted_user(self):
        return self._promoted_user

    @promoted_user.setter
    def promoted_user(self, value):
        self._promoted_user = value
    @property
    def scene_result(self):
        return self._scene_result

    @scene_result.setter
    def scene_result(self, value):
        if isinstance(value, SceneResult):
            self._scene_result = value
        else:
            self._scene_result = SceneResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCrowdConsultResponse, self).parse_response_content(response_content)
        if 'activity_code_list' in response:
            self.activity_code_list = response['activity_code_list']
        if 'promoted_user' in response:
            self.promoted_user = response['promoted_user']
        if 'scene_result' in response:
            self.scene_result = response['scene_result']
