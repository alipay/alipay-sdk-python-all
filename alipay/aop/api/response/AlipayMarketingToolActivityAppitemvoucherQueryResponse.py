#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppItemActivityQueryBaseInfo import AppItemActivityQueryBaseInfo
from alipay.aop.api.domain.AppItemVoucherQueryBudgetSupplyInfo import AppItemVoucherQueryBudgetSupplyInfo
from alipay.aop.api.domain.AppItemVoucherQueryCustomerGuideInfo import AppItemVoucherQueryCustomerGuideInfo
from alipay.aop.api.domain.AppItemVoucherQueryDeductInfo import AppItemVoucherQueryDeductInfo
from alipay.aop.api.domain.AppItemVoucherQueryDisplayPatternInfo import AppItemVoucherQueryDisplayPatternInfo
from alipay.aop.api.domain.AppItemVoucherQuerySendModeInfo import AppItemVoucherQuerySendModeInfo
from alipay.aop.api.domain.AppItemVoucherQueryUseRuleInfo import AppItemVoucherQueryUseRuleInfo


class AlipayMarketingToolActivityAppitemvoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolActivityAppitemvoucherQueryResponse, self).__init__()
        self._app_item_activity_base_info = None
        self._app_item_voucher_budget_supply_info = None
        self._app_item_voucher_customer_guide_info = None
        self._app_item_voucher_deduct_info = None
        self._app_item_voucher_display_pattern_info = None
        self._app_item_voucher_send_mode_info = None
        self._app_item_voucher_use_rule_info = None

    @property
    def app_item_activity_base_info(self):
        return self._app_item_activity_base_info

    @app_item_activity_base_info.setter
    def app_item_activity_base_info(self, value):
        if isinstance(value, AppItemActivityQueryBaseInfo):
            self._app_item_activity_base_info = value
        else:
            self._app_item_activity_base_info = AppItemActivityQueryBaseInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_budget_supply_info(self):
        return self._app_item_voucher_budget_supply_info

    @app_item_voucher_budget_supply_info.setter
    def app_item_voucher_budget_supply_info(self, value):
        if isinstance(value, AppItemVoucherQueryBudgetSupplyInfo):
            self._app_item_voucher_budget_supply_info = value
        else:
            self._app_item_voucher_budget_supply_info = AppItemVoucherQueryBudgetSupplyInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_customer_guide_info(self):
        return self._app_item_voucher_customer_guide_info

    @app_item_voucher_customer_guide_info.setter
    def app_item_voucher_customer_guide_info(self, value):
        if isinstance(value, AppItemVoucherQueryCustomerGuideInfo):
            self._app_item_voucher_customer_guide_info = value
        else:
            self._app_item_voucher_customer_guide_info = AppItemVoucherQueryCustomerGuideInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_deduct_info(self):
        return self._app_item_voucher_deduct_info

    @app_item_voucher_deduct_info.setter
    def app_item_voucher_deduct_info(self, value):
        if isinstance(value, AppItemVoucherQueryDeductInfo):
            self._app_item_voucher_deduct_info = value
        else:
            self._app_item_voucher_deduct_info = AppItemVoucherQueryDeductInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_display_pattern_info(self):
        return self._app_item_voucher_display_pattern_info

    @app_item_voucher_display_pattern_info.setter
    def app_item_voucher_display_pattern_info(self, value):
        if isinstance(value, AppItemVoucherQueryDisplayPatternInfo):
            self._app_item_voucher_display_pattern_info = value
        else:
            self._app_item_voucher_display_pattern_info = AppItemVoucherQueryDisplayPatternInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_send_mode_info(self):
        return self._app_item_voucher_send_mode_info

    @app_item_voucher_send_mode_info.setter
    def app_item_voucher_send_mode_info(self, value):
        if isinstance(value, AppItemVoucherQuerySendModeInfo):
            self._app_item_voucher_send_mode_info = value
        else:
            self._app_item_voucher_send_mode_info = AppItemVoucherQuerySendModeInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_use_rule_info(self):
        return self._app_item_voucher_use_rule_info

    @app_item_voucher_use_rule_info.setter
    def app_item_voucher_use_rule_info(self, value):
        if isinstance(value, AppItemVoucherQueryUseRuleInfo):
            self._app_item_voucher_use_rule_info = value
        else:
            self._app_item_voucher_use_rule_info = AppItemVoucherQueryUseRuleInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolActivityAppitemvoucherQueryResponse, self).parse_response_content(response_content)
        if 'app_item_activity_base_info' in response:
            self.app_item_activity_base_info = response['app_item_activity_base_info']
        if 'app_item_voucher_budget_supply_info' in response:
            self.app_item_voucher_budget_supply_info = response['app_item_voucher_budget_supply_info']
        if 'app_item_voucher_customer_guide_info' in response:
            self.app_item_voucher_customer_guide_info = response['app_item_voucher_customer_guide_info']
        if 'app_item_voucher_deduct_info' in response:
            self.app_item_voucher_deduct_info = response['app_item_voucher_deduct_info']
        if 'app_item_voucher_display_pattern_info' in response:
            self.app_item_voucher_display_pattern_info = response['app_item_voucher_display_pattern_info']
        if 'app_item_voucher_send_mode_info' in response:
            self.app_item_voucher_send_mode_info = response['app_item_voucher_send_mode_info']
        if 'app_item_voucher_use_rule_info' in response:
            self.app_item_voucher_use_rule_info = response['app_item_voucher_use_rule_info']
