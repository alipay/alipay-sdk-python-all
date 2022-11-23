#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcApplyorderSignModel(object):

    def __init__(self):
        self._agent_appid = None
        self._agent_pid = None
        self._alipay_order_id = None
        self._open_id = None
        self._out_order_id = None
        self._seller_id = None
        self._sign_return_url = None
        self._user_id = None
        self._vehicle_info_sync_flag = None

    @property
    def agent_appid(self):
        return self._agent_appid

    @agent_appid.setter
    def agent_appid(self, value):
        self._agent_appid = value
    @property
    def agent_pid(self):
        return self._agent_pid

    @agent_pid.setter
    def agent_pid(self, value):
        self._agent_pid = value
    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def sign_return_url(self):
        return self._sign_return_url

    @sign_return_url.setter
    def sign_return_url(self, value):
        self._sign_return_url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vehicle_info_sync_flag(self):
        return self._vehicle_info_sync_flag

    @vehicle_info_sync_flag.setter
    def vehicle_info_sync_flag(self, value):
        self._vehicle_info_sync_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_appid:
            if hasattr(self.agent_appid, 'to_alipay_dict'):
                params['agent_appid'] = self.agent_appid.to_alipay_dict()
            else:
                params['agent_appid'] = self.agent_appid
        if self.agent_pid:
            if hasattr(self.agent_pid, 'to_alipay_dict'):
                params['agent_pid'] = self.agent_pid.to_alipay_dict()
            else:
                params['agent_pid'] = self.agent_pid
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.sign_return_url:
            if hasattr(self.sign_return_url, 'to_alipay_dict'):
                params['sign_return_url'] = self.sign_return_url.to_alipay_dict()
            else:
                params['sign_return_url'] = self.sign_return_url
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vehicle_info_sync_flag:
            if hasattr(self.vehicle_info_sync_flag, 'to_alipay_dict'):
                params['vehicle_info_sync_flag'] = self.vehicle_info_sync_flag.to_alipay_dict()
            else:
                params['vehicle_info_sync_flag'] = self.vehicle_info_sync_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcApplyorderSignModel()
        if 'agent_appid' in d:
            o.agent_appid = d['agent_appid']
        if 'agent_pid' in d:
            o.agent_pid = d['agent_pid']
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'sign_return_url' in d:
            o.sign_return_url = d['sign_return_url']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vehicle_info_sync_flag' in d:
            o.vehicle_info_sync_flag = d['vehicle_info_sync_flag']
        return o


