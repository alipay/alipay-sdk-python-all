#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiServindustryExerciseNoticeCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryExerciseNoticeCreateResponse, self).__init__()
        self._notice_id = None

    @property
    def notice_id(self):
        return self._notice_id

    @notice_id.setter
    def notice_id(self, value):
        self._notice_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryExerciseNoticeCreateResponse, self).parse_response_content(response_content)
        if 'notice_id' in response:
            self.notice_id = response['notice_id']
