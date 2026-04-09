#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementDelegationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementDelegationQueryResponse, self).__init__()
        self._agreement_no = None
        self._delegation_id = None
        self._delegation_tag = None
        self._external_delegation_id = None
        self._max_total_amount = None
        self._remaining_amount = None
        self._remaining_times = None
        self._status = None
        self._times_limit = None
        self._validity_end_time = None
        self._validity_start_time = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def delegation_id(self):
        return self._delegation_id

    @delegation_id.setter
    def delegation_id(self, value):
        self._delegation_id = value
    @property
    def delegation_tag(self):
        return self._delegation_tag

    @delegation_tag.setter
    def delegation_tag(self, value):
        self._delegation_tag = value
    @property
    def external_delegation_id(self):
        return self._external_delegation_id

    @external_delegation_id.setter
    def external_delegation_id(self, value):
        self._external_delegation_id = value
    @property
    def max_total_amount(self):
        return self._max_total_amount

    @max_total_amount.setter
    def max_total_amount(self, value):
        self._max_total_amount = value
    @property
    def remaining_amount(self):
        return self._remaining_amount

    @remaining_amount.setter
    def remaining_amount(self, value):
        self._remaining_amount = value
    @property
    def remaining_times(self):
        return self._remaining_times

    @remaining_times.setter
    def remaining_times(self, value):
        self._remaining_times = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def times_limit(self):
        return self._times_limit

    @times_limit.setter
    def times_limit(self, value):
        self._times_limit = value
    @property
    def validity_end_time(self):
        return self._validity_end_time

    @validity_end_time.setter
    def validity_end_time(self, value):
        self._validity_end_time = value
    @property
    def validity_start_time(self):
        return self._validity_start_time

    @validity_start_time.setter
    def validity_start_time(self, value):
        self._validity_start_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementDelegationQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'delegation_id' in response:
            self.delegation_id = response['delegation_id']
        if 'delegation_tag' in response:
            self.delegation_tag = response['delegation_tag']
        if 'external_delegation_id' in response:
            self.external_delegation_id = response['external_delegation_id']
        if 'max_total_amount' in response:
            self.max_total_amount = response['max_total_amount']
        if 'remaining_amount' in response:
            self.remaining_amount = response['remaining_amount']
        if 'remaining_times' in response:
            self.remaining_times = response['remaining_times']
        if 'status' in response:
            self.status = response['status']
        if 'times_limit' in response:
            self.times_limit = response['times_limit']
        if 'validity_end_time' in response:
            self.validity_end_time = response['validity_end_time']
        if 'validity_start_time' in response:
            self.validity_start_time = response['validity_start_time']
