#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CtuErrorInfo import CtuErrorInfo


class AlipayOpenAligroupProductopenApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAligroupProductopenApplyResponse, self).__init__()
        self._ctu_error_info = None
        self._order_no = None

    @property
    def ctu_error_info(self):
        return self._ctu_error_info

    @ctu_error_info.setter
    def ctu_error_info(self, value):
        if isinstance(value, CtuErrorInfo):
            self._ctu_error_info = value
        else:
            self._ctu_error_info = CtuErrorInfo.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAligroupProductopenApplyResponse, self).parse_response_content(response_content)
        if 'ctu_error_info' in response:
            self.ctu_error_info = response['ctu_error_info']
        if 'order_no' in response:
            self.order_no = response['order_no']
