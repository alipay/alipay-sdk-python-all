#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceFundBindCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceFundBindCreateResponse, self).__init__()
        self._idempotent = None
        self._out_bind_no = None
        self._schema = None

    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value
    @property
    def out_bind_no(self):
        return self._out_bind_no

    @out_bind_no.setter
    def out_bind_no(self, value):
        self._out_bind_no = value
    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value):
        self._schema = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceFundBindCreateResponse, self).parse_response_content(response_content)
        if 'idempotent' in response:
            self.idempotent = response['idempotent']
        if 'out_bind_no' in response:
            self.out_bind_no = response['out_bind_no']
        if 'schema' in response:
            self.schema = response['schema']
