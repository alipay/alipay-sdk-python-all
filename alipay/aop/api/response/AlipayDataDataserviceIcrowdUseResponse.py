#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IcrowdUseResp import IcrowdUseResp


class AlipayDataDataserviceIcrowdUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceIcrowdUseResponse, self).__init__()
        self._icrowd_use_resp = None

    @property
    def icrowd_use_resp(self):
        return self._icrowd_use_resp

    @icrowd_use_resp.setter
    def icrowd_use_resp(self, value):
        if isinstance(value, IcrowdUseResp):
            self._icrowd_use_resp = value
        else:
            self._icrowd_use_resp = IcrowdUseResp.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceIcrowdUseResponse, self).parse_response_content(response_content)
        if 'icrowd_use_resp' in response:
            self.icrowd_use_resp = response['icrowd_use_resp']
