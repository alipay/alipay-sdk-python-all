#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneChannelsaleVoucherCancelModel(object):

    def __init__(self):
        self._channel_merchant_id = None
        self._invalid_reason = None
        self._partner_org_id = None
        self._voucher_code = None

    @property
    def channel_merchant_id(self):
        return self._channel_merchant_id

    @channel_merchant_id.setter
    def channel_merchant_id(self, value):
        self._channel_merchant_id = value
    @property
    def invalid_reason(self):
        return self._invalid_reason

    @invalid_reason.setter
    def invalid_reason(self, value):
        self._invalid_reason = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def voucher_code(self):
        return self._voucher_code

    @voucher_code.setter
    def voucher_code(self, value):
        self._voucher_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_merchant_id:
            if hasattr(self.channel_merchant_id, 'to_alipay_dict'):
                params['channel_merchant_id'] = self.channel_merchant_id.to_alipay_dict()
            else:
                params['channel_merchant_id'] = self.channel_merchant_id
        if self.invalid_reason:
            if hasattr(self.invalid_reason, 'to_alipay_dict'):
                params['invalid_reason'] = self.invalid_reason.to_alipay_dict()
            else:
                params['invalid_reason'] = self.invalid_reason
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.voucher_code:
            if hasattr(self.voucher_code, 'to_alipay_dict'):
                params['voucher_code'] = self.voucher_code.to_alipay_dict()
            else:
                params['voucher_code'] = self.voucher_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneChannelsaleVoucherCancelModel()
        if 'channel_merchant_id' in d:
            o.channel_merchant_id = d['channel_merchant_id']
        if 'invalid_reason' in d:
            o.invalid_reason = d['invalid_reason']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'voucher_code' in d:
            o.voucher_code = d['voucher_code']
        return o


