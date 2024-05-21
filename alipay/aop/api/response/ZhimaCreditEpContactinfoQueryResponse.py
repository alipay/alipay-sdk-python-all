#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpContactInfo import EpContactInfo


class ZhimaCreditEpContactinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpContactinfoQueryResponse, self).__init__()
        self._data = None
        self._ent_name = None
        self._reg_no = None
        self._uscc = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, EpContactInfo):
            self._data = value
        else:
            self._data = EpContactInfo.from_alipay_dict(value)
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpContactinfoQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'ent_name' in response:
            self.ent_name = response['ent_name']
        if 'reg_no' in response:
            self.reg_no = response['reg_no']
        if 'uscc' in response:
            self.uscc = response['uscc']
