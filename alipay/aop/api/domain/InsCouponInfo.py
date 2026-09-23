#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsCouponInfo(object):

    def __init__(self):
        self._bind_voucher_id = None
        self._coupon_config_id = None
        self._coupon_send_flow_id = None
        self._coupon_status = None
        self._coupon_type = None
        self._gmt_active = None
        self._gmt_expired = None

    @property
    def bind_voucher_id(self):
        return self._bind_voucher_id

    @bind_voucher_id.setter
    def bind_voucher_id(self, value):
        self._bind_voucher_id = value
    @property
    def coupon_config_id(self):
        return self._coupon_config_id

    @coupon_config_id.setter
    def coupon_config_id(self, value):
        self._coupon_config_id = value
    @property
    def coupon_send_flow_id(self):
        return self._coupon_send_flow_id

    @coupon_send_flow_id.setter
    def coupon_send_flow_id(self, value):
        self._coupon_send_flow_id = value
    @property
    def coupon_status(self):
        return self._coupon_status

    @coupon_status.setter
    def coupon_status(self, value):
        self._coupon_status = value
    @property
    def coupon_type(self):
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, value):
        self._coupon_type = value
    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_voucher_id:
            if hasattr(self.bind_voucher_id, 'to_alipay_dict'):
                params['bind_voucher_id'] = self.bind_voucher_id.to_alipay_dict()
            else:
                params['bind_voucher_id'] = self.bind_voucher_id
        if self.coupon_config_id:
            if hasattr(self.coupon_config_id, 'to_alipay_dict'):
                params['coupon_config_id'] = self.coupon_config_id.to_alipay_dict()
            else:
                params['coupon_config_id'] = self.coupon_config_id
        if self.coupon_send_flow_id:
            if hasattr(self.coupon_send_flow_id, 'to_alipay_dict'):
                params['coupon_send_flow_id'] = self.coupon_send_flow_id.to_alipay_dict()
            else:
                params['coupon_send_flow_id'] = self.coupon_send_flow_id
        if self.coupon_status:
            if hasattr(self.coupon_status, 'to_alipay_dict'):
                params['coupon_status'] = self.coupon_status.to_alipay_dict()
            else:
                params['coupon_status'] = self.coupon_status
        if self.coupon_type:
            if hasattr(self.coupon_type, 'to_alipay_dict'):
                params['coupon_type'] = self.coupon_type.to_alipay_dict()
            else:
                params['coupon_type'] = self.coupon_type
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsCouponInfo()
        if 'bind_voucher_id' in d:
            o.bind_voucher_id = d['bind_voucher_id']
        if 'coupon_config_id' in d:
            o.coupon_config_id = d['coupon_config_id']
        if 'coupon_send_flow_id' in d:
            o.coupon_send_flow_id = d['coupon_send_flow_id']
        if 'coupon_status' in d:
            o.coupon_status = d['coupon_status']
        if 'coupon_type' in d:
            o.coupon_type = d['coupon_type']
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        return o


