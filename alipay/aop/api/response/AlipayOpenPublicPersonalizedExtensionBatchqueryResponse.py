#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryExtension import QueryExtension


class AlipayOpenPublicPersonalizedExtensionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicPersonalizedExtensionBatchqueryResponse, self).__init__()
        self._count = None
        self._extensions = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def extensions(self):
        return self._extensions

    @extensions.setter
    def extensions(self, value):
        if isinstance(value, list):
            self._extensions = list()
            for i in value:
                if isinstance(i, QueryExtension):
                    self._extensions.append(i)
                else:
                    self._extensions.append(QueryExtension.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicPersonalizedExtensionBatchqueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'extensions' in response:
            self.extensions = response['extensions']
