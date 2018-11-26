#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeskEntity import DeskEntity


class KoubeiCateringPosDeskQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosDeskQueryResponse, self).__init__()
        self._pos_desk_list = None

    @property
    def pos_desk_list(self):
        return self._pos_desk_list

    @pos_desk_list.setter
    def pos_desk_list(self, value):
        if isinstance(value, list):
            self._pos_desk_list = list()
            for i in value:
                if isinstance(i, DeskEntity):
                    self._pos_desk_list.append(i)
                else:
                    self._pos_desk_list.append(DeskEntity.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosDeskQueryResponse, self).parse_response_content(response_content)
        if 'pos_desk_list' in response:
            self.pos_desk_list = response['pos_desk_list']
