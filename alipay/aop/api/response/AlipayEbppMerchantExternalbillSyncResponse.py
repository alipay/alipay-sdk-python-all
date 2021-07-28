#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppMerchantExternalbillSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppMerchantExternalbillSyncResponse, self).__init__()
        self._alipay_bill_id = None
        self._out_biz_no = None
        self._status = None

    @property
    def alipay_bill_id(self):
        return self._alipay_bill_id

    @alipay_bill_id.setter
    def alipay_bill_id(self, value):
        self._alipay_bill_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppMerchantExternalbillSyncResponse, self).parse_response_content(response_content)
        if 'alipay_bill_id' in response:
            self.alipay_bill_id = response['alipay_bill_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
