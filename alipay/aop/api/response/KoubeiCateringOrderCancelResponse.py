#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefundDescriptionDTO import RefundDescriptionDTO


class KoubeiCateringOrderCancelResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringOrderCancelResponse, self).__init__()
        self._ext_info = None
        self._order_id = None
        self._out_biz_no = None
        self._refund_description_list = None
        self._retry = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    @property
    def refund_description_list(self):
        return self._refund_description_list

    @refund_description_list.setter
    def refund_description_list(self, value):
        if isinstance(value, list):
            self._refund_description_list = list()
            for i in value:
                if isinstance(i, RefundDescriptionDTO):
                    self._refund_description_list.append(i)
                else:
                    self._refund_description_list.append(RefundDescriptionDTO.from_alipay_dict(i))
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringOrderCancelResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'refund_description_list' in response:
            self.refund_description_list = response['refund_description_list']
        if 'retry' in response:
            self.retry = response['retry']
