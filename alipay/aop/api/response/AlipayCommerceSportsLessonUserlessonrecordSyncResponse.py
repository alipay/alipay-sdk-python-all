#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceSportsLessonUserlessonrecordSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsLessonUserlessonrecordSyncResponse, self).__init__()
        self._sport_coin_num = None

    @property
    def sport_coin_num(self):
        return self._sport_coin_num

    @sport_coin_num.setter
    def sport_coin_num(self, value):
        self._sport_coin_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsLessonUserlessonrecordSyncResponse, self).parse_response_content(response_content)
        if 'sport_coin_num' in response:
            self.sport_coin_num = response['sport_coin_num']
