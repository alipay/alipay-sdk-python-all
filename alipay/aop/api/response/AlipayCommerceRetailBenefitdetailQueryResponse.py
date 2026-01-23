#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailBenefitdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailBenefitdetailQueryResponse, self).__init__()
        self._activity_id = None
        self._activity_name = None
        self._activity_rule = None
        self._activity_rule_desc = None
        self._activity_scope_list = None
        self._activity_source = None
        self._activity_type = None
        self._brand_image = None
        self._brand_logo_image = None
        self._brand_name = None
        self._en_info = None
        self._end_time = None
        self._operator = None
        self._priority = None
        self._prize_infos = None
        self._start_time = None
        self._status = None
        self._verify_tester = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_rule(self):
        return self._activity_rule

    @activity_rule.setter
    def activity_rule(self, value):
        self._activity_rule = value
    @property
    def activity_rule_desc(self):
        return self._activity_rule_desc

    @activity_rule_desc.setter
    def activity_rule_desc(self, value):
        self._activity_rule_desc = value
    @property
    def activity_scope_list(self):
        return self._activity_scope_list

    @activity_scope_list.setter
    def activity_scope_list(self, value):
        if isinstance(value, list):
            self._activity_scope_list = list()
            for i in value:
                self._activity_scope_list.append(i)
    @property
    def activity_source(self):
        return self._activity_source

    @activity_source.setter
    def activity_source(self, value):
        self._activity_source = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def brand_image(self):
        return self._brand_image

    @brand_image.setter
    def brand_image(self, value):
        self._brand_image = value
    @property
    def brand_logo_image(self):
        return self._brand_logo_image

    @brand_logo_image.setter
    def brand_logo_image(self, value):
        self._brand_logo_image = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def en_info(self):
        return self._en_info

    @en_info.setter
    def en_info(self, value):
        self._en_info = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def prize_infos(self):
        return self._prize_infos

    @prize_infos.setter
    def prize_infos(self, value):
        if isinstance(value, list):
            self._prize_infos = list()
            for i in value:
                self._prize_infos.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def verify_tester(self):
        return self._verify_tester

    @verify_tester.setter
    def verify_tester(self, value):
        if isinstance(value, list):
            self._verify_tester = list()
            for i in value:
                self._verify_tester.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailBenefitdetailQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'activity_rule' in response:
            self.activity_rule = response['activity_rule']
        if 'activity_rule_desc' in response:
            self.activity_rule_desc = response['activity_rule_desc']
        if 'activity_scope_list' in response:
            self.activity_scope_list = response['activity_scope_list']
        if 'activity_source' in response:
            self.activity_source = response['activity_source']
        if 'activity_type' in response:
            self.activity_type = response['activity_type']
        if 'brand_image' in response:
            self.brand_image = response['brand_image']
        if 'brand_logo_image' in response:
            self.brand_logo_image = response['brand_logo_image']
        if 'brand_name' in response:
            self.brand_name = response['brand_name']
        if 'en_info' in response:
            self.en_info = response['en_info']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'operator' in response:
            self.operator = response['operator']
        if 'priority' in response:
            self.priority = response['priority']
        if 'prize_infos' in response:
            self.prize_infos = response['prize_infos']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
        if 'verify_tester' in response:
            self.verify_tester = response['verify_tester']
