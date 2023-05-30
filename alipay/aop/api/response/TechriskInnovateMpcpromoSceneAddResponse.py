#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class TechriskInnovateMpcpromoSceneAddResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoSceneAddResponse, self).__init__()
        self._illegal_goods_list = None

    @property
    def illegal_goods_list(self):
        return self._illegal_goods_list

    @illegal_goods_list.setter
    def illegal_goods_list(self, value):
        if isinstance(value, list):
            self._illegal_goods_list = list()
            for i in value:
                self._illegal_goods_list.append(i)

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoSceneAddResponse, self).parse_response_content(response_content)
        if 'illegal_goods_list' in response:
            self.illegal_goods_list = response['illegal_goods_list']
