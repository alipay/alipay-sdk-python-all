#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppProdmodeTasknodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppProdmodeTasknodeQueryResponse, self).__init__()
        self._gmt_modified = None
        self._is_edit_all = None
        self._is_edit_fund = None
        self._node_code = None
        self._node_name = None
        self._reject = None
        self._reject_time = None

    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def is_edit_all(self):
        return self._is_edit_all

    @is_edit_all.setter
    def is_edit_all(self, value):
        self._is_edit_all = value
    @property
    def is_edit_fund(self):
        return self._is_edit_fund

    @is_edit_fund.setter
    def is_edit_fund(self, value):
        self._is_edit_fund = value
    @property
    def node_code(self):
        return self._node_code

    @node_code.setter
    def node_code(self, value):
        self._node_code = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value
    @property
    def reject(self):
        return self._reject

    @reject.setter
    def reject(self, value):
        self._reject = value
    @property
    def reject_time(self):
        return self._reject_time

    @reject_time.setter
    def reject_time(self, value):
        self._reject_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppProdmodeTasknodeQueryResponse, self).parse_response_content(response_content)
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'is_edit_all' in response:
            self.is_edit_all = response['is_edit_all']
        if 'is_edit_fund' in response:
            self.is_edit_fund = response['is_edit_fund']
        if 'node_code' in response:
            self.node_code = response['node_code']
        if 'node_name' in response:
            self.node_name = response['node_name']
        if 'reject' in response:
            self.reject = response['reject']
        if 'reject_time' in response:
            self.reject_time = response['reject_time']
