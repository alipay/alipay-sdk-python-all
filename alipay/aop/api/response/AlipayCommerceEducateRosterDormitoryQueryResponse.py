#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PlaceInfo import PlaceInfo


class AlipayCommerceEducateRosterDormitoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateRosterDormitoryQueryResponse, self).__init__()
        self._candidate_place_list = None
        self._current_out_biz_no = None
        self._current_parent_place_id = None
        self._current_parent_place_name = None
        self._current_place_id = None
        self._current_place_name = None
        self._employee_no = None
        self._name = None
        self._node_name = None

    @property
    def candidate_place_list(self):
        return self._candidate_place_list

    @candidate_place_list.setter
    def candidate_place_list(self, value):
        if isinstance(value, list):
            self._candidate_place_list = list()
            for i in value:
                if isinstance(i, PlaceInfo):
                    self._candidate_place_list.append(i)
                else:
                    self._candidate_place_list.append(PlaceInfo.from_alipay_dict(i))
    @property
    def current_out_biz_no(self):
        return self._current_out_biz_no

    @current_out_biz_no.setter
    def current_out_biz_no(self, value):
        self._current_out_biz_no = value
    @property
    def current_parent_place_id(self):
        return self._current_parent_place_id

    @current_parent_place_id.setter
    def current_parent_place_id(self, value):
        self._current_parent_place_id = value
    @property
    def current_parent_place_name(self):
        return self._current_parent_place_name

    @current_parent_place_name.setter
    def current_parent_place_name(self, value):
        self._current_parent_place_name = value
    @property
    def current_place_id(self):
        return self._current_place_id

    @current_place_id.setter
    def current_place_id(self, value):
        self._current_place_id = value
    @property
    def current_place_name(self):
        return self._current_place_name

    @current_place_name.setter
    def current_place_name(self, value):
        self._current_place_name = value
    @property
    def employee_no(self):
        return self._employee_no

    @employee_no.setter
    def employee_no(self, value):
        self._employee_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateRosterDormitoryQueryResponse, self).parse_response_content(response_content)
        if 'candidate_place_list' in response:
            self.candidate_place_list = response['candidate_place_list']
        if 'current_out_biz_no' in response:
            self.current_out_biz_no = response['current_out_biz_no']
        if 'current_parent_place_id' in response:
            self.current_parent_place_id = response['current_parent_place_id']
        if 'current_parent_place_name' in response:
            self.current_parent_place_name = response['current_parent_place_name']
        if 'current_place_id' in response:
            self.current_place_id = response['current_place_id']
        if 'current_place_name' in response:
            self.current_place_name = response['current_place_name']
        if 'employee_no' in response:
            self.employee_no = response['employee_no']
        if 'name' in response:
            self.name = response['name']
        if 'node_name' in response:
            self.node_name = response['node_name']
