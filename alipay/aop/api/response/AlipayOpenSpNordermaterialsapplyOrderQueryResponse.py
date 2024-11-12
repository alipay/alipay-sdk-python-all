#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordermaterialsapplyOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyOrderQueryResponse, self).__init__()
        self._apply_status = None
        self._apply_status_code = None
        self._materials_num = None
        self._refuse_reason = None
        self._shop_num = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apply_status_code(self):
        return self._apply_status_code

    @apply_status_code.setter
    def apply_status_code(self, value):
        self._apply_status_code = value
    @property
    def materials_num(self):
        return self._materials_num

    @materials_num.setter
    def materials_num(self, value):
        self._materials_num = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def shop_num(self):
        return self._shop_num

    @shop_num.setter
    def shop_num(self, value):
        self._shop_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyOrderQueryResponse, self).parse_response_content(response_content)
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
        if 'apply_status_code' in response:
            self.apply_status_code = response['apply_status_code']
        if 'materials_num' in response:
            self.materials_num = response['materials_num']
        if 'refuse_reason' in response:
            self.refuse_reason = response['refuse_reason']
        if 'shop_num' in response:
            self.shop_num = response['shop_num']
