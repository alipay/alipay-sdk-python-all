#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreativePageListRes import CreativePageListRes
from alipay.aop.api.domain.CreativePageListRes import CreativePageListRes
from alipay.aop.api.domain.AdCamPagination import AdCamPagination


class AlipayDataDataserviceAdcampaignCreativeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignCreativeBatchqueryResponse, self).__init__()
        self._content_list = None
        self._list = None
        self._pagination = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                if isinstance(i, CreativePageListRes):
                    self._content_list.append(i)
                else:
                    self._content_list.append(CreativePageListRes.from_alipay_dict(i))
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, CreativePageListRes):
            self._list = value
        else:
            self._list = CreativePageListRes.from_alipay_dict(value)
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
        response = super(AlipayDataDataserviceAdcampaignCreativeBatchqueryResponse, self).parse_response_content(response_content)
        if 'content_list' in response:
            self.content_list = response['content_list']
        if 'list' in response:
            self.list = response['list']
        if 'pagination' in response:
            self.pagination = response['pagination']
