#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NbConversation import NbConversation
from alipay.aop.api.domain.NbPagination import NbPagination


class AlipayCloudNextbuilderAgentConversationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudNextbuilderAgentConversationQueryResponse, self).__init__()
        self._data = None
        self._pagination = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, NbConversation):
                    self._data.append(i)
                else:
                    self._data.append(NbConversation.from_alipay_dict(i))
    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, value):
        if isinstance(value, NbPagination):
            self._pagination = value
        else:
            self._pagination = NbPagination.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudNextbuilderAgentConversationQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'pagination' in response:
            self.pagination = response['pagination']
