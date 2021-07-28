#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishCommGroupInfo import KbdishCommGroupInfo


class KoubeiCateringDishCommgroupSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishCommgroupSyncResponse, self).__init__()
        self._comm_group_id = None
        self._kbdish_comm_group_info = None

    @property
    def comm_group_id(self):
        return self._comm_group_id

    @comm_group_id.setter
    def comm_group_id(self, value):
        self._comm_group_id = value
    @property
    def kbdish_comm_group_info(self):
        return self._kbdish_comm_group_info

    @kbdish_comm_group_info.setter
    def kbdish_comm_group_info(self, value):
        if isinstance(value, KbdishCommGroupInfo):
            self._kbdish_comm_group_info = value
        else:
            self._kbdish_comm_group_info = KbdishCommGroupInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishCommgroupSyncResponse, self).parse_response_content(response_content)
        if 'comm_group_id' in response:
            self.comm_group_id = response['comm_group_id']
        if 'kbdish_comm_group_info' in response:
            self.kbdish_comm_group_info = response['kbdish_comm_group_info']
