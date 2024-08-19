#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemActivityModifyBaseInfo import AppItemActivityModifyBaseInfo
from alipay.aop.api.domain.AppItemVoucherModifyAvailableScopeInfo import AppItemVoucherModifyAvailableScopeInfo
from alipay.aop.api.domain.AppItemVoucherModifyDisplayPatternInfo import AppItemVoucherModifyDisplayPatternInfo
from alipay.aop.api.domain.AppItemVoucherModifySendModeInfo import AppItemVoucherModifySendModeInfo
from alipay.aop.api.domain.AppItemVoucherModifyUseRuleInfo import AppItemVoucherModifyUseRuleInfo


class AlipayMarketingToolActivityAppitemvoucherModifyModel(object):

    def __init__(self):
        self._app_item_activity_base_info = None
        self._app_item_voucher_available_scope_info = None
        self._app_item_voucher_display_pattern_info = None
        self._app_item_voucher_send_mode_info = None
        self._app_item_voucher_use_rule_info = None
        self._out_biz_no = None

    @property
    def app_item_activity_base_info(self):
        return self._app_item_activity_base_info

    @app_item_activity_base_info.setter
    def app_item_activity_base_info(self, value):
        if isinstance(value, AppItemActivityModifyBaseInfo):
            self._app_item_activity_base_info = value
        else:
            self._app_item_activity_base_info = AppItemActivityModifyBaseInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_available_scope_info(self):
        return self._app_item_voucher_available_scope_info

    @app_item_voucher_available_scope_info.setter
    def app_item_voucher_available_scope_info(self, value):
        if isinstance(value, AppItemVoucherModifyAvailableScopeInfo):
            self._app_item_voucher_available_scope_info = value
        else:
            self._app_item_voucher_available_scope_info = AppItemVoucherModifyAvailableScopeInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_display_pattern_info(self):
        return self._app_item_voucher_display_pattern_info

    @app_item_voucher_display_pattern_info.setter
    def app_item_voucher_display_pattern_info(self, value):
        if isinstance(value, AppItemVoucherModifyDisplayPatternInfo):
            self._app_item_voucher_display_pattern_info = value
        else:
            self._app_item_voucher_display_pattern_info = AppItemVoucherModifyDisplayPatternInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_send_mode_info(self):
        return self._app_item_voucher_send_mode_info

    @app_item_voucher_send_mode_info.setter
    def app_item_voucher_send_mode_info(self, value):
        if isinstance(value, AppItemVoucherModifySendModeInfo):
            self._app_item_voucher_send_mode_info = value
        else:
            self._app_item_voucher_send_mode_info = AppItemVoucherModifySendModeInfo.from_alipay_dict(value)
    @property
    def app_item_voucher_use_rule_info(self):
        return self._app_item_voucher_use_rule_info

    @app_item_voucher_use_rule_info.setter
    def app_item_voucher_use_rule_info(self, value):
        if isinstance(value, AppItemVoucherModifyUseRuleInfo):
            self._app_item_voucher_use_rule_info = value
        else:
            self._app_item_voucher_use_rule_info = AppItemVoucherModifyUseRuleInfo.from_alipay_dict(value)
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
        o = AlipayMarketingToolActivityAppitemvoucherModifyModel()
        if 'app_item_activity_base_info' in d:
            o.app_item_activity_base_info = d['app_item_activity_base_info']
        if 'app_item_voucher_available_scope_info' in d:
            o.app_item_voucher_available_scope_info = d['app_item_voucher_available_scope_info']
        if 'app_item_voucher_display_pattern_info' in d:
            o.app_item_voucher_display_pattern_info = d['app_item_voucher_display_pattern_info']
        if 'app_item_voucher_send_mode_info' in d:
            o.app_item_voucher_send_mode_info = d['app_item_voucher_send_mode_info']
        if 'app_item_voucher_use_rule_info' in d:
            o.app_item_voucher_use_rule_info = d['app_item_voucher_use_rule_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


