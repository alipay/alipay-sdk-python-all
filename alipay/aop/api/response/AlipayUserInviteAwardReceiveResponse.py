#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserInviteAwardReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInviteAwardReceiveResponse, self).__init__()
        self._alipay_account_no = None
        self._biz_result_code = None
        self._biz_result_desc = None
        self._ext_info = None
        self._mobile = None
        self._user_attr = None

    @property
    def alipay_account_no(self):
        return self._alipay_account_no

    @alipay_account_no.setter
    def alipay_account_no(self, value):
        self._alipay_account_no = value
    @property
    def biz_result_code(self):
        return self._biz_result_code

    @biz_result_code.setter
    def biz_result_code(self, value):
        self._biz_result_code = value
    @property
    def biz_result_desc(self):
        return self._biz_result_desc

    @biz_result_desc.setter
    def biz_result_desc(self, value):
        self._biz_result_desc = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def user_attr(self):
        return self._user_attr

    @user_attr.setter
    def user_attr(self, value):
        self._user_attr = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserInviteAwardReceiveResponse, self).parse_response_content(response_content)
        if 'alipay_account_no' in response:
            self.alipay_account_no = response['alipay_account_no']
        if 'biz_result_code' in response:
            self.biz_result_code = response['biz_result_code']
        if 'biz_result_desc' in response:
            self.biz_result_desc = response['biz_result_desc']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'mobile' in response:
            self.mobile = response['mobile']
        if 'user_attr' in response:
            self.user_attr = response['user_attr']
