#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletOpenQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletOpenQueryResponse, self).__init__()
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._open_id = None
        self._out_biz_no = None
        self._status = None
        self._user_id = None
        self._wallet_template_id = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletOpenQueryResponse, self).parse_response_content(response_content)
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'id' in response:
            self.id = response['id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'wallet_template_id' in response:
            self.wallet_template_id = response['wallet_template_id']
