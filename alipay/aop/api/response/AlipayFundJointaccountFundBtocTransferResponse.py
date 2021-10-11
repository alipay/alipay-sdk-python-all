#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountFundBtocTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountFundBtocTransferResponse, self).__init__()
        self._biz_trans_id = None
        self._out_biz_no = None
        self._status = None
        self._trans_date = None

    @property
    def biz_trans_id(self):
        return self._biz_trans_id

    @biz_trans_id.setter
    def biz_trans_id(self, value):
        self._biz_trans_id = value
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
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountFundBtocTransferResponse, self).parse_response_content(response_content)
        if 'biz_trans_id' in response:
            self.biz_trans_id = response['biz_trans_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'status' in response:
            self.status = response['status']
        if 'trans_date' in response:
            self.trans_date = response['trans_date']
