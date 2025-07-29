#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupMsgAutoreplyDetailVO import GroupMsgAutoreplyDetailVO


class AlipayMerchantGroupAutoreplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupAutoreplyQueryResponse, self).__init__()
        self._group_msg_autoreply_detail = None

    @property
    def group_msg_autoreply_detail(self):
        return self._group_msg_autoreply_detail

    @group_msg_autoreply_detail.setter
    def group_msg_autoreply_detail(self, value):
        if isinstance(value, GroupMsgAutoreplyDetailVO):
            self._group_msg_autoreply_detail = value
        else:
            self._group_msg_autoreply_detail = GroupMsgAutoreplyDetailVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupAutoreplyQueryResponse, self).parse_response_content(response_content)
        if 'group_msg_autoreply_detail' in response:
            self.group_msg_autoreply_detail = response['group_msg_autoreply_detail']
