#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CommunityPartnerRelaData import CommunityPartnerRelaData


class AlipayOpenAppCommunityPartnerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppCommunityPartnerQueryResponse, self).__init__()
        self._count = None
        self._data_list = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, CommunityPartnerRelaData):
                    self._data_list.append(i)
                else:
                    self._data_list.append(CommunityPartnerRelaData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppCommunityPartnerQueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'data_list' in response:
            self.data_list = response['data_list']
