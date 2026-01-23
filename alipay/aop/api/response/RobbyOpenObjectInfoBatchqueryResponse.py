#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ObjStatus import ObjStatus


class RobbyOpenObjectInfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(RobbyOpenObjectInfoBatchqueryResponse, self).__init__()
        self._object_status_list = None

    @property
    def object_status_list(self):
        return self._object_status_list

    @object_status_list.setter
    def object_status_list(self, value):
        if isinstance(value, list):
            self._object_status_list = list()
            for i in value:
                if isinstance(i, ObjStatus):
                    self._object_status_list.append(i)
                else:
                    self._object_status_list.append(ObjStatus.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(RobbyOpenObjectInfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'object_status_list' in response:
            self.object_status_list = response['object_status_list']
