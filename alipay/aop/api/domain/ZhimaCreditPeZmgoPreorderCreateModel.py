#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtTemplateConf import ExtTemplateConf
from alipay.aop.api.domain.PreOrderExtInfo import PreOrderExtInfo


class ZhimaCreditPeZmgoPreorderCreateModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._biz_time = None
        self._custom_temp_conf = None
        self._expire_aisle_data = None
        self._ext_template_conf = None
        self._extend_params = None
        self._freeze_amount = None
        self._isv_pid = None
        self._out_request_no = None
        self._partner_id = None
        self._partner_user_identifier = None
        self._pay_aisle_data = None
        self._sign_aisle_data = None
        self._template_id = None
        self._timeout_express = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def custom_temp_conf(self):
        return self._custom_temp_conf

    @custom_temp_conf.setter
    def custom_temp_conf(self, value):
        self._custom_temp_conf = value
    @property
    def expire_aisle_data(self):
        return self._expire_aisle_data

    @expire_aisle_data.setter
    def expire_aisle_data(self, value):
        self._expire_aisle_data = value
    @property
    def ext_template_conf(self):
        return self._ext_template_conf

    @ext_template_conf.setter
    def ext_template_conf(self, value):
        if isinstance(value, ExtTemplateConf):
            self._ext_template_conf = value
        else:
            self._ext_template_conf = ExtTemplateConf.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, PreOrderExtInfo):
            self._extend_params = value
        else:
            self._extend_params = PreOrderExtInfo.from_alipay_dict(value)
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_user_identifier(self):
        return self._partner_user_identifier

    @partner_user_identifier.setter
    def partner_user_identifier(self, value):
        self._partner_user_identifier = value
    @property
    def pay_aisle_data(self):
        return self._pay_aisle_data

    @pay_aisle_data.setter
    def pay_aisle_data(self, value):
        self._pay_aisle_data = value
    @property
    def sign_aisle_data(self):
        return self._sign_aisle_data

    @sign_aisle_data.setter
    def sign_aisle_data(self, value):
        self._sign_aisle_data = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.custom_temp_conf:
            if hasattr(self.custom_temp_conf, 'to_alipay_dict'):
                params['custom_temp_conf'] = self.custom_temp_conf.to_alipay_dict()
            else:
                params['custom_temp_conf'] = self.custom_temp_conf
        if self.expire_aisle_data:
            if hasattr(self.expire_aisle_data, 'to_alipay_dict'):
                params['expire_aisle_data'] = self.expire_aisle_data.to_alipay_dict()
            else:
                params['expire_aisle_data'] = self.expire_aisle_data
        if self.ext_template_conf:
            if hasattr(self.ext_template_conf, 'to_alipay_dict'):
                params['ext_template_conf'] = self.ext_template_conf.to_alipay_dict()
            else:
                params['ext_template_conf'] = self.ext_template_conf
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_user_identifier:
            if hasattr(self.partner_user_identifier, 'to_alipay_dict'):
                params['partner_user_identifier'] = self.partner_user_identifier.to_alipay_dict()
            else:
                params['partner_user_identifier'] = self.partner_user_identifier
        if self.pay_aisle_data:
            if hasattr(self.pay_aisle_data, 'to_alipay_dict'):
                params['pay_aisle_data'] = self.pay_aisle_data.to_alipay_dict()
            else:
                params['pay_aisle_data'] = self.pay_aisle_data
        if self.sign_aisle_data:
            if hasattr(self.sign_aisle_data, 'to_alipay_dict'):
                params['sign_aisle_data'] = self.sign_aisle_data.to_alipay_dict()
            else:
                params['sign_aisle_data'] = self.sign_aisle_data
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeZmgoPreorderCreateModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'custom_temp_conf' in d:
            o.custom_temp_conf = d['custom_temp_conf']
        if 'expire_aisle_data' in d:
            o.expire_aisle_data = d['expire_aisle_data']
        if 'ext_template_conf' in d:
            o.ext_template_conf = d['ext_template_conf']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_user_identifier' in d:
            o.partner_user_identifier = d['partner_user_identifier']
        if 'pay_aisle_data' in d:
            o.pay_aisle_data = d['pay_aisle_data']
        if 'sign_aisle_data' in d:
            o.sign_aisle_data = d['sign_aisle_data']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        return o


