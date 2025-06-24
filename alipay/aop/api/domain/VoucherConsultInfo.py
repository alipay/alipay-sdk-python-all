#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemPromoInfo import ItemPromoInfo
from alipay.aop.api.domain.QuotaInfoDTO import QuotaInfoDTO


class VoucherConsultInfo(object):

    def __init__(self):
        self._active_time = None
        self._asset_type = None
        self._assets_code = None
        self._ceiling_amount = None
        self._expired_time = None
        self._item_promo_info = None
        self._optimal = None
        self._promo_amount = None
        self._promo_text = None
        self._promo_type = None
        self._quota_info_list = None
        self._reduction_amount = None
        self._reduction_ratio = None
        self._specified_amount = None
        self._threshold_amount = None
        self._voucher_id = None
        self._voucher_name = None
        self._voucher_type = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def assets_code(self):
        return self._assets_code

    @assets_code.setter
    def assets_code(self, value):
        self._assets_code = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def item_promo_info(self):
        return self._item_promo_info

    @item_promo_info.setter
    def item_promo_info(self, value):
        if isinstance(value, ItemPromoInfo):
            self._item_promo_info = value
        else:
            self._item_promo_info = ItemPromoInfo.from_alipay_dict(value)
    @property
    def optimal(self):
        return self._optimal

    @optimal.setter
    def optimal(self, value):
        self._optimal = value
    @property
    def promo_amount(self):
        return self._promo_amount

    @promo_amount.setter
    def promo_amount(self, value):
        self._promo_amount = value
    @property
    def promo_text(self):
        return self._promo_text

    @promo_text.setter
    def promo_text(self, value):
        self._promo_text = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def quota_info_list(self):
        return self._quota_info_list

    @quota_info_list.setter
    def quota_info_list(self, value):
        if isinstance(value, list):
            self._quota_info_list = list()
            for i in value:
                if isinstance(i, QuotaInfoDTO):
                    self._quota_info_list.append(i)
                else:
                    self._quota_info_list.append(QuotaInfoDTO.from_alipay_dict(i))
    @property
    def reduction_amount(self):
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, value):
        self._reduction_amount = value
    @property
    def reduction_ratio(self):
        return self._reduction_ratio

    @reduction_ratio.setter
    def reduction_ratio(self, value):
        self._reduction_ratio = value
    @property
    def specified_amount(self):
        return self._specified_amount

    @specified_amount.setter
    def specified_amount(self, value):
        self._specified_amount = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.assets_code:
            if hasattr(self.assets_code, 'to_alipay_dict'):
                params['assets_code'] = self.assets_code.to_alipay_dict()
            else:
                params['assets_code'] = self.assets_code
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.item_promo_info:
            if hasattr(self.item_promo_info, 'to_alipay_dict'):
                params['item_promo_info'] = self.item_promo_info.to_alipay_dict()
            else:
                params['item_promo_info'] = self.item_promo_info
        if self.optimal:
            if hasattr(self.optimal, 'to_alipay_dict'):
                params['optimal'] = self.optimal.to_alipay_dict()
            else:
                params['optimal'] = self.optimal
        if self.promo_amount:
            if hasattr(self.promo_amount, 'to_alipay_dict'):
                params['promo_amount'] = self.promo_amount.to_alipay_dict()
            else:
                params['promo_amount'] = self.promo_amount
        if self.promo_text:
            if hasattr(self.promo_text, 'to_alipay_dict'):
                params['promo_text'] = self.promo_text.to_alipay_dict()
            else:
                params['promo_text'] = self.promo_text
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.quota_info_list:
            if isinstance(self.quota_info_list, list):
                for i in range(0, len(self.quota_info_list)):
                    element = self.quota_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quota_info_list[i] = element.to_alipay_dict()
            if hasattr(self.quota_info_list, 'to_alipay_dict'):
                params['quota_info_list'] = self.quota_info_list.to_alipay_dict()
            else:
                params['quota_info_list'] = self.quota_info_list
        if self.reduction_amount:
            if hasattr(self.reduction_amount, 'to_alipay_dict'):
                params['reduction_amount'] = self.reduction_amount.to_alipay_dict()
            else:
                params['reduction_amount'] = self.reduction_amount
        if self.reduction_ratio:
            if hasattr(self.reduction_ratio, 'to_alipay_dict'):
                params['reduction_ratio'] = self.reduction_ratio.to_alipay_dict()
            else:
                params['reduction_ratio'] = self.reduction_ratio
        if self.specified_amount:
            if hasattr(self.specified_amount, 'to_alipay_dict'):
                params['specified_amount'] = self.specified_amount.to_alipay_dict()
            else:
                params['specified_amount'] = self.specified_amount
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherConsultInfo()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'assets_code' in d:
            o.assets_code = d['assets_code']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'item_promo_info' in d:
            o.item_promo_info = d['item_promo_info']
        if 'optimal' in d:
            o.optimal = d['optimal']
        if 'promo_amount' in d:
            o.promo_amount = d['promo_amount']
        if 'promo_text' in d:
            o.promo_text = d['promo_text']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'quota_info_list' in d:
            o.quota_info_list = d['quota_info_list']
        if 'reduction_amount' in d:
            o.reduction_amount = d['reduction_amount']
        if 'reduction_ratio' in d:
            o.reduction_ratio = d['reduction_ratio']
        if 'specified_amount' in d:
            o.specified_amount = d['specified_amount']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


