#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsDataDsbEstimateResultDetail import InsDataDsbEstimateResultDetail


class AlipayInsDataDsbEstimateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataDsbEstimateQueryResponse, self).__init__()
        self._confidence = None
        self._estimate_detail_list = None
        self._estimate_no = None
        self._frame_no = None
        self._license_no = None
        self._repair_corp_properties = None
        self._total_damage_amount = None
        self._total_remain_value = None

    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        self._confidence = value
    @property
    def estimate_detail_list(self):
        return self._estimate_detail_list

    @estimate_detail_list.setter
    def estimate_detail_list(self, value):
        if isinstance(value, list):
            self._estimate_detail_list = list()
            for i in value:
                if isinstance(i, InsDataDsbEstimateResultDetail):
                    self._estimate_detail_list.append(i)
                else:
                    self._estimate_detail_list.append(InsDataDsbEstimateResultDetail.from_alipay_dict(i))
    @property
    def estimate_no(self):
        return self._estimate_no

    @estimate_no.setter
    def estimate_no(self, value):
        self._estimate_no = value
    @property
    def frame_no(self):
        return self._frame_no

    @frame_no.setter
    def frame_no(self, value):
        self._frame_no = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def repair_corp_properties(self):
        return self._repair_corp_properties

    @repair_corp_properties.setter
    def repair_corp_properties(self, value):
        self._repair_corp_properties = value
    @property
    def total_damage_amount(self):
        return self._total_damage_amount

    @total_damage_amount.setter
    def total_damage_amount(self, value):
        self._total_damage_amount = value
    @property
    def total_remain_value(self):
        return self._total_remain_value

    @total_remain_value.setter
    def total_remain_value(self, value):
        self._total_remain_value = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataDsbEstimateQueryResponse, self).parse_response_content(response_content)
        if 'confidence' in response:
            self.confidence = response['confidence']
        if 'estimate_detail_list' in response:
            self.estimate_detail_list = response['estimate_detail_list']
        if 'estimate_no' in response:
            self.estimate_no = response['estimate_no']
        if 'frame_no' in response:
            self.frame_no = response['frame_no']
        if 'license_no' in response:
            self.license_no = response['license_no']
        if 'repair_corp_properties' in response:
            self.repair_corp_properties = response['repair_corp_properties']
        if 'total_damage_amount' in response:
            self.total_damage_amount = response['total_damage_amount']
        if 'total_remain_value' in response:
            self.total_remain_value = response['total_remain_value']
