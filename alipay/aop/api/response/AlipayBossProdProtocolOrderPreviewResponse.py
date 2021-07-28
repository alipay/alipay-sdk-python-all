#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProtocolPreviewVO import ProtocolPreviewVO


class AlipayBossProdProtocolOrderPreviewResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdProtocolOrderPreviewResponse, self).__init__()
        self._protocol_preview_vo_list = None

    @property
    def protocol_preview_vo_list(self):
        return self._protocol_preview_vo_list

    @protocol_preview_vo_list.setter
    def protocol_preview_vo_list(self, value):
        if isinstance(value, ProtocolPreviewVO):
            self._protocol_preview_vo_list = value
        else:
            self._protocol_preview_vo_list = ProtocolPreviewVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdProtocolOrderPreviewResponse, self).parse_response_content(response_content)
        if 'protocol_preview_vo_list' in response:
            self.protocol_preview_vo_list = response['protocol_preview_vo_list']
