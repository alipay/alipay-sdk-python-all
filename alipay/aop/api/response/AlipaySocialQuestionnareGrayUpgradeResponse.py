#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialQuestionnareGrayUpgradeResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialQuestionnareGrayUpgradeResponse, self).__init__()
        self._ext_info = None
        self._gray_percent = None
        self._qstn_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gray_percent(self):
        return self._gray_percent

    @gray_percent.setter
    def gray_percent(self, value):
        self._gray_percent = value
    @property
    def qstn_id(self):
        return self._qstn_id

    @qstn_id.setter
    def qstn_id(self, value):
        self._qstn_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialQuestionnareGrayUpgradeResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'gray_percent' in response:
            self.gray_percent = response['gray_percent']
        if 'qstn_id' in response:
            self.qstn_id = response['qstn_id']
