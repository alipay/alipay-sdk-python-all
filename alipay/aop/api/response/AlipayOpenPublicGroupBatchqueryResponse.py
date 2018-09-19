#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryGroup import QueryGroup


class AlipayOpenPublicGroupBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicGroupBatchqueryResponse, self).__init__()
        self._groups = None

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, value):
        if isinstance(value, list):
            self._groups = list()
            for i in value:
                if isinstance(i, QueryGroup):
                    self._groups.append(i)
                else:
                    self._groups.append(QueryGroup.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicGroupBatchqueryResponse, self).parse_response_content(response_content)
        if 'groups' in response:
            self.groups = response['groups']
