#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IpAddrLbsInfo import IpAddrLbsInfo


class AlipaySecurityDataInfoIpaddrinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataInfoIpaddrinfoQueryResponse, self).__init__()
        self._ip_addr_lbs_info = None

    @property
    def ip_addr_lbs_info(self):
        return self._ip_addr_lbs_info

    @ip_addr_lbs_info.setter
    def ip_addr_lbs_info(self, value):
        if isinstance(value, IpAddrLbsInfo):
            self._ip_addr_lbs_info = value
        else:
            self._ip_addr_lbs_info = IpAddrLbsInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataInfoIpaddrinfoQueryResponse, self).parse_response_content(response_content)
        if 'ip_addr_lbs_info' in response:
            self.ip_addr_lbs_info = response['ip_addr_lbs_info']
