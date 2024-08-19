#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemActivityBaseInfo import AppItemActivityBaseInfo
from alipay.aop.api.domain.AppItemVoucherAvailableScopeInfo import AppItemVoucherAvailableScopeInfo
from alipay.aop.api.domain.AppItemVoucherBudgetSupplyInfo import AppItemVoucherBudgetSupplyInfo
from alipay.aop.api.domain.AppItemVoucherCustomerGuideInfo import AppItemVoucherCustomerGuideInfo
from alipay.aop.api.domain.AppItemVoucherDeductInfo import AppItemVoucherDeductInfo
from alipay.aop.api.domain.AppItemVoucherDisplayPatternInfo import AppItemVoucherDisplayPatternInfo
from alipay.aop.api.domain.AppItemVoucherSendModeInfo import AppItemVoucherSendModeInfo
from alipay.aop.api.domain.AppItemVoucherUseRuleInfo import AppItemVoucherUseRuleInfo


class AlipayMarketingToolActivityAppitemvoucherCreateModel(object):

    def __init__(self):
        self._app_item_activity_base_info = None
        self._app_item_voucher_available_scope_info = None
        self._app_item_voucher_budget_supply_info = None
        self._app_item_voucher_customer_guide_info = None
        self._app_item_voucher_deduct_info = None
        self._app_item_voucher_display_pattern_info = None
        self._app_item_voucher_send_mode_info = None
        self._app_item_voucher_use_rule_info = None
        self._out_biz_no = None

    @property
    def app_item_activity_base_info(self):
        return self._app_item_activity_base_info

    @app_item_activity_base_info.setter
    def app_item_activity_base_info(self, value):
        if isinstance(value, AppItemActivityBaseInfo):
            self._app_item_activity_base_info = value
        else:
            self._app_item_activity_base_info = AppItemActivityBaseInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_available_scope_info(self):
        return self._app_item_voucher_available_scope_info

    @app_item_voucher_available_scope_info.setter
    def app_item_voucher_available_scope_info(self, value):
        if isinstance(value, AppItemVoucherAvailableScopeInfo):
            self._app_item_voucher_available_scope_info = value
        else:
            self._app_item_voucher_available_scope_info = AppItemVoucherAvailableScopeInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_budget_supply_info(self):
        return self._app_item_voucher_budget_supply_info

    @app_item_voucher_budget_supply_info.setter
    def app_item_voucher_budget_supply_info(self, value):
        if isinstance(value, AppItemVoucherBudgetSupplyInfo):
            self._app_item_voucher_budget_supply_info = value
        else:
            self._app_item_voucher_budget_supply_info = AppItemVoucherBudgetSupplyInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_customer_guide_info(self):
        return self._app_item_voucher_customer_guide_info

    @app_item_voucher_customer_guide_info.setter
    def app_item_voucher_customer_guide_info(self, value):
        if isinstance(value, AppItemVoucherCustomerGuideInfo):
            self._app_item_voucher_customer_guide_info = value
        else:
            self._app_item_voucher_customer_guide_info = AppItemVoucherCustomerGuideInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_deduct_info(self):
        return self._app_item_voucher_deduct_info

    @app_item_voucher_deduct_info.setter
    def app_item_voucher_deduct_info(self, value):
        if isinstance(value, AppItemVoucherDeductInfo):
            self._app_item_voucher_deduct_info = value
        else:
            self._app_item_voucher_deduct_info = AppItemVoucherDeductInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_display_pattern_info(self):
        return self._app_item_voucher_display_pattern_info

    @app_item_voucher_display_pattern_info.setter
    def app_item_voucher_display_pattern_info(self, value):
        if isinstance(value, AppItemVoucherDisplayPatternInfo):
            self._app_item_voucher_display_pattern_info = value
        else:
            self._app_item_voucher_display_pattern_info = AppItemVoucherDisplayPatternInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_send_mode_info(self):
        return self._app_item_voucher_send_mode_info

    @app_item_voucher_send_mode_info.setter
    def app_item_voucher_send_mode_info(self, value):
        if isinstance(value, AppItemVoucherSendModeInfo):
            self._app_item_voucher_send_mode_info = value
        else:
            self._app_item_voucher_send_mode_info = AppItemVoucherSendModeInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_use_rule_info(self):
        return self._app_item_voucher_use_rule_info

    @app_item_voucher_use_rule_info.setter
    def app_item_voucher_use_rule_info(self, value):
        if isinstance(value, AppItemVoucherUseRuleInfo):
            self._app_item_voucher_use_rule_info = value
        else:
            self._app_item_voucher_use_rule_info = AppItemVoucherUseRuleInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_activity_base_info:
            if hasattr(self.app_item_activity_base_info, 'to_alipay_dict'):
                params['app_item_activity_base_info'] = self.app_item_activity_base_info.to_alipay_dict()
            else:
                params['app_item_activity_base_info'] = self.app_item_activity_base_info
        if self.app_item_voucher_available_scope_info:
            if hasattr(self.app_item_voucher_available_scope_info, 'to_alipay_dict'):
                params['app_item_voucher_available_scope_info'] = self.app_item_voucher_available_scope_info.to_alipay_dict()
            else:
                params['app_item_voucher_available_scope_info'] = self.app_item_voucher_available_scope_info
        if self.app_item_voucher_budget_supply_info:
            if hasattr(self.app_item_voucher_budget_supply_info, 'to_alipay_dict'):
                params['app_item_voucher_budget_supply_info'] = self.app_item_voucher_budget_supply_info.to_alipay_dict()
            else:
                params['app_item_voucher_budget_supply_info'] = self.app_item_voucher_budget_supply_info
        if self.app_item_voucher_customer_guide_info:
            if hasattr(self.app_item_voucher_customer_guide_info, 'to_alipay_dict'):
                params['app_item_voucher_customer_guide_info'] = self.app_item_voucher_customer_guide_info.to_alipay_dict()
            else:
                params['app_item_voucher_customer_guide_info'] = self.app_item_voucher_customer_guide_info
        if self.app_item_voucher_deduct_info:
            if hasattr(self.app_item_voucher_deduct_info, 'to_alipay_dict'):
                params['app_item_voucher_deduct_info'] = self.app_item_voucher_deduct_info.to_alipay_dict()
            else:
                params['app_item_voucher_deduct_info'] = self.app_item_voucher_deduct_info
        if self.app_item_voucher_display_pattern_info:
            if hasattr(self.app_item_voucher_display_pattern_info, 'to_alipay_dict'):
                params['app_item_voucher_display_pattern_info'] = self.app_item_voucher_display_pattern_info.to_alipay_dict()
            else:
                params['app_item_voucher_display_pattern_info'] = self.app_item_voucher_display_pattern_info
        if self.app_item_voucher_send_mode_info:
            if hasattr(self.app_item_voucher_send_mode_info, 'to_alipay_dict'):
                params['app_item_voucher_send_mode_info'] = self.app_item_voucher_send_mode_info.to_alipay_dict()
            else:
                params['app_item_voucher_send_mode_info'] = self.app_item_voucher_send_mode_info
        if self.app_item_voucher_use_rule_info:
            if hasattr(self.app_item_voucher_use_rule_info, 'to_alipay_dict'):
                params['app_item_voucher_use_rule_info'] = self.app_item_voucher_use_rule_info.to_alipay_dict()
            else:
                params['app_item_voucher_use_rule_info'] = self.app_item_voucher_use_rule_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolActivityAppitemvoucherCreateModel()
        if 'app_item_activity_base_info' in d:
            o.app_item_activity_base_info = d['app_item_activity_base_info']
        if 'app_item_voucher_available_scope_info' in d:
            o.app_item_voucher_available_scope_info = d['app_item_voucher_available_scope_info']
        if 'app_item_voucher_budget_supply_info' in d:
            o.app_item_voucher_budget_supply_info = d['app_item_voucher_budget_supply_info']
        if 'app_item_voucher_customer_guide_info' in d:
            o.app_item_voucher_customer_guide_info = d['app_item_voucher_customer_guide_info']
        if 'app_item_voucher_deduct_info' in d:
            o.app_item_voucher_deduct_info = d['app_item_voucher_deduct_info']
        if 'app_item_voucher_display_pattern_info' in d:
            o.app_item_voucher_display_pattern_info = d['app_item_voucher_display_pattern_info']
        if 'app_item_voucher_send_mode_info' in d:
            o.app_item_voucher_send_mode_info = d['app_item_voucher_send_mode_info']
        if 'app_item_voucher_use_rule_info' in d:
            o.app_item_voucher_use_rule_info = d['app_item_voucher_use_rule_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


