#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PortfolioDetailProductInfo import PortfolioDetailProductInfo


class AntfortuneEquityPortfolioQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneEquityPortfolioQueryResponse, self).__init__()
        self._can_purchase = None
        self._can_sell = None
        self._established_date = None
        self._last_day_profit_rate = None
        self._latest_one_year_profit_rate = None
        self._min_purchase_amount = None
        self._portfolio_code = None
        self._portfolio_detail_products = None
        self._portfolio_name = None
        self._portfolio_tag_list = None
        self._portfolio_type = None
        self._product_id = None
        self._profit_period_key = None
        self._profit_rate = None
        self._risk_evaluation = None
        self._sp_code = None
        self._sp_id = None
        self._sp_intro = None
        self._sp_logo = None
        self._sp_name = None
        self._sp_type = None
        self._strategy_goal = None
        self._strategy_intro = None
        self._strategy_url = None
        self._suggested_keep_period = None

    @property
    def can_purchase(self):
        return self._can_purchase

    @can_purchase.setter
    def can_purchase(self, value):
        self._can_purchase = value
    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def established_date(self):
        return self._established_date

    @established_date.setter
    def established_date(self, value):
        self._established_date = value
    @property
    def last_day_profit_rate(self):
        return self._last_day_profit_rate

    @last_day_profit_rate.setter
    def last_day_profit_rate(self, value):
        self._last_day_profit_rate = value
    @property
    def latest_one_year_profit_rate(self):
        return self._latest_one_year_profit_rate

    @latest_one_year_profit_rate.setter
    def latest_one_year_profit_rate(self, value):
        self._latest_one_year_profit_rate = value
    @property
    def min_purchase_amount(self):
        return self._min_purchase_amount

    @min_purchase_amount.setter
    def min_purchase_amount(self, value):
        self._min_purchase_amount = value
    @property
    def portfolio_code(self):
        return self._portfolio_code

    @portfolio_code.setter
    def portfolio_code(self, value):
        self._portfolio_code = value
    @property
    def portfolio_detail_products(self):
        return self._portfolio_detail_products

    @portfolio_detail_products.setter
    def portfolio_detail_products(self, value):
        if isinstance(value, list):
            self._portfolio_detail_products = list()
            for i in value:
                if isinstance(i, PortfolioDetailProductInfo):
                    self._portfolio_detail_products.append(i)
                else:
                    self._portfolio_detail_products.append(PortfolioDetailProductInfo.from_alipay_dict(i))
    @property
    def portfolio_name(self):
        return self._portfolio_name

    @portfolio_name.setter
    def portfolio_name(self, value):
        self._portfolio_name = value
    @property
    def portfolio_tag_list(self):
        return self._portfolio_tag_list

    @portfolio_tag_list.setter
    def portfolio_tag_list(self, value):
        if isinstance(value, list):
            self._portfolio_tag_list = list()
            for i in value:
                self._portfolio_tag_list.append(i)
    @property
    def portfolio_type(self):
        return self._portfolio_type

    @portfolio_type.setter
    def portfolio_type(self, value):
        self._portfolio_type = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def profit_period_key(self):
        return self._profit_period_key

    @profit_period_key.setter
    def profit_period_key(self, value):
        self._profit_period_key = value
    @property
    def profit_rate(self):
        return self._profit_rate

    @profit_rate.setter
    def profit_rate(self, value):
        self._profit_rate = value
    @property
    def risk_evaluation(self):
        return self._risk_evaluation

    @risk_evaluation.setter
    def risk_evaluation(self, value):
        self._risk_evaluation = value
    @property
    def sp_code(self):
        return self._sp_code

    @sp_code.setter
    def sp_code(self, value):
        self._sp_code = value
    @property
    def sp_id(self):
        return self._sp_id

    @sp_id.setter
    def sp_id(self, value):
        self._sp_id = value
    @property
    def sp_intro(self):
        return self._sp_intro

    @sp_intro.setter
    def sp_intro(self, value):
        self._sp_intro = value
    @property
    def sp_logo(self):
        return self._sp_logo

    @sp_logo.setter
    def sp_logo(self, value):
        self._sp_logo = value
    @property
    def sp_name(self):
        return self._sp_name

    @sp_name.setter
    def sp_name(self, value):
        self._sp_name = value
    @property
    def sp_type(self):
        return self._sp_type

    @sp_type.setter
    def sp_type(self, value):
        self._sp_type = value
    @property
    def strategy_goal(self):
        return self._strategy_goal

    @strategy_goal.setter
    def strategy_goal(self, value):
        self._strategy_goal = value
    @property
    def strategy_intro(self):
        return self._strategy_intro

    @strategy_intro.setter
    def strategy_intro(self, value):
        self._strategy_intro = value
    @property
    def strategy_url(self):
        return self._strategy_url

    @strategy_url.setter
    def strategy_url(self, value):
        self._strategy_url = value
    @property
    def suggested_keep_period(self):
        return self._suggested_keep_period

    @suggested_keep_period.setter
    def suggested_keep_period(self, value):
        self._suggested_keep_period = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneEquityPortfolioQueryResponse, self).parse_response_content(response_content)
        if 'can_purchase' in response:
            self.can_purchase = response['can_purchase']
        if 'can_sell' in response:
            self.can_sell = response['can_sell']
        if 'established_date' in response:
            self.established_date = response['established_date']
        if 'last_day_profit_rate' in response:
            self.last_day_profit_rate = response['last_day_profit_rate']
        if 'latest_one_year_profit_rate' in response:
            self.latest_one_year_profit_rate = response['latest_one_year_profit_rate']
        if 'min_purchase_amount' in response:
            self.min_purchase_amount = response['min_purchase_amount']
        if 'portfolio_code' in response:
            self.portfolio_code = response['portfolio_code']
        if 'portfolio_detail_products' in response:
            self.portfolio_detail_products = response['portfolio_detail_products']
        if 'portfolio_name' in response:
            self.portfolio_name = response['portfolio_name']
        if 'portfolio_tag_list' in response:
            self.portfolio_tag_list = response['portfolio_tag_list']
        if 'portfolio_type' in response:
            self.portfolio_type = response['portfolio_type']
        if 'product_id' in response:
            self.product_id = response['product_id']
        if 'profit_period_key' in response:
            self.profit_period_key = response['profit_period_key']
        if 'profit_rate' in response:
            self.profit_rate = response['profit_rate']
        if 'risk_evaluation' in response:
            self.risk_evaluation = response['risk_evaluation']
        if 'sp_code' in response:
            self.sp_code = response['sp_code']
        if 'sp_id' in response:
            self.sp_id = response['sp_id']
        if 'sp_intro' in response:
            self.sp_intro = response['sp_intro']
        if 'sp_logo' in response:
            self.sp_logo = response['sp_logo']
        if 'sp_name' in response:
            self.sp_name = response['sp_name']
        if 'sp_type' in response:
            self.sp_type = response['sp_type']
        if 'strategy_goal' in response:
            self.strategy_goal = response['strategy_goal']
        if 'strategy_intro' in response:
            self.strategy_intro = response['strategy_intro']
        if 'strategy_url' in response:
            self.strategy_url = response['strategy_url']
        if 'suggested_keep_period' in response:
            self.suggested_keep_period = response['suggested_keep_period']
