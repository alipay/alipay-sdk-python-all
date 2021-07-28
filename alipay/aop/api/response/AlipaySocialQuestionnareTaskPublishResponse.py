#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialQuestionnareTaskPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialQuestionnareTaskPublishResponse, self).__init__()
        self._ext_info = None
        self._out_request_no = None
        self._qstn_id = None
        self._rmt_qstn_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def qstn_id(self):
        return self._qstn_id

    @qstn_id.setter
    def qstn_id(self, value):
        self._qstn_id = value
    @property
    def rmt_qstn_id(self):
        return self._rmt_qstn_id

    @rmt_qstn_id.setter
    def rmt_qstn_id(self, value):
        self._rmt_qstn_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialQuestionnareTaskPublishResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'qstn_id' in response:
            self.qstn_id = response['qstn_id']
        if 'rmt_qstn_id' in response:
            self.rmt_qstn_id = response['rmt_qstn_id']
