#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CircularAgreementRelation import CircularAgreementRelation


class AlipayCircularAgreementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCircularAgreementQueryResponse, self).__init__()
        self._relations = None
        self._total = None

    @property
    def relations(self):
        return self._relations

    @relations.setter
    def relations(self, value):
        if isinstance(value, CircularAgreementRelation):
            self._relations = value
        else:
            self._relations = CircularAgreementRelation.from_alipay_dict(value)
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCircularAgreementQueryResponse, self).parse_response_content(response_content)
        if 'relations' in response:
            self.relations = response['relations']
        if 'total' in response:
            self.total = response['total']
