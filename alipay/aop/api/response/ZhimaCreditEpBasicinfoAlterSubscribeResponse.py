#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpBasicInfo import EpBasicInfo


class ZhimaCreditEpBasicinfoAlterSubscribeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpBasicinfoAlterSubscribeResponse, self).__init__()
        self._ep_basic_infos = None
        self._listen_item_list = None
        self._listen_no = None

    @property
    def ep_basic_infos(self):
        return self._ep_basic_infos

    @ep_basic_infos.setter
    def ep_basic_infos(self, value):
        if isinstance(value, list):
            self._ep_basic_infos = list()
            for i in value:
                if isinstance(i, EpBasicInfo):
                    self._ep_basic_infos.append(i)
                else:
                    self._ep_basic_infos.append(EpBasicInfo.from_alipay_dict(i))
    @property
    def listen_item_list(self):
        return self._listen_item_list

    @listen_item_list.setter
    def listen_item_list(self, value):
        if isinstance(value, list):
            self._listen_item_list = list()
            for i in value:
                self._listen_item_list.append(i)
    @property
    def listen_no(self):
        return self._listen_no

    @listen_no.setter
    def listen_no(self, value):
        self._listen_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpBasicinfoAlterSubscribeResponse, self).parse_response_content(response_content)
        if 'ep_basic_infos' in response:
            self.ep_basic_infos = response['ep_basic_infos']
        if 'listen_item_list' in response:
            self.listen_item_list = response['listen_item_list']
        if 'listen_no' in response:
            self.listen_no = response['listen_no']
