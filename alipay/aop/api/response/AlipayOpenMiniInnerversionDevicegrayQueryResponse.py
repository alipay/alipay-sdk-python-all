#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppGrayGroupDto import MiniAppGrayGroupDto


class AlipayOpenMiniInnerversionDevicegrayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionDevicegrayQueryResponse, self).__init__()
        self._device_no_list = None
        self._gray_groups = None
        self._name = None

    @property
    def device_no_list(self):
        return self._device_no_list

    @device_no_list.setter
    def device_no_list(self, value):
        if isinstance(value, list):
            self._device_no_list = list()
            for i in value:
                self._device_no_list.append(i)
    @property
    def gray_groups(self):
        return self._gray_groups

    @gray_groups.setter
    def gray_groups(self, value):
        if isinstance(value, list):
            self._gray_groups = list()
            for i in value:
                if isinstance(i, MiniAppGrayGroupDto):
                    self._gray_groups.append(i)
                else:
                    self._gray_groups.append(MiniAppGrayGroupDto.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionDevicegrayQueryResponse, self).parse_response_content(response_content)
        if 'device_no_list' in response:
            self.device_no_list = response['device_no_list']
        if 'gray_groups' in response:
            self.gray_groups = response['gray_groups']
        if 'name' in response:
            self.name = response['name']
