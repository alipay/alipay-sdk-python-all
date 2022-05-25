#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundFlexiblestaffingAuthorizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingAuthorizeQueryResponse, self).__init__()
        self._authorize_time = None
        self._authorized_party_name = None
        self._biz_scene = None
        self._out_biz_no = None
        self._principal_id = None
        self._product_code = None
        self._status = None

    @property
    def authorize_time(self):
        return self._authorize_time

    @authorize_time.setter
    def authorize_time(self, value):
        self._authorize_time = value
    @property
    def authorized_party_name(self):
        return self._authorized_party_name

    @authorized_party_name.setter
    def authorized_party_name(self, value):
        self._authorized_party_name = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingAuthorizeQueryResponse, self).parse_response_content(response_content)
        if 'authorize_time' in response:
            self.authorize_time = response['authorize_time']
        if 'authorized_party_name' in response:
            self.authorized_party_name = response['authorized_party_name']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'principal_id' in response:
            self.principal_id = response['principal_id']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'status' in response:
            self.status = response['status']
