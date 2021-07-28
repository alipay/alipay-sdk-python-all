#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiQualityTestShieldOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiQualityTestShieldOrderCreateResponse, self).__init__()
        self._batch_no = None
        self._ext_infos = None
        self._order_id = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiQualityTestShieldOrderCreateResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'ext_infos' in response:
            self.ext_infos = response['ext_infos']
        if 'order_id' in response:
            self.order_id = response['order_id']
