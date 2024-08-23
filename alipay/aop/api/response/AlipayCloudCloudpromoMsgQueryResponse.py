#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AichatPushMsgVO import AichatPushMsgVO


class AlipayCloudCloudpromoMsgQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMsgQueryResponse, self).__init__()
        self._aichat_push_msgs = None

    @property
    def aichat_push_msgs(self):
        return self._aichat_push_msgs

    @aichat_push_msgs.setter
    def aichat_push_msgs(self, value):
        if isinstance(value, list):
            self._aichat_push_msgs = list()
            for i in value:
                if isinstance(i, AichatPushMsgVO):
                    self._aichat_push_msgs.append(i)
                else:
                    self._aichat_push_msgs.append(AichatPushMsgVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMsgQueryResponse, self).parse_response_content(response_content)
        if 'aichat_push_msgs' in response:
            self.aichat_push_msgs = response['aichat_push_msgs']
