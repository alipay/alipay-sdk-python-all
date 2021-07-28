#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LibraryInfo import LibraryInfo


class AlipayIserviceCcmSwLibraryBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwLibraryBatchqueryResponse, self).__init__()
        self._libraries = None

    @property
    def libraries(self):
        return self._libraries

    @libraries.setter
    def libraries(self, value):
        if isinstance(value, list):
            self._libraries = list()
            for i in value:
                if isinstance(i, LibraryInfo):
                    self._libraries.append(i)
                else:
                    self._libraries.append(LibraryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwLibraryBatchqueryResponse, self).parse_response_content(response_content)
        if 'libraries' in response:
            self.libraries = response['libraries']
