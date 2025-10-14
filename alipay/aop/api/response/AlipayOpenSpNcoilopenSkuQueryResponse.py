#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNcoilopenSkuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNcoilopenSkuQueryResponse, self).__init__()
        self._need_desk_no = None
        self._need_point_name = None
        self._need_qr_code_link = None
        self._sku_id = None
        self._solution_id = None
        self._template_code = None

    @property
    def need_desk_no(self):
        return self._need_desk_no

    @need_desk_no.setter
    def need_desk_no(self, value):
        self._need_desk_no = value
    @property
    def need_point_name(self):
        return self._need_point_name

    @need_point_name.setter
    def need_point_name(self, value):
        self._need_point_name = value
    @property
    def need_qr_code_link(self):
        return self._need_qr_code_link

    @need_qr_code_link.setter
    def need_qr_code_link(self, value):
        self._need_qr_code_link = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNcoilopenSkuQueryResponse, self).parse_response_content(response_content)
        if 'need_desk_no' in response:
            self.need_desk_no = response['need_desk_no']
        if 'need_point_name' in response:
            self.need_point_name = response['need_point_name']
        if 'need_qr_code_link' in response:
            self.need_qr_code_link = response['need_qr_code_link']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
        if 'solution_id' in response:
            self.solution_id = response['solution_id']
        if 'template_code' in response:
            self.template_code = response['template_code']
