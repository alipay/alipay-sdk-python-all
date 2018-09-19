#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingVoucherConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherConfirmResponse, self).__init__()
        self._need_redirect = None
        self._out_biz_no = None
        self._redirect_uri = None
        self._send_code = None
        self._template_id = None
        self._theme = None
        self._user_id = None

    @property
    def need_redirect(self):
        return self._need_redirect

    @need_redirect.setter
    def need_redirect(self, value):
        self._need_redirect = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def redirect_uri(self):
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, value):
        self._redirect_uri = value
    @property
    def send_code(self):
        return self._send_code

    @send_code.setter
    def send_code(self, value):
        self._send_code = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, value):
        self._theme = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherConfirmResponse, self).parse_response_content(response_content)
        if 'need_redirect' in response:
            self.need_redirect = response['need_redirect']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'redirect_uri' in response:
            self.redirect_uri = response['redirect_uri']
        if 'send_code' in response:
            self.send_code = response['send_code']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'theme' in response:
            self.theme = response['theme']
        if 'user_id' in response:
            self.user_id = response['user_id']
