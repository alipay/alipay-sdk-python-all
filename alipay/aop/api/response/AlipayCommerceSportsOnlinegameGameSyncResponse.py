#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OnlineGameInfo import OnlineGameInfo


class AlipayCommerceSportsOnlinegameGameSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsOnlinegameGameSyncResponse, self).__init__()
        self._online_game_info = None

    @property
    def online_game_info(self):
        return self._online_game_info

    @online_game_info.setter
    def online_game_info(self, value):
        if isinstance(value, OnlineGameInfo):
            self._online_game_info = value
        else:
            self._online_game_info = OnlineGameInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsOnlinegameGameSyncResponse, self).parse_response_content(response_content)
        if 'online_game_info' in response:
            self.online_game_info = response['online_game_info']
