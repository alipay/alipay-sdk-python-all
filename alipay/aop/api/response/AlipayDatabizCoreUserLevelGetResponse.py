#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayUserLevelInfo import AlipayUserLevelInfo


class AlipayDatabizCoreUserLevelGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDatabizCoreUserLevelGetResponse, self).__init__()
        self._user_level_infos = None

    @property
    def user_level_infos(self):
        return self._user_level_infos

    @user_level_infos.setter
    def user_level_infos(self, value):
        if isinstance(value, list):
            self._user_level_infos = list()
            for i in value:
                if isinstance(i, AlipayUserLevelInfo):
                    self._user_level_infos.append(i)
                else:
                    self._user_level_infos.append(AlipayUserLevelInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDatabizCoreUserLevelGetResponse, self).parse_response_content(response_content)
        if 'user_level_infos' in response:
            self.user_level_infos = response['user_level_infos']
