#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo


class AlipayCommerceDataQrCodeApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceDataQrCodeApplyResponse, self).__init__()
        self._biz_type = None
        self._dynamic_img_url = None
        self._dynamic_img_url_and_trans = None
        self._ext_info = None
        self._isv_pid = None
        self._outer_biz_id = None
        self._page_url = None
        self._qr_code_url = None
        self._shop_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def dynamic_img_url(self):
        return self._dynamic_img_url

    @dynamic_img_url.setter
    def dynamic_img_url(self, value):
        self._dynamic_img_url = value
    @property
    def dynamic_img_url_and_trans(self):
        return self._dynamic_img_url_and_trans

    @dynamic_img_url_and_trans.setter
    def dynamic_img_url_and_trans(self, value):
        self._dynamic_img_url_and_trans = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ScenicExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ScenicExtInfo.from_alipay_dict(i))
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def outer_biz_id(self):
        return self._outer_biz_id

    @outer_biz_id.setter
    def outer_biz_id(self, value):
        self._outer_biz_id = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceDataQrCodeApplyResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'dynamic_img_url' in response:
            self.dynamic_img_url = response['dynamic_img_url']
        if 'dynamic_img_url_and_trans' in response:
            self.dynamic_img_url_and_trans = response['dynamic_img_url_and_trans']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'isv_pid' in response:
            self.isv_pid = response['isv_pid']
        if 'outer_biz_id' in response:
            self.outer_biz_id = response['outer_biz_id']
        if 'page_url' in response:
            self.page_url = response['page_url']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
