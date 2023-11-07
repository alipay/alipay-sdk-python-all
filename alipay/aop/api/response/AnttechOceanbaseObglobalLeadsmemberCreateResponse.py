#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FxiaokeOperateLeadsMemberParams import FxiaokeOperateLeadsMemberParams


class AnttechOceanbaseObglobalLeadsmemberCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalLeadsmemberCreateResponse, self).__init__()
        self._biz_error_code = None
        self._biz_error_msg = None
        self._biz_success = None
        self._result = None

    @property
    def biz_error_code(self):
        return self._biz_error_code

    @biz_error_code.setter
    def biz_error_code(self, value):
        self._biz_error_code = value
    @property
    def biz_error_msg(self):
        return self._biz_error_msg

    @biz_error_msg.setter
    def biz_error_msg(self, value):
        self._biz_error_msg = value
    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, FxiaokeOperateLeadsMemberParams):
            self._result = value
        else:
            self._result = FxiaokeOperateLeadsMemberParams.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalLeadsmemberCreateResponse, self).parse_response_content(response_content)
        if 'biz_error_code' in response:
            self.biz_error_code = response['biz_error_code']
        if 'biz_error_msg' in response:
            self.biz_error_msg = response['biz_error_msg']
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
        if 'result' in response:
            self.result = response['result']
