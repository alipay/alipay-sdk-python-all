#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntfarmUserOrnament import AntfarmUserOrnament


class AlipaySocialAntfarmUserornamentsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntfarmUserornamentsQueryResponse, self).__init__()
        self._user_ornament_list = None

    @property
    def user_ornament_list(self):
        return self._user_ornament_list

    @user_ornament_list.setter
    def user_ornament_list(self, value):
        if isinstance(value, list):
            self._user_ornament_list = list()
            for i in value:
                if isinstance(i, AntfarmUserOrnament):
                    self._user_ornament_list.append(i)
                else:
                    self._user_ornament_list.append(AntfarmUserOrnament.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntfarmUserornamentsQueryResponse, self).parse_response_content(response_content)
        if 'user_ornament_list' in response:
            self.user_ornament_list = response['user_ornament_list']
