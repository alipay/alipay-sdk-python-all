#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasEnterprisecertifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasEnterprisecertifyQueryResponse, self).__init__()
        self._certify_end_time = None
        self._certify_order_no = None
        self._credit_code = None
        self._enterprise_name = None
        self._legal_representative_id_no_postfix = None
        self._legal_representative_name = None
        self._out_request_no = None
        self._status = None
        self._status_desc = None

    @property
    def certify_end_time(self):
        return self._certify_end_time

    @certify_end_time.setter
    def certify_end_time(self, value):
        self._certify_end_time = value
    @property
    def certify_order_no(self):
        return self._certify_order_no

    @certify_order_no.setter
    def certify_order_no(self, value):
        self._certify_order_no = value
    @property
    def credit_code(self):
        return self._credit_code

    @credit_code.setter
    def credit_code(self, value):
        self._credit_code = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def legal_representative_id_no_postfix(self):
        return self._legal_representative_id_no_postfix

    @legal_representative_id_no_postfix.setter
    def legal_representative_id_no_postfix(self, value):
        self._legal_representative_id_no_postfix = value
    @property
    def legal_representative_name(self):
        return self._legal_representative_name

    @legal_representative_name.setter
    def legal_representative_name(self, value):
        self._legal_representative_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasEnterprisecertifyQueryResponse, self).parse_response_content(response_content)
        if 'certify_end_time' in response:
            self.certify_end_time = response['certify_end_time']
        if 'certify_order_no' in response:
            self.certify_order_no = response['certify_order_no']
        if 'credit_code' in response:
            self.credit_code = response['credit_code']
        if 'enterprise_name' in response:
            self.enterprise_name = response['enterprise_name']
        if 'legal_representative_id_no_postfix' in response:
            self.legal_representative_id_no_postfix = response['legal_representative_id_no_postfix']
        if 'legal_representative_name' in response:
            self.legal_representative_name = response['legal_representative_name']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'status' in response:
            self.status = response['status']
        if 'status_desc' in response:
            self.status_desc = response['status_desc']
