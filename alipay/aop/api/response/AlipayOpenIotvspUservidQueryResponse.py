#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IotIdentityOrgUserVidInfoResponse import IotIdentityOrgUserVidInfoResponse


class AlipayOpenIotvspUservidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspUservidQueryResponse, self).__init__()
        self._vid_info_list = None

    @property
    def vid_info_list(self):
        return self._vid_info_list

    @vid_info_list.setter
    def vid_info_list(self, value):
        if isinstance(value, IotIdentityOrgUserVidInfoResponse):
            self._vid_info_list = value
        else:
            self._vid_info_list = IotIdentityOrgUserVidInfoResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspUservidQueryResponse, self).parse_response_content(response_content)
        if 'vid_info_list' in response:
            self.vid_info_list = response['vid_info_list']
