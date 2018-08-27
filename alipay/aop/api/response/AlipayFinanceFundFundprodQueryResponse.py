#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinanceFundFundprodQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinanceFundFundprodQueryResponse, self).__init__()
        self._establishment_date = None
        self._fund_code = None
        self._fund_name = None
        self._fund_name_abbr = None
        self._net_value = None
        self._net_value_date = None
        self._profit_seven_days = None
        self._profit_ten_thousand = None
        self._risk_evaluation = None

    @property
    def establishment_date(self):
        return self._establishment_date

    @establishment_date.setter
    def establishment_date(self, value):
        self._establishment_date = value
    @property
    def fund_code(self):
        return self._fund_code

    @fund_code.setter
    def fund_code(self, value):
        self._fund_code = value
    @property
    def fund_name(self):
        return self._fund_name

    @fund_name.setter
    def fund_name(self, value):
        self._fund_name = value
    @property
    def fund_name_abbr(self):
        return self._fund_name_abbr

    @fund_name_abbr.setter
    def fund_name_abbr(self, value):
        self._fund_name_abbr = value
    @property
    def net_value(self):
        return self._net_value

    @net_value.setter
    def net_value(self, value):
        self._net_value = value
    @property
    def net_value_date(self):
        return self._net_value_date

    @net_value_date.setter
    def net_value_date(self, value):
        self._net_value_date = value
    @property
    def profit_seven_days(self):
        return self._profit_seven_days

    @profit_seven_days.setter
    def profit_seven_days(self, value):
        self._profit_seven_days = value
    @property
    def profit_ten_thousand(self):
        return self._profit_ten_thousand

    @profit_ten_thousand.setter
    def profit_ten_thousand(self, value):
        self._profit_ten_thousand = value
    @property
    def risk_evaluation(self):
        return self._risk_evaluation

    @risk_evaluation.setter
    def risk_evaluation(self, value):
        self._risk_evaluation = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinanceFundFundprodQueryResponse, self).parse_response_content(response_content)
        if 'establishment_date' in response:
            self.establishment_date = response['establishment_date']
        if 'fund_code' in response:
            self.fund_code = response['fund_code']
        if 'fund_name' in response:
            self.fund_name = response['fund_name']
        if 'fund_name_abbr' in response:
            self.fund_name_abbr = response['fund_name_abbr']
        if 'net_value' in response:
            self.net_value = response['net_value']
        if 'net_value_date' in response:
            self.net_value_date = response['net_value_date']
        if 'profit_seven_days' in response:
            self.profit_seven_days = response['profit_seven_days']
        if 'profit_ten_thousand' in response:
            self.profit_ten_thousand = response['profit_ten_thousand']
        if 'risk_evaluation' in response:
            self.risk_evaluation = response['risk_evaluation']
