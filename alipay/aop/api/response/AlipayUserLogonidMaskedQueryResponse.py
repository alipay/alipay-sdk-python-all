#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MaskedLogonIdView import MaskedLogonIdView


class AlipayUserLogonidMaskedQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserLogonidMaskedQueryResponse, self).__init__()
        self._logon_id_views = None

    @property
    def logon_id_views(self):
        return self._logon_id_views

    @logon_id_views.setter
    def logon_id_views(self, value):
        if isinstance(value, list):
            self._logon_id_views = list()
            for i in value:
                if isinstance(i, MaskedLogonIdView):
                    self._logon_id_views.append(i)
                else:
                    self._logon_id_views.append(MaskedLogonIdView.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserLogonidMaskedQueryResponse, self).parse_response_content(response_content)
        if 'logon_id_views' in response:
            self.logon_id_views = response['logon_id_views']
