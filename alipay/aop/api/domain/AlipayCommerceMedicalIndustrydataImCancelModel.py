#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataImCancelModel(object):

    def __init__(self):
        self._alipay_chat_id = None
        self._alipay_msg_id = None
        self._alipay_order_id = None
        self._merchant_user_id = None
        self._out_biz_no = None
        self._out_chat_id = None
        self._out_msg_id = None
        self._recall_reason = None

    @property
    def alipay_chat_id(self):
        return self._alipay_chat_id

    @alipay_chat_id.setter
    def alipay_chat_id(self, value):
        self._alipay_chat_id = value
    @property
    def alipay_msg_id(self):
        return self._alipay_msg_id

    @alipay_msg_id.setter
    def alipay_msg_id(self, value):
        self._alipay_msg_id = value
    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_chat_id(self):
        return self._out_chat_id

    @out_chat_id.setter
    def out_chat_id(self, value):
        self._out_chat_id = value
    @property
    def out_msg_id(self):
        return self._out_msg_id

    @out_msg_id.setter
    def out_msg_id(self, value):
        self._out_msg_id = value
    @property
    def recall_reason(self):
        return self._recall_reason

    @recall_reason.setter
    def recall_reason(self, value):
        self._recall_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_chat_id:
            if hasattr(self.alipay_chat_id, 'to_alipay_dict'):
                params['alipay_chat_id'] = self.alipay_chat_id.to_alipay_dict()
            else:
                params['alipay_chat_id'] = self.alipay_chat_id
        if self.alipay_msg_id:
            if hasattr(self.alipay_msg_id, 'to_alipay_dict'):
                params['alipay_msg_id'] = self.alipay_msg_id.to_alipay_dict()
            else:
                params['alipay_msg_id'] = self.alipay_msg_id
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_chat_id:
            if hasattr(self.out_chat_id, 'to_alipay_dict'):
                params['out_chat_id'] = self.out_chat_id.to_alipay_dict()
            else:
                params['out_chat_id'] = self.out_chat_id
        if self.out_msg_id:
            if hasattr(self.out_msg_id, 'to_alipay_dict'):
                params['out_msg_id'] = self.out_msg_id.to_alipay_dict()
            else:
                params['out_msg_id'] = self.out_msg_id
        if self.recall_reason:
            if hasattr(self.recall_reason, 'to_alipay_dict'):
                params['recall_reason'] = self.recall_reason.to_alipay_dict()
            else:
                params['recall_reason'] = self.recall_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataImCancelModel()
        if 'alipay_chat_id' in d:
            o.alipay_chat_id = d['alipay_chat_id']
        if 'alipay_msg_id' in d:
            o.alipay_msg_id = d['alipay_msg_id']
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_chat_id' in d:
            o.out_chat_id = d['out_chat_id']
        if 'out_msg_id' in d:
            o.out_msg_id = d['out_msg_id']
        if 'recall_reason' in d:
            o.recall_reason = d['recall_reason']
        return o


