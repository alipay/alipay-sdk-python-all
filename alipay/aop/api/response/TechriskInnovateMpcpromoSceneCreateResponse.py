#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class TechriskInnovateMpcpromoSceneCreateResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoSceneCreateResponse, self).__init__()
        self._illegal_goods_list = None
        self._scene_id = None

    @property
    def illegal_goods_list(self):
        return self._illegal_goods_list

    @illegal_goods_list.setter
    def illegal_goods_list(self, value):
        if isinstance(value, list):
            self._illegal_goods_list = list()
            for i in value:
                self._illegal_goods_list.append(i)
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoSceneCreateResponse, self).parse_response_content(response_content)
        if 'illegal_goods_list' in response:
            self.illegal_goods_list = response['illegal_goods_list']
        if 'scene_id' in response:
            self.scene_id = response['scene_id']
