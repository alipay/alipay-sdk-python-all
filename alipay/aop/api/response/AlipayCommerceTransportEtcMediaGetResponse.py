#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MediaContentList import MediaContentList


class AlipayCommerceTransportEtcMediaGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcMediaGetResponse, self).__init__()
        self._content_list = None
        self._order_id = None
        self._out_biz_no = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                if isinstance(i, MediaContentList):
                    self._content_list.append(i)
                else:
                    self._content_list.append(MediaContentList.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcMediaGetResponse, self).parse_response_content(response_content)
        if 'content_list' in response:
            self.content_list = response['content_list']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
