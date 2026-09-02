#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZmUserDetailModel import ZmUserDetailModel
from alipay.aop.api.domain.ZmUserDetailModel import ZmUserDetailModel
from alipay.aop.api.domain.ZmUserDetailModel import ZmUserDetailModel


class ZhimaCreditPeUserMappingQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserMappingQueryResponse, self).__init__()
        self._credit_agreement_id = None
        self._mapped_score = None
        self._open_id = None
        self._user_cert_no = None
        self._user_id = None
        self._user_name = None
        self._user_phone = None

    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def mapped_score(self):
        return self._mapped_score

    @mapped_score.setter
    def mapped_score(self, value):
        self._mapped_score = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_cert_no(self):
        return self._user_cert_no

    @user_cert_no.setter
    def user_cert_no(self, value):
        if isinstance(value, ZmUserDetailModel):
            self._user_cert_no = value
        else:
            self._user_cert_no = ZmUserDetailModel.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        if isinstance(value, ZmUserDetailModel):
            self._user_name = value
        else:
            self._user_name = ZmUserDetailModel.from_alipay_dict(value)
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        if isinstance(value, ZmUserDetailModel):
            self._user_phone = value
        else:
            self._user_phone = ZmUserDetailModel.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserMappingQueryResponse, self).parse_response_content(response_content)
        if 'credit_agreement_id' in response:
            self.credit_agreement_id = response['credit_agreement_id']
        if 'mapped_score' in response:
            self.mapped_score = response['mapped_score']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'user_cert_no' in response:
            self.user_cert_no = response['user_cert_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'user_name' in response:
            self.user_name = response['user_name']
        if 'user_phone' in response:
            self.user_phone = response['user_phone']
