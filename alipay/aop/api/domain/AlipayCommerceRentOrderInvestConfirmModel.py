#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentOrderInvestConfirmModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_open_id = None
        self._confirm_out_order_id = None
        self._confirm_reason = None
        self._confirm_result = None
        self._confirm_time = None
        self._confirm_type = None
        self._order_id = None
        self._royalty_period = None
        self._royalty_stage = None
        self._royalty_type = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def confirm_out_order_id(self):
        return self._confirm_out_order_id

    @confirm_out_order_id.setter
    def confirm_out_order_id(self, value):
        self._confirm_out_order_id = value
    @property
    def confirm_reason(self):
        return self._confirm_reason

    @confirm_reason.setter
    def confirm_reason(self, value):
        self._confirm_reason = value
    @property
    def confirm_result(self):
        return self._confirm_result

    @confirm_result.setter
    def confirm_result(self, value):
        self._confirm_result = value
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
    @property
    def confirm_type(self):
        return self._confirm_type

    @confirm_type.setter
    def confirm_type(self, value):
        self._confirm_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def royalty_period(self):
        return self._royalty_period

    @royalty_period.setter
    def royalty_period(self, value):
        self._royalty_period = value
    @property
    def royalty_stage(self):
        return self._royalty_stage

    @royalty_stage.setter
    def royalty_stage(self, value):
        self._royalty_stage = value
    @property
    def royalty_type(self):
        return self._royalty_type

    @royalty_type.setter
    def royalty_type(self, value):
        self._royalty_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.confirm_out_order_id:
            if hasattr(self.confirm_out_order_id, 'to_alipay_dict'):
                params['confirm_out_order_id'] = self.confirm_out_order_id.to_alipay_dict()
            else:
                params['confirm_out_order_id'] = self.confirm_out_order_id
        if self.confirm_reason:
            if hasattr(self.confirm_reason, 'to_alipay_dict'):
                params['confirm_reason'] = self.confirm_reason.to_alipay_dict()
            else:
                params['confirm_reason'] = self.confirm_reason
        if self.confirm_result:
            if hasattr(self.confirm_result, 'to_alipay_dict'):
                params['confirm_result'] = self.confirm_result.to_alipay_dict()
            else:
                params['confirm_result'] = self.confirm_result
        if self.confirm_time:
            if hasattr(self.confirm_time, 'to_alipay_dict'):
                params['confirm_time'] = self.confirm_time.to_alipay_dict()
            else:
                params['confirm_time'] = self.confirm_time
        if self.confirm_type:
            if hasattr(self.confirm_type, 'to_alipay_dict'):
                params['confirm_type'] = self.confirm_type.to_alipay_dict()
            else:
                params['confirm_type'] = self.confirm_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.royalty_period:
            if hasattr(self.royalty_period, 'to_alipay_dict'):
                params['royalty_period'] = self.royalty_period.to_alipay_dict()
            else:
                params['royalty_period'] = self.royalty_period
        if self.royalty_stage:
            if hasattr(self.royalty_stage, 'to_alipay_dict'):
                params['royalty_stage'] = self.royalty_stage.to_alipay_dict()
            else:
                params['royalty_stage'] = self.royalty_stage
        if self.royalty_type:
            if hasattr(self.royalty_type, 'to_alipay_dict'):
                params['royalty_type'] = self.royalty_type.to_alipay_dict()
            else:
                params['royalty_type'] = self.royalty_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderInvestConfirmModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'confirm_out_order_id' in d:
            o.confirm_out_order_id = d['confirm_out_order_id']
        if 'confirm_reason' in d:
            o.confirm_reason = d['confirm_reason']
        if 'confirm_result' in d:
            o.confirm_result = d['confirm_result']
        if 'confirm_time' in d:
            o.confirm_time = d['confirm_time']
        if 'confirm_type' in d:
            o.confirm_type = d['confirm_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'royalty_period' in d:
            o.royalty_period = d['royalty_period']
        if 'royalty_stage' in d:
            o.royalty_stage = d['royalty_stage']
        if 'royalty_type' in d:
            o.royalty_type = d['royalty_type']
        return o


