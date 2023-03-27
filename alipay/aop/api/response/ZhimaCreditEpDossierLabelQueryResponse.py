#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EpLabelContent import EpLabelContent


class ZhimaCreditEpDossierLabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierLabelQueryResponse, self).__init__()
        self._ep_cert_no = None
        self._has_authed = None
        self._label_content = None

    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def has_authed(self):
        return self._has_authed

    @has_authed.setter
    def has_authed(self, value):
        self._has_authed = value
    @property
    def label_content(self):
        return self._label_content

    @label_content.setter
    def label_content(self, value):
        if isinstance(value, list):
            self._label_content = list()
            for i in value:
                if isinstance(i, EpLabelContent):
                    self._label_content.append(i)
                else:
                    self._label_content.append(EpLabelContent.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierLabelQueryResponse, self).parse_response_content(response_content)
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'has_authed' in response:
            self.has_authed = response['has_authed']
        if 'label_content' in response:
            self.label_content = response['label_content']
