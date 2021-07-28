#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoBizoptCloseResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoBizoptCloseResponse, self).__init__()
        self._biz_opt_no = None
        self._out_request_no = None
        self._partner_id = None
        self._user_id = None

    @property
    def biz_opt_no(self):
        return self._biz_opt_no

    @biz_opt_no.setter
    def biz_opt_no(self, value):
        self._biz_opt_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoBizoptCloseResponse, self).parse_response_content(response_content)
        if 'biz_opt_no' in response:
            self.biz_opt_no = response['biz_opt_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
