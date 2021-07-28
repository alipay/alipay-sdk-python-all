#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInstserviceDeductSignModel(object):

    def __init__(self):
        self._agent_channel = None
        self._agent_code = None
        self._bill_key = None
        self._biz_type = None
        self._ededuct_product_code = None
        self._extend_field = None
        self._inst_id = None
        self._pay_mode = None
        self._sub_biz_type = None
        self._user_id = None
        self._verify_id = None

    @property
    def agent_channel(self):
        return self._agent_channel

    @agent_channel.setter
    def agent_channel(self, value):
        self._agent_channel = value
    @property
    def agent_code(self):
        return self._agent_code

    @agent_code.setter
    def agent_code(self, value):
        self._agent_code = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ededuct_product_code(self):
        return self._ededuct_product_code

    @ededuct_product_code.setter
    def ededuct_product_code(self, value):
        self._ededuct_product_code = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def pay_mode(self):
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, value):
        self._pay_mode = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_channel:
            if hasattr(self.agent_channel, 'to_alipay_dict'):
                params['agent_channel'] = self.agent_channel.to_alipay_dict()
            else:
                params['agent_channel'] = self.agent_channel
        if self.agent_code:
            if hasattr(self.agent_code, 'to_alipay_dict'):
                params['agent_code'] = self.agent_code.to_alipay_dict()
            else:
                params['agent_code'] = self.agent_code
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.ededuct_product_code:
            if hasattr(self.ededuct_product_code, 'to_alipay_dict'):
                params['ededuct_product_code'] = self.ededuct_product_code.to_alipay_dict()
            else:
                params['ededuct_product_code'] = self.ededuct_product_code
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.pay_mode:
            if hasattr(self.pay_mode, 'to_alipay_dict'):
                params['pay_mode'] = self.pay_mode.to_alipay_dict()
            else:
                params['pay_mode'] = self.pay_mode
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInstserviceDeductSignModel()
        if 'agent_channel' in d:
            o.agent_channel = d['agent_channel']
        if 'agent_code' in d:
            o.agent_code = d['agent_code']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'ededuct_product_code' in d:
            o.ededuct_product_code = d['ededuct_product_code']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'pay_mode' in d:
            o.pay_mode = d['pay_mode']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


