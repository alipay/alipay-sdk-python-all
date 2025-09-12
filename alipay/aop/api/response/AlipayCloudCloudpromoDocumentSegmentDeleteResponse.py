#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoDocumentSegmentDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoDocumentSegmentDeleteResponse, self).__init__()
        self._delete_num = None

    @property
    def delete_num(self):
        return self._delete_num

    @delete_num.setter
    def delete_num(self, value):
        self._delete_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoDocumentSegmentDeleteResponse, self).parse_response_content(response_content)
        if 'delete_num' in response:
            self.delete_num = response['delete_num']
