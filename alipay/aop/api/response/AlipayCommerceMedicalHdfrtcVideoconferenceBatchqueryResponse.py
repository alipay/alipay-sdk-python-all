#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberEnterInfo import MemberEnterInfo


class AlipayCommerceMedicalHdfrtcVideoconferenceBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcVideoconferenceBatchqueryResponse, self).__init__()
        self._member_enter_infos = None

    @property
    def member_enter_infos(self):
        return self._member_enter_infos

    @member_enter_infos.setter
    def member_enter_infos(self, value):
        if isinstance(value, list):
            self._member_enter_infos = list()
            for i in value:
                if isinstance(i, MemberEnterInfo):
                    self._member_enter_infos.append(i)
                else:
                    self._member_enter_infos.append(MemberEnterInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcVideoconferenceBatchqueryResponse, self).parse_response_content(response_content)
        if 'member_enter_infos' in response:
            self.member_enter_infos = response['member_enter_infos']
