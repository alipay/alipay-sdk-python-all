#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupPageListRes import GroupPageListRes
from alipay.aop.api.domain.AdCamPagination import AdCamPagination


class AlipayDataDataserviceAdcampaignGroupBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignGroupBatchqueryResponse, self).__init__()
        self._list = None
        self._pagination = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, GroupPageListRes):
                    self._list.append(i)
                else:
                    self._list.append(GroupPageListRes.from_alipay_dict(i))
    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, value):
        if isinstance(value, AdCamPagination):
            self._pagination = value
        else:
            self._pagination = AdCamPagination.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignGroupBatchqueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']
        if 'pagination' in response:
            self.pagination = response['pagination']
