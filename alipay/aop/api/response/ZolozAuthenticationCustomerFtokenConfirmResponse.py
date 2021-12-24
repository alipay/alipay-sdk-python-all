#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FtokenInfoResult import FtokenInfoResult


class ZolozAuthenticationCustomerFtokenConfirmResponse(AlipayResponse):

    def __init__(self):
        super(ZolozAuthenticationCustomerFtokenConfirmResponse, self).__init__()
        self._retcode = None
        self._retmsg = None
        self._uids = None

    @property
    def retcode(self):
        return self._retcode

    @retcode.setter
    def retcode(self, value):
        self._retcode = value
    @property
    def retmsg(self):
        return self._retmsg

    @retmsg.setter
    def retmsg(self, value):
        self._retmsg = value
    @property
    def uids(self):
        return self._uids

    @uids.setter
    def uids(self, value):
        if isinstance(value, list):
            self._uids = list()
            for i in value:
                if isinstance(i, FtokenInfoResult):
                    self._uids.append(i)
                else:
                    self._uids.append(FtokenInfoResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZolozAuthenticationCustomerFtokenConfirmResponse, self).parse_response_content(response_content)
        if 'retcode' in response:
            self.retcode = response['retcode']
        if 'retmsg' in response:
            self.retmsg = response['retmsg']
        if 'uids' in response:
            self.uids = response['uids']
