#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AxfOrderMemoInfo import AxfOrderMemoInfo


class AlipayCommerceMerchantcardOrdermemoSetModel(object):

    def __init__(self):
        self._axf_order_memo_info = None
        self._card_id = None
        self._operate_type = None

    @property
    def axf_order_memo_info(self):
        return self._axf_order_memo_info

    @axf_order_memo_info.setter
    def axf_order_memo_info(self, value):
        if isinstance(value, AxfOrderMemoInfo):
            self._axf_order_memo_info = value
        else:
            self._axf_order_memo_info = AxfOrderMemoInfo.from_alipay_dict(value)
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.axf_order_memo_info:
            if hasattr(self.axf_order_memo_info, 'to_alipay_dict'):
                params['axf_order_memo_info'] = self.axf_order_memo_info.to_alipay_dict()
            else:
                params['axf_order_memo_info'] = self.axf_order_memo_info
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardOrdermemoSetModel()
        if 'axf_order_memo_info' in d:
            o.axf_order_memo_info = d['axf_order_memo_info']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


