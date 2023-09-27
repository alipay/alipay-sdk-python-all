#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseQuotacontrolRuleGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseQuotacontrolRuleGetResponse, self).__init__()
        self._fee_item_code = None
        self._fee_item_name = None
        self._package_quota = None
        self._rule_id = None
        self._threshold = None
        self._unit_name = None

    @property
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def fee_item_name(self):
        return self._fee_item_name

    @fee_item_name.setter
    def fee_item_name(self, value):
        self._fee_item_name = value
    @property
    def package_quota(self):
        return self._package_quota

    @package_quota.setter
    def package_quota(self, value):
        self._package_quota = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value
    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseQuotacontrolRuleGetResponse, self).parse_response_content(response_content)
        if 'fee_item_code' in response:
            self.fee_item_code = response['fee_item_code']
        if 'fee_item_name' in response:
            self.fee_item_name = response['fee_item_name']
        if 'package_quota' in response:
            self.package_quota = response['package_quota']
        if 'rule_id' in response:
            self.rule_id = response['rule_id']
        if 'threshold' in response:
            self.threshold = response['threshold']
        if 'unit_name' in response:
            self.unit_name = response['unit_name']
