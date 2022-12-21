#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserOnlineGameInfo import UserOnlineGameInfo


class AlipayCommerceSportsOnlinegameUsergameSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsOnlinegameUsergameSyncResponse, self).__init__()
        self._user_online_game_info = None

    @property
    def user_online_game_info(self):
        return self._user_online_game_info

    @user_online_game_info.setter
    def user_online_game_info(self, value):
        if isinstance(value, UserOnlineGameInfo):
            self._user_online_game_info = value
        else:
            self._user_online_game_info = UserOnlineGameInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsOnlinegameUsergameSyncResponse, self).parse_response_content(response_content)
        if 'user_online_game_info' in response:
            self.user_online_game_info = response['user_online_game_info']
