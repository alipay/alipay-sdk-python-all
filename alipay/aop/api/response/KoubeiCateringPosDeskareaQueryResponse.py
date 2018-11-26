#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeskAreaEntity import DeskAreaEntity


class KoubeiCateringPosDeskareaQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosDeskareaQueryResponse, self).__init__()
        self._pos_desk_area_list = None

    @property
    def pos_desk_area_list(self):
        return self._pos_desk_area_list

    @pos_desk_area_list.setter
    def pos_desk_area_list(self, value):
        if isinstance(value, list):
            self._pos_desk_area_list = list()
            for i in value:
                if isinstance(i, DeskAreaEntity):
                    self._pos_desk_area_list.append(i)
                else:
                    self._pos_desk_area_list.append(DeskAreaEntity.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosDeskareaQueryResponse, self).parse_response_content(response_content)
        if 'pos_desk_area_list' in response:
            self.pos_desk_area_list = response['pos_desk_area_list']
