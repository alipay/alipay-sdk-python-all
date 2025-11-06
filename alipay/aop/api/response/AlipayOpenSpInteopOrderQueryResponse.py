#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InteOpSubOrderInfo import InteOpSubOrderInfo


class AlipayOpenSpInteopOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpInteopOrderQueryResponse, self).__init__()
        self._inteop_order_no = None
        self._inteop_order_status = None
        self._inteop_sub_order_infos = None
        self._wp_qr_code = None
        self._wp_qr_code_img_url = None
        self._wp_web_link = None

    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def inteop_order_status(self):
        return self._inteop_order_status

    @inteop_order_status.setter
    def inteop_order_status(self, value):
        self._inteop_order_status = value
    @property
    def inteop_sub_order_infos(self):
        return self._inteop_sub_order_infos

    @inteop_sub_order_infos.setter
    def inteop_sub_order_infos(self, value):
        if isinstance(value, list):
            self._inteop_sub_order_infos = list()
            for i in value:
                if isinstance(i, InteOpSubOrderInfo):
                    self._inteop_sub_order_infos.append(i)
                else:
                    self._inteop_sub_order_infos.append(InteOpSubOrderInfo.from_alipay_dict(i))
    @property
    def wp_qr_code(self):
        return self._wp_qr_code

    @wp_qr_code.setter
    def wp_qr_code(self, value):
        self._wp_qr_code = value
    @property
    def wp_qr_code_img_url(self):
        return self._wp_qr_code_img_url

    @wp_qr_code_img_url.setter
    def wp_qr_code_img_url(self, value):
        self._wp_qr_code_img_url = value
    @property
    def wp_web_link(self):
        return self._wp_web_link

    @wp_web_link.setter
    def wp_web_link(self, value):
        self._wp_web_link = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpInteopOrderQueryResponse, self).parse_response_content(response_content)
        if 'inteop_order_no' in response:
            self.inteop_order_no = response['inteop_order_no']
        if 'inteop_order_status' in response:
            self.inteop_order_status = response['inteop_order_status']
        if 'inteop_sub_order_infos' in response:
            self.inteop_sub_order_infos = response['inteop_sub_order_infos']
        if 'wp_qr_code' in response:
            self.wp_qr_code = response['wp_qr_code']
        if 'wp_qr_code_img_url' in response:
            self.wp_qr_code_img_url = response['wp_qr_code_img_url']
        if 'wp_web_link' in response:
            self.wp_web_link = response['wp_web_link']
