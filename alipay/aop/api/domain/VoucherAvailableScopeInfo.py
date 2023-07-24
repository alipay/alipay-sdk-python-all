#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAvailableAccountInfo import VoucherAvailableAccountInfo
from alipay.aop.api.domain.VoucherAvailableAppInfo import VoucherAvailableAppInfo
from alipay.aop.api.domain.VoucherAvailableGeographyScopeInfo import VoucherAvailableGeographyScopeInfo
from alipay.aop.api.domain.VoucherAvailableGoodsInfo import VoucherAvailableGoodsInfo
from alipay.aop.api.domain.VoucherAvailableItemInfo import VoucherAvailableItemInfo


class VoucherAvailableScopeInfo(object):

    def __init__(self):
        self._voucher_available_account_info = None
        self._voucher_available_app_info = None
        self._voucher_available_geography_scope_info = None
        self._voucher_available_goods_info = None
        self._voucher_available_item_info = None

    @property
    def voucher_available_account_info(self):
        return self._voucher_available_account_info

    @voucher_available_account_info.setter
    def voucher_available_account_info(self, value):
        if isinstance(value, VoucherAvailableAccountInfo):
            self._voucher_available_account_info = value
        else:
            self._voucher_available_account_info = VoucherAvailableAccountInfo.from_alipay_dict(value)
    @property
    def voucher_available_app_info(self):
        return self._voucher_available_app_info

    @voucher_available_app_info.setter
    def voucher_available_app_info(self, value):
        if isinstance(value, VoucherAvailableAppInfo):
            self._voucher_available_app_info = value
        else:
            self._voucher_available_app_info = VoucherAvailableAppInfo.from_alipay_dict(value)
    @property
    def voucher_available_geography_scope_info(self):
        return self._voucher_available_geography_scope_info

    @voucher_available_geography_scope_info.setter
    def voucher_available_geography_scope_info(self, value):
        if isinstance(value, VoucherAvailableGeographyScopeInfo):
            self._voucher_available_geography_scope_info = value
        else:
            self._voucher_available_geography_scope_info = VoucherAvailableGeographyScopeInfo.from_alipay_dict(value)
    @property
    def voucher_available_goods_info(self):
        return self._voucher_available_goods_info

    @voucher_available_goods_info.setter
    def voucher_available_goods_info(self, value):
        if isinstance(value, VoucherAvailableGoodsInfo):
            self._voucher_available_goods_info = value
        else:
            self._voucher_available_goods_info = VoucherAvailableGoodsInfo.from_alipay_dict(value)
    @property
    def voucher_available_item_info(self):
        return self._voucher_available_item_info

    @voucher_available_item_info.setter
    def voucher_available_item_info(self, value):
        if isinstance(value, VoucherAvailableItemInfo):
            self._voucher_available_item_info = value
        else:
            self._voucher_available_item_info = VoucherAvailableItemInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_available_account_info:
            if hasattr(self.voucher_available_account_info, 'to_alipay_dict'):
                params['voucher_available_account_info'] = self.voucher_available_account_info.to_alipay_dict()
            else:
                params['voucher_available_account_info'] = self.voucher_available_account_info
        if self.voucher_available_app_info:
            if hasattr(self.voucher_available_app_info, 'to_alipay_dict'):
                params['voucher_available_app_info'] = self.voucher_available_app_info.to_alipay_dict()
            else:
                params['voucher_available_app_info'] = self.voucher_available_app_info
        if self.voucher_available_geography_scope_info:
            if hasattr(self.voucher_available_geography_scope_info, 'to_alipay_dict'):
                params['voucher_available_geography_scope_info'] = self.voucher_available_geography_scope_info.to_alipay_dict()
            else:
                params['voucher_available_geography_scope_info'] = self.voucher_available_geography_scope_info
        if self.voucher_available_goods_info:
            if hasattr(self.voucher_available_goods_info, 'to_alipay_dict'):
                params['voucher_available_goods_info'] = self.voucher_available_goods_info.to_alipay_dict()
            else:
                params['voucher_available_goods_info'] = self.voucher_available_goods_info
        if self.voucher_available_item_info:
            if hasattr(self.voucher_available_item_info, 'to_alipay_dict'):
                params['voucher_available_item_info'] = self.voucher_available_item_info.to_alipay_dict()
            else:
                params['voucher_available_item_info'] = self.voucher_available_item_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableScopeInfo()
        if 'voucher_available_account_info' in d:
            o.voucher_available_account_info = d['voucher_available_account_info']
        if 'voucher_available_app_info' in d:
            o.voucher_available_app_info = d['voucher_available_app_info']
        if 'voucher_available_geography_scope_info' in d:
            o.voucher_available_geography_scope_info = d['voucher_available_geography_scope_info']
        if 'voucher_available_goods_info' in d:
            o.voucher_available_goods_info = d['voucher_available_goods_info']
        if 'voucher_available_item_info' in d:
            o.voucher_available_item_info = d['voucher_available_item_info']
        return o


