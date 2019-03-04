#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneContentCommunityLabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneContentCommunityLabelQueryResponse, self).__init__()
        self._label_group_list = None
        self._scene_key = None
        self._scene_name = None

    @property
    def label_group_list(self):
        return self._label_group_list

    @label_group_list.setter
    def label_group_list(self, value):
        self._label_group_list = value
    @property
    def scene_key(self):
        return self._scene_key

    @scene_key.setter
    def scene_key(self, value):
        self._scene_key = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneContentCommunityLabelQueryResponse, self).parse_response_content(response_content)
        if 'label_group_list' in response:
            self.label_group_list = response['label_group_list']
        if 'scene_key' in response:
            self.scene_key = response['scene_key']
        if 'scene_name' in response:
            self.scene_name = response['scene_name']
