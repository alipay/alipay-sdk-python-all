#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantActivityModifyVoucherInfo import MerchantActivityModifyVoucherInfo


class KoubeiMarketingCampaignItemMerchantactivityModifyModel(object):

    def __init__(self):
        self._activity_id = None
        self._external_callback_url = None
        self._gmt_end = None
        self._item_ids = None
        self._memo = None
        self._voucher_info = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def external_callback_url(self):
        return self._external_callback_url

    @external_callback_url.setter
    def external_callback_url(self, value):
        self._external_callback_url = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def voucher_info(self):
        return self._voucher_info

    @voucher_info.setter
    def voucher_info(self, value):
        if isinstance(value, MerchantActivityModifyVoucherInfo):
            self._voucher_info = value
        else:
            self._voucher_info = MerchantActivityModifyVoucherInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.external_callback_url:
            if hasattr(self.external_callback_url, 'to_alipay_dict'):
                params['external_callback_url'] = self.external_callback_url.to_alipay_dict()
            else:
                params['external_callback_url'] = self.external_callback_url
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.voucher_info:
            if hasattr(self.voucher_info, 'to_alipay_dict'):
                params['voucher_info'] = self.voucher_info.to_alipay_dict()
            else:
                params['voucher_info'] = self.voucher_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignItemMerchantactivityModifyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'external_callback_url' in d:
            o.external_callback_url = d['external_callback_url']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        if 'memo' in d:
            o.memo = d['memo']
        if 'voucher_info' in d:
            o.voucher_info = d['voucher_info']
        return o


