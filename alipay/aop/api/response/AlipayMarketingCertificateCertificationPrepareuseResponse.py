#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertificatePrepareInfo import CertificatePrepareInfo


class AlipayMarketingCertificateCertificationPrepareuseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCertificateCertificationPrepareuseResponse, self).__init__()
        self._certificate_prepare_info_list = None
        self._open_id = None
        self._order_id = None
        self._user_id = None

    @property
    def certificate_prepare_info_list(self):
        return self._certificate_prepare_info_list

    @certificate_prepare_info_list.setter
    def certificate_prepare_info_list(self, value):
        if isinstance(value, list):
            self._certificate_prepare_info_list = list()
            for i in value:
                if isinstance(i, CertificatePrepareInfo):
                    self._certificate_prepare_info_list.append(i)
                else:
                    self._certificate_prepare_info_list.append(CertificatePrepareInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCertificateCertificationPrepareuseResponse, self).parse_response_content(response_content)
        if 'certificate_prepare_info_list' in response:
            self.certificate_prepare_info_list = response['certificate_prepare_info_list']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'user_id' in response:
            self.user_id = response['user_id']
