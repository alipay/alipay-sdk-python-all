#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubRentRiskResult import SubRentRiskResult
from alipay.aop.api.domain.SubRentRiskItem import SubRentRiskItem


class AlipayCloudTraasCloudriskRentriskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudTraasCloudriskRentriskQueryResponse, self).__init__()
        self._record_id = None
        self._risk_desc = None
        self._risk_name = None
        self._risk_rank = None
        self._sub_rent_risk_result = None
        self._sub_risk_result_list = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def risk_desc(self):
        return self._risk_desc

    @risk_desc.setter
    def risk_desc(self, value):
        self._risk_desc = value
    @property
    def risk_name(self):
        return self._risk_name

    @risk_name.setter
    def risk_name(self, value):
        self._risk_name = value
    @property
    def risk_rank(self):
        return self._risk_rank

    @risk_rank.setter
    def risk_rank(self, value):
        self._risk_rank = value
    @property
    def sub_rent_risk_result(self):
        return self._sub_rent_risk_result

    @sub_rent_risk_result.setter
    def sub_rent_risk_result(self, value):
        if isinstance(value, SubRentRiskResult):
            self._sub_rent_risk_result = value
        else:
            self._sub_rent_risk_result = SubRentRiskResult.from_alipay_dict(value)
    @property
    def sub_risk_result_list(self):
        return self._sub_risk_result_list

    @sub_risk_result_list.setter
    def sub_risk_result_list(self, value):
        if isinstance(value, list):
            self._sub_risk_result_list = list()
            for i in value:
                if isinstance(i, SubRentRiskItem):
                    self._sub_risk_result_list.append(i)
                else:
                    self._sub_risk_result_list.append(SubRentRiskItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudTraasCloudriskRentriskQueryResponse, self).parse_response_content(response_content)
        if 'record_id' in response:
            self.record_id = response['record_id']
        if 'risk_desc' in response:
            self.risk_desc = response['risk_desc']
        if 'risk_name' in response:
            self.risk_name = response['risk_name']
        if 'risk_rank' in response:
            self.risk_rank = response['risk_rank']
        if 'sub_rent_risk_result' in response:
            self.sub_rent_risk_result = response['sub_rent_risk_result']
        if 'sub_risk_result_list' in response:
            self.sub_risk_result_list = response['sub_risk_result_list']
