#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IgAuthQuota import IgAuthQuota


class KoubeiServindustryPromoGuidequotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryPromoGuidequotaQueryResponse, self).__init__()
        self._auth_quota = None

    @property
    def auth_quota(self):
        return self._auth_quota

    @auth_quota.setter
    def auth_quota(self, value):
        if isinstance(value, list):
            self._auth_quota = list()
            for i in value:
                if isinstance(i, IgAuthQuota):
                    self._auth_quota.append(i)
                else:
                    self._auth_quota.append(IgAuthQuota.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryPromoGuidequotaQueryResponse, self).parse_response_content(response_content)
        if 'auth_quota' in response:
            self.auth_quota = response['auth_quota']
