#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPaymentPayoperationIntentionOrderApplyModel(object):

    def __init__(self):
        self._biz_id = None
        self._mobile_phone = None
        self._out_trade_no = None
        self._pay_by_alipay = None
        self._pay_time = None
        self._right_code = None
        self._scene_code = None
        self._send_reason = None
        self._source_code = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_by_alipay(self):
        return self._pay_by_alipay

    @pay_by_alipay.setter
    def pay_by_alipay(self, value):
        self._pay_by_alipay = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def right_code(self):
        return self._right_code

    @right_code.setter
    def right_code(self, value):
        self._right_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def send_reason(self):
        return self._send_reason

    @send_reason.setter
    def send_reason(self, value):
        self._send_reason = value
    @property
    def source_code(self):
        return self._source_code

    @source_code.setter
    def source_code(self, value):
        self._source_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_by_alipay:
            if hasattr(self.pay_by_alipay, 'to_alipay_dict'):
                params['pay_by_alipay'] = self.pay_by_alipay.to_alipay_dict()
            else:
                params['pay_by_alipay'] = self.pay_by_alipay
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.right_code:
            if hasattr(self.right_code, 'to_alipay_dict'):
                params['right_code'] = self.right_code.to_alipay_dict()
            else:
                params['right_code'] = self.right_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.send_reason:
            if hasattr(self.send_reason, 'to_alipay_dict'):
                params['send_reason'] = self.send_reason.to_alipay_dict()
            else:
                params['send_reason'] = self.send_reason
        if self.source_code:
            if hasattr(self.source_code, 'to_alipay_dict'):
                params['source_code'] = self.source_code.to_alipay_dict()
            else:
                params['source_code'] = self.source_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPaymentPayoperationIntentionOrderApplyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_by_alipay' in d:
            o.pay_by_alipay = d['pay_by_alipay']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'right_code' in d:
            o.right_code = d['right_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'send_reason' in d:
            o.send_reason = d['send_reason']
        if 'source_code' in d:
            o.source_code = d['source_code']
        return o


