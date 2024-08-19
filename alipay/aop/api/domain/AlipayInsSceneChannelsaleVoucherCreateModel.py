#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenVoucherBizDataDTO import InsOpenVoucherBizDataDTO


class AlipayInsSceneChannelsaleVoucherCreateModel(object):

    def __init__(self):
        self._biz_data = None
        self._channel_merchant_id = None
        self._channel_merchant_type = None
        self._operator_id = None
        self._out_biz_no = None
        self._partner_org_id = None
        self._phone = None
        self._product_plan_id = None
        self._purchase_merchant_id = None
        self._registered_subject_id = None
        self._send_type = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, InsOpenVoucherBizDataDTO):
            self._biz_data = value
        else:
            self._biz_data = InsOpenVoucherBizDataDTO.from_alipay_dict(value)
    @property
    def channel_merchant_id(self):
        return self._channel_merchant_id

    @channel_merchant_id.setter
    def channel_merchant_id(self, value):
        self._channel_merchant_id = value
    @property
    def channel_merchant_type(self):
        return self._channel_merchant_type

    @channel_merchant_type.setter
    def channel_merchant_type(self, value):
        self._channel_merchant_type = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def purchase_merchant_id(self):
        return self._purchase_merchant_id

    @purchase_merchant_id.setter
    def purchase_merchant_id(self, value):
        self._purchase_merchant_id = value
    @property
    def registered_subject_id(self):
        return self._registered_subject_id

    @registered_subject_id.setter
    def registered_subject_id(self, value):
        self._registered_subject_id = value
    @property
    def send_type(self):
        return self._send_type

    @send_type.setter
    def send_type(self, value):
        self._send_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.channel_merchant_id:
            if hasattr(self.channel_merchant_id, 'to_alipay_dict'):
                params['channel_merchant_id'] = self.channel_merchant_id.to_alipay_dict()
            else:
                params['channel_merchant_id'] = self.channel_merchant_id
        if self.channel_merchant_type:
            if hasattr(self.channel_merchant_type, 'to_alipay_dict'):
                params['channel_merchant_type'] = self.channel_merchant_type.to_alipay_dict()
            else:
                params['channel_merchant_type'] = self.channel_merchant_type
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.purchase_merchant_id:
            if hasattr(self.purchase_merchant_id, 'to_alipay_dict'):
                params['purchase_merchant_id'] = self.purchase_merchant_id.to_alipay_dict()
            else:
                params['purchase_merchant_id'] = self.purchase_merchant_id
        if self.registered_subject_id:
            if hasattr(self.registered_subject_id, 'to_alipay_dict'):
                params['registered_subject_id'] = self.registered_subject_id.to_alipay_dict()
            else:
                params['registered_subject_id'] = self.registered_subject_id
        if self.send_type:
            if hasattr(self.send_type, 'to_alipay_dict'):
                params['send_type'] = self.send_type.to_alipay_dict()
            else:
                params['send_type'] = self.send_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneChannelsaleVoucherCreateModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'channel_merchant_id' in d:
            o.channel_merchant_id = d['channel_merchant_id']
        if 'channel_merchant_type' in d:
            o.channel_merchant_type = d['channel_merchant_type']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'purchase_merchant_id' in d:
            o.purchase_merchant_id = d['purchase_merchant_id']
        if 'registered_subject_id' in d:
            o.registered_subject_id = d['registered_subject_id']
        if 'send_type' in d:
            o.send_type = d['send_type']
        return o


