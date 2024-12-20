#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarUnionmemberAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarUnionmemberAccountQueryResponse, self).__init__()
        self._benefit_ids = None
        self._biz_card_no = None
        self._open_date = None
        self._out_biz_id = None
        self._out_user_id = None
        self._status = None
        self._valid_date = None

    @property
    def benefit_ids(self):
        return self._benefit_ids

    @benefit_ids.setter
    def benefit_ids(self, value):
        if isinstance(value, list):
            self._benefit_ids = list()
            for i in value:
                self._benefit_ids.append(i)
    @property
    def biz_card_no(self):
        return self._biz_card_no

    @biz_card_no.setter
    def biz_card_no(self, value):
        self._biz_card_no = value
    @property
    def open_date(self):
        return self._open_date

    @open_date.setter
    def open_date(self, value):
        self._open_date = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def valid_date(self):
        return self._valid_date

    @valid_date.setter
    def valid_date(self, value):
        self._valid_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarUnionmemberAccountQueryResponse, self).parse_response_content(response_content)
        if 'benefit_ids' in response:
            self.benefit_ids = response['benefit_ids']
        if 'biz_card_no' in response:
            self.biz_card_no = response['biz_card_no']
        if 'open_date' in response:
            self.open_date = response['open_date']
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
        if 'out_user_id' in response:
            self.out_user_id = response['out_user_id']
        if 'status' in response:
            self.status = response['status']
        if 'valid_date' in response:
            self.valid_date = response['valid_date']
