#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupDetail import GroupDetail


class AlipaySocialBaseBcGroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseBcGroupQueryResponse, self).__init__()
        self._group_detail = None

    @property
    def group_detail(self):
        return self._group_detail

    @group_detail.setter
    def group_detail(self, value):
        if isinstance(value, GroupDetail):
            self._group_detail = value
        else:
            self._group_detail = GroupDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseBcGroupQueryResponse, self).parse_response_content(response_content)
        if 'group_detail' in response:
            self.group_detail = response['group_detail']
