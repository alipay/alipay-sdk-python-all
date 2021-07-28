#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoPaysignApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoPaysignApplyResponse, self).__init__()
        self._agreement_id = None
        self._biz_type = None
        self._idempotent = None
        self._zmgo_opt_no = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value
    @property
    def zmgo_opt_no(self):
        return self._zmgo_opt_no

    @zmgo_opt_no.setter
    def zmgo_opt_no(self, value):
        self._zmgo_opt_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoPaysignApplyResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'idempotent' in response:
            self.idempotent = response['idempotent']
        if 'zmgo_opt_no' in response:
            self.zmgo_opt_no = response['zmgo_opt_no']
