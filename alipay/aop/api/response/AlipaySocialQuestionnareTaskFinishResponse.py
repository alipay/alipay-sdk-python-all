#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialQuestionnareTaskFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialQuestionnareTaskFinishResponse, self).__init__()
        self._ext_info = None
        self._qstn_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def qstn_id(self):
        return self._qstn_id

    @qstn_id.setter
    def qstn_id(self, value):
        self._qstn_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialQuestionnareTaskFinishResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'qstn_id' in response:
            self.qstn_id = response['qstn_id']
