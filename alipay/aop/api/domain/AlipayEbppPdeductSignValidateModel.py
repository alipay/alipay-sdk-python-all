#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppPdeductSignValidateModel(object):

    def __init__(self):
        self._agent_channel = None
        self._agent_code = None
        self._bill_key = None
        self._biz_type = None
        self._charge_inst = None
        self._deduct_type = None
        self._extend_field = None
        self._notify_config = None
        self._out_agreement_id = None
        self._owner_name = None
        self._pay_config = None
        self._pid = None
        self._sign_expire_date = None
        self._sub_biz_type = None
        self._user_id = None

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
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def deduct_type(self):
        return self._deduct_type

    @deduct_type.setter
    def deduct_type(self, value):
        self._deduct_type = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def notify_config(self):
        return self._notify_config

    @notify_config.setter
    def notify_config(self, value):
        self._notify_config = value
    @property
    def out_agreement_id(self):
        return self._out_agreement_id

    @out_agreement_id.setter
    def out_agreement_id(self, value):
        self._out_agreement_id = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def pay_config(self):
        return self._pay_config

    @pay_config.setter
    def pay_config(self, value):
        self._pay_config = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def sign_expire_date(self):
        return self._sign_expire_date

    @sign_expire_date.setter
    def sign_expire_date(self, value):
        self._sign_expire_date = value
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
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.deduct_type:
            if hasattr(self.deduct_type, 'to_alipay_dict'):
                params['deduct_type'] = self.deduct_type.to_alipay_dict()
            else:
                params['deduct_type'] = self.deduct_type
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.notify_config:
            if hasattr(self.notify_config, 'to_alipay_dict'):
                params['notify_config'] = self.notify_config.to_alipay_dict()
            else:
                params['notify_config'] = self.notify_config
        if self.out_agreement_id:
            if hasattr(self.out_agreement_id, 'to_alipay_dict'):
                params['out_agreement_id'] = self.out_agreement_id.to_alipay_dict()
            else:
                params['out_agreement_id'] = self.out_agreement_id
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.pay_config:
            if hasattr(self.pay_config, 'to_alipay_dict'):
                params['pay_config'] = self.pay_config.to_alipay_dict()
            else:
                params['pay_config'] = self.pay_config
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.sign_expire_date:
            if hasattr(self.sign_expire_date, 'to_alipay_dict'):
                params['sign_expire_date'] = self.sign_expire_date.to_alipay_dict()
            else:
                params['sign_expire_date'] = self.sign_expire_date
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppPdeductSignValidateModel()
        if 'agent_channel' in d:
            o.agent_channel = d['agent_channel']
        if 'agent_code' in d:
            o.agent_code = d['agent_code']
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'deduct_type' in d:
            o.deduct_type = d['deduct_type']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'notify_config' in d:
            o.notify_config = d['notify_config']
        if 'out_agreement_id' in d:
            o.out_agreement_id = d['out_agreement_id']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'pay_config' in d:
            o.pay_config = d['pay_config']
        if 'pid' in d:
            o.pid = d['pid']
        if 'sign_expire_date' in d:
            o.sign_expire_date = d['sign_expire_date']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


