#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SceneContent import SceneContent
from alipay.aop.api.domain.SceneDetail import SceneDetail


class AlipaySocialBaseSceneContentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseSceneContentQueryResponse, self).__init__()
        self._scene_content = None
        self._scene_detail = None
        self._scheme = None

    @property
    def scene_content(self):
        return self._scene_content

    @scene_content.setter
    def scene_content(self, value):
        if isinstance(value, list):
            self._scene_content = list()
            for i in value:
                if isinstance(i, SceneContent):
                    self._scene_content.append(i)
                else:
                    self._scene_content.append(SceneContent.from_alipay_dict(i))
    @property
    def scene_detail(self):
        return self._scene_detail

    @scene_detail.setter
    def scene_detail(self, value):
        if isinstance(value, SceneDetail):
            self._scene_detail = value
        else:
            self._scene_detail = SceneDetail.from_alipay_dict(value)
    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, value):
        self._scheme = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseSceneContentQueryResponse, self).parse_response_content(response_content)
        if 'scene_content' in response:
            self.scene_content = response['scene_content']
        if 'scene_detail' in response:
            self.scene_detail = response['scene_detail']
        if 'scheme' in response:
            self.scheme = response['scheme']
