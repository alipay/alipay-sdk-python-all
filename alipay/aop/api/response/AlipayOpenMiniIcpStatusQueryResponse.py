#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniIcpStatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIcpStatusQueryResponse, self).__init__()
        self._icp_result_desc = None
        self._icp_status = None

    @property
    def icp_result_desc(self):
        return self._icp_result_desc

    @icp_result_desc.setter
    def icp_result_desc(self, value):
        self._icp_result_desc = value
    @property
    def icp_status(self):
        return self._icp_status

    @icp_status.setter
    def icp_status(self, value):
        self._icp_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIcpStatusQueryResponse, self).parse_response_content(response_content)
        if 'icp_result_desc' in response:
            self.icp_result_desc = response['icp_result_desc']
        if 'icp_status' in response:
            self.icp_status = response['icp_status']
