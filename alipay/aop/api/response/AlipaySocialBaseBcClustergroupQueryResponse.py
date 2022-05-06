#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupBrief import GroupBrief


class AlipaySocialBaseBcClustergroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseBcClustergroupQueryResponse, self).__init__()
        self._group_briefs = None

    @property
    def group_briefs(self):
        return self._group_briefs

    @group_briefs.setter
    def group_briefs(self, value):
        if isinstance(value, list):
            self._group_briefs = list()
            for i in value:
                if isinstance(i, GroupBrief):
                    self._group_briefs.append(i)
                else:
                    self._group_briefs.append(GroupBrief.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseBcClustergroupQueryResponse, self).parse_response_content(response_content)
        if 'group_briefs' in response:
            self.group_briefs = response['group_briefs']
