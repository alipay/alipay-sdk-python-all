#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserOnlineGameDataInfo import UserOnlineGameDataInfo


class AlipayCommerceSportsOnlinegameUsergamedataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsOnlinegameUsergamedataQueryResponse, self).__init__()
        self._has_more = None
        self._user_online_game_data_info_list = None

    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def user_online_game_data_info_list(self):
        return self._user_online_game_data_info_list

    @user_online_game_data_info_list.setter
    def user_online_game_data_info_list(self, value):
        if isinstance(value, list):
            self._user_online_game_data_info_list = list()
            for i in value:
                if isinstance(i, UserOnlineGameDataInfo):
                    self._user_online_game_data_info_list.append(i)
                else:
                    self._user_online_game_data_info_list.append(UserOnlineGameDataInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsOnlinegameUsergamedataQueryResponse, self).parse_response_content(response_content)
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'user_online_game_data_info_list' in response:
            self.user_online_game_data_info_list = response['user_online_game_data_info_list']
