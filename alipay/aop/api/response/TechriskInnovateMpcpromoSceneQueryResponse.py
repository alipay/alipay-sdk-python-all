#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcSceneQueryInfo import MpcSceneQueryInfo


class TechriskInnovateMpcpromoSceneQueryResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoSceneQueryResponse, self).__init__()
        self._scene_list = None

    @property
    def scene_list(self):
        return self._scene_list

    @scene_list.setter
    def scene_list(self, value):
        if isinstance(value, MpcSceneQueryInfo):
            self._scene_list = value
        else:
            self._scene_list = MpcSceneQueryInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoSceneQueryResponse, self).parse_response_content(response_content)
        if 'scene_list' in response:
            self.scene_list = response['scene_list']
