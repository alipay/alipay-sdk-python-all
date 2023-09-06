#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RareNameInfo import RareNameInfo


class AlipayUserCertifyRarenameAssociateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyRarenameAssociateResponse, self).__init__()
        self._rare_name_infos = None

    @property
    def rare_name_infos(self):
        return self._rare_name_infos

    @rare_name_infos.setter
    def rare_name_infos(self, value):
        if isinstance(value, RareNameInfo):
            self._rare_name_infos = value
        else:
            self._rare_name_infos = RareNameInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyRarenameAssociateResponse, self).parse_response_content(response_content)
        if 'rare_name_infos' in response:
            self.rare_name_infos = response['rare_name_infos']
