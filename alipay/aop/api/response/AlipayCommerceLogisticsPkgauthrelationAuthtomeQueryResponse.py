#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PkgAuthRelation import PkgAuthRelation


class AlipayCommerceLogisticsPkgauthrelationAuthtomeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsPkgauthrelationAuthtomeQueryResponse, self).__init__()
        self._pkg_auth_relations = None

    @property
    def pkg_auth_relations(self):
        return self._pkg_auth_relations

    @pkg_auth_relations.setter
    def pkg_auth_relations(self, value):
        if isinstance(value, list):
            self._pkg_auth_relations = list()
            for i in value:
                if isinstance(i, PkgAuthRelation):
                    self._pkg_auth_relations.append(i)
                else:
                    self._pkg_auth_relations.append(PkgAuthRelation.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsPkgauthrelationAuthtomeQueryResponse, self).parse_response_content(response_content)
        if 'pkg_auth_relations' in response:
            self.pkg_auth_relations = response['pkg_auth_relations']
