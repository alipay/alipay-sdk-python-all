#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PublicBindAccount import PublicBindAccount


class AlipayMobilePublicAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicAccountQueryResponse, self).__init__()
        self._code = None
        self._menu_key = None
        self._msg = None
        self._public_bind_accounts = None
        self._remark = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def menu_key(self):
        return self._menu_key

    @menu_key.setter
    def menu_key(self, value):
        self._menu_key = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def public_bind_accounts(self):
        return self._public_bind_accounts

    @public_bind_accounts.setter
    def public_bind_accounts(self, value):
        if isinstance(value, list):
            self._public_bind_accounts = list()
            for i in value:
                if isinstance(i, PublicBindAccount):
                    self._public_bind_accounts.append(i)
                else:
                    self._public_bind_accounts.append(PublicBindAccount.from_alipay_dict(i))
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicAccountQueryResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'menu_key' in response:
            self.menu_key = response['menu_key']
        if 'msg' in response:
            self.msg = response['msg']
        if 'public_bind_accounts' in response:
            self.public_bind_accounts = response['public_bind_accounts']
        if 'remark' in response:
            self.remark = response['remark']
