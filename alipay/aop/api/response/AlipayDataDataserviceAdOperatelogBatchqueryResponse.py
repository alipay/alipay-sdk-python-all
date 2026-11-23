#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OperateLogDetailResponse import OperateLogDetailResponse
from alipay.aop.api.domain.PageResInfo import PageResInfo


class AlipayDataDataserviceAdOperatelogBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdOperatelogBatchqueryResponse, self).__init__()
        self._list = None
        self._pagination = None

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, OperateLogDetailResponse):
            self._list = value
        else:
            self._list = OperateLogDetailResponse.from_alipay_dict(value)
    @property
    def pagination(self):
        return self._pagination

    @pagination.setter
    def pagination(self, value):
        if isinstance(value, PageResInfo):
            self._pagination = value
        else:
            self._pagination = PageResInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdOperatelogBatchqueryResponse, self).parse_response_content(response_content)
        if 'list' in response:
            self.list = response['list']
        if 'pagination' in response:
            self.pagination = response['pagination']
