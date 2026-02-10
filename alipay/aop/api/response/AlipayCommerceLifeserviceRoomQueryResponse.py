#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LifeServiceRoom import LifeServiceRoom


class AlipayCommerceLifeserviceRoomQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceRoomQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._room_infos = None
        self._total = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def room_infos(self):
        return self._room_infos

    @room_infos.setter
    def room_infos(self, value):
        if isinstance(value, list):
            self._room_infos = list()
            for i in value:
                if isinstance(i, LifeServiceRoom):
                    self._room_infos.append(i)
                else:
                    self._room_infos.append(LifeServiceRoom.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceRoomQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'room_infos' in response:
            self.room_infos = response['room_infos']
        if 'total' in response:
            self.total = response['total']
