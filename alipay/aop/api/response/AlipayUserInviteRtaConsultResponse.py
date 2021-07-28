#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RtaInfo import RtaInfo


class AlipayUserInviteRtaConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInviteRtaConsultResponse, self).__init__()
        self._principal_label = None
        self._required_flow = None
        self._rta_info_list = None

    @property
    def principal_label(self):
        return self._principal_label

    @principal_label.setter
    def principal_label(self, value):
        self._principal_label = value
    @property
    def required_flow(self):
        return self._required_flow

    @required_flow.setter
    def required_flow(self, value):
        self._required_flow = value
    @property
    def rta_info_list(self):
        return self._rta_info_list

    @rta_info_list.setter
    def rta_info_list(self, value):
        if isinstance(value, list):
            self._rta_info_list = list()
            for i in value:
                if isinstance(i, RtaInfo):
                    self._rta_info_list.append(i)
                else:
                    self._rta_info_list.append(RtaInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserInviteRtaConsultResponse, self).parse_response_content(response_content)
        if 'principal_label' in response:
            self.principal_label = response['principal_label']
        if 'required_flow' in response:
            self.required_flow = response['required_flow']
        if 'rta_info_list' in response:
            self.rta_info_list = response['rta_info_list']
