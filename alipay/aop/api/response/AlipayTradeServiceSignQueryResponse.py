#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgreementTextInfo import AgreementTextInfo


class AlipayTradeServiceSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeServiceSignQueryResponse, self).__init__()
        self._agreement_text_infos = None
        self._sign_result = None
        self._sub_biz_type = None

    @property
    def agreement_text_infos(self):
        return self._agreement_text_infos

    @agreement_text_infos.setter
    def agreement_text_infos(self, value):
        if isinstance(value, list):
            self._agreement_text_infos = list()
            for i in value:
                if isinstance(i, AgreementTextInfo):
                    self._agreement_text_infos.append(i)
                else:
                    self._agreement_text_infos.append(AgreementTextInfo.from_alipay_dict(i))
    @property
    def sign_result(self):
        return self._sign_result

    @sign_result.setter
    def sign_result(self, value):
        self._sign_result = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeServiceSignQueryResponse, self).parse_response_content(response_content)
        if 'agreement_text_infos' in response:
            self.agreement_text_infos = response['agreement_text_infos']
        if 'sign_result' in response:
            self.sign_result = response['sign_result']
        if 'sub_biz_type' in response:
            self.sub_biz_type = response['sub_biz_type']
