#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InvestorMaterialInfo import InvestorMaterialInfo


class AntfortuneStockQualifiedInvestorApplyResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockQualifiedInvestorApplyResponse, self).__init__()
        self._agreement_no = None
        self._alipay_asset_time = None
        self._alipay_total_asset = None
        self._first_yeb_trade_day = None
        self._has_material = None
        self._material_list = None
        self._total_income = None
        self._trace_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_asset_time(self):
        return self._alipay_asset_time

    @alipay_asset_time.setter
    def alipay_asset_time(self, value):
        self._alipay_asset_time = value
    @property
    def alipay_total_asset(self):
        return self._alipay_total_asset

    @alipay_total_asset.setter
    def alipay_total_asset(self, value):
        self._alipay_total_asset = value
    @property
    def first_yeb_trade_day(self):
        return self._first_yeb_trade_day

    @first_yeb_trade_day.setter
    def first_yeb_trade_day(self, value):
        self._first_yeb_trade_day = value
    @property
    def has_material(self):
        return self._has_material

    @has_material.setter
    def has_material(self, value):
        self._has_material = value
    @property
    def material_list(self):
        return self._material_list

    @material_list.setter
    def material_list(self, value):
        if isinstance(value, list):
            self._material_list = list()
            for i in value:
                if isinstance(i, InvestorMaterialInfo):
                    self._material_list.append(i)
                else:
                    self._material_list.append(InvestorMaterialInfo.from_alipay_dict(i))
    @property
    def total_income(self):
        return self._total_income

    @total_income.setter
    def total_income(self, value):
        self._total_income = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockQualifiedInvestorApplyResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'alipay_asset_time' in response:
            self.alipay_asset_time = response['alipay_asset_time']
        if 'alipay_total_asset' in response:
            self.alipay_total_asset = response['alipay_total_asset']
        if 'first_yeb_trade_day' in response:
            self.first_yeb_trade_day = response['first_yeb_trade_day']
        if 'has_material' in response:
            self.has_material = response['has_material']
        if 'material_list' in response:
            self.material_list = response['material_list']
        if 'total_income' in response:
            self.total_income = response['total_income']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
