#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaTorchreplayleftoffliQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaTorchreplayleftoffliQueryResponse, self).__init__()
        self._share_asian_games_spirit_cnt = None
        self._take_flame_cnt = None

    @property
    def share_asian_games_spirit_cnt(self):
        return self._share_asian_games_spirit_cnt

    @share_asian_games_spirit_cnt.setter
    def share_asian_games_spirit_cnt(self, value):
        self._share_asian_games_spirit_cnt = value
    @property
    def take_flame_cnt(self):
        return self._take_flame_cnt

    @take_flame_cnt.setter
    def take_flame_cnt(self, value):
        self._take_flame_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaTorchreplayleftoffliQueryResponse, self).parse_response_content(response_content)
        if 'share_asian_games_spirit_cnt' in response:
            self.share_asian_games_spirit_cnt = response['share_asian_games_spirit_cnt']
        if 'take_flame_cnt' in response:
            self.take_flame_cnt = response['take_flame_cnt']
