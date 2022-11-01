#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayPaysharingprodSharepeerpayApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayPaysharingprodSharepeerpayApplyResponse, self).__init__()
        self._friend_share_page_url = None
        self._peerpay_order_no = None
        self._qrcode = None
        self._qrcode_image = None
        self._ztoken = None

    @property
    def friend_share_page_url(self):
        return self._friend_share_page_url

    @friend_share_page_url.setter
    def friend_share_page_url(self, value):
        self._friend_share_page_url = value
    @property
    def peerpay_order_no(self):
        return self._peerpay_order_no

    @peerpay_order_no.setter
    def peerpay_order_no(self, value):
        self._peerpay_order_no = value
    @property
    def qrcode(self):
        return self._qrcode

    @qrcode.setter
    def qrcode(self, value):
        self._qrcode = value
    @property
    def qrcode_image(self):
        return self._qrcode_image

    @qrcode_image.setter
    def qrcode_image(self, value):
        self._qrcode_image = value
    @property
    def ztoken(self):
        return self._ztoken

    @ztoken.setter
    def ztoken(self, value):
        self._ztoken = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayPaysharingprodSharepeerpayApplyResponse, self).parse_response_content(response_content)
        if 'friend_share_page_url' in response:
            self.friend_share_page_url = response['friend_share_page_url']
        if 'peerpay_order_no' in response:
            self.peerpay_order_no = response['peerpay_order_no']
        if 'qrcode' in response:
            self.qrcode = response['qrcode']
        if 'qrcode_image' in response:
            self.qrcode_image = response['qrcode_image']
        if 'ztoken' in response:
            self.ztoken = response['ztoken']
