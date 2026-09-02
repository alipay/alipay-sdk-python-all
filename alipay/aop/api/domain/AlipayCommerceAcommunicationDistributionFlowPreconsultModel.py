#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationDistributionFlowPreconsultModel(object):

    def __init__(self):
        self._access_channel = None
        self._alipay_user_id = None
        self._encrypted_mobile = None
        self._first_channel = None
        self._fixed_position_code = None
        self._item_id = None
        self._mobile = None
        self._open_id = None
        self._proxy_order_url = None
        self._report_materials_no = None
        self._request_id = None
        self._second_channel = None
        self._target_account = None

    @property
    def access_channel(self):
        return self._access_channel

    @access_channel.setter
    def access_channel(self, value):
        self._access_channel = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def encrypted_mobile(self):
        return self._encrypted_mobile

    @encrypted_mobile.setter
    def encrypted_mobile(self, value):
        self._encrypted_mobile = value
    @property
    def first_channel(self):
        return self._first_channel

    @first_channel.setter
    def first_channel(self, value):
        self._first_channel = value
    @property
    def fixed_position_code(self):
        return self._fixed_position_code

    @fixed_position_code.setter
    def fixed_position_code(self, value):
        self._fixed_position_code = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def proxy_order_url(self):
        return self._proxy_order_url

    @proxy_order_url.setter
    def proxy_order_url(self, value):
        self._proxy_order_url = value
    @property
    def report_materials_no(self):
        return self._report_materials_no

    @report_materials_no.setter
    def report_materials_no(self, value):
        self._report_materials_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def second_channel(self):
        return self._second_channel

    @second_channel.setter
    def second_channel(self, value):
        self._second_channel = value
    @property
    def target_account(self):
        return self._target_account

    @target_account.setter
    def target_account(self, value):
        self._target_account = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_channel:
            if hasattr(self.access_channel, 'to_alipay_dict'):
                params['access_channel'] = self.access_channel.to_alipay_dict()
            else:
                params['access_channel'] = self.access_channel
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.encrypted_mobile:
            if hasattr(self.encrypted_mobile, 'to_alipay_dict'):
                params['encrypted_mobile'] = self.encrypted_mobile.to_alipay_dict()
            else:
                params['encrypted_mobile'] = self.encrypted_mobile
        if self.first_channel:
            if hasattr(self.first_channel, 'to_alipay_dict'):
                params['first_channel'] = self.first_channel.to_alipay_dict()
            else:
                params['first_channel'] = self.first_channel
        if self.fixed_position_code:
            if hasattr(self.fixed_position_code, 'to_alipay_dict'):
                params['fixed_position_code'] = self.fixed_position_code.to_alipay_dict()
            else:
                params['fixed_position_code'] = self.fixed_position_code
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.proxy_order_url:
            if hasattr(self.proxy_order_url, 'to_alipay_dict'):
                params['proxy_order_url'] = self.proxy_order_url.to_alipay_dict()
            else:
                params['proxy_order_url'] = self.proxy_order_url
        if self.report_materials_no:
            if hasattr(self.report_materials_no, 'to_alipay_dict'):
                params['report_materials_no'] = self.report_materials_no.to_alipay_dict()
            else:
                params['report_materials_no'] = self.report_materials_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.second_channel:
            if hasattr(self.second_channel, 'to_alipay_dict'):
                params['second_channel'] = self.second_channel.to_alipay_dict()
            else:
                params['second_channel'] = self.second_channel
        if self.target_account:
            if hasattr(self.target_account, 'to_alipay_dict'):
                params['target_account'] = self.target_account.to_alipay_dict()
            else:
                params['target_account'] = self.target_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationDistributionFlowPreconsultModel()
        if 'access_channel' in d:
            o.access_channel = d['access_channel']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'encrypted_mobile' in d:
            o.encrypted_mobile = d['encrypted_mobile']
        if 'first_channel' in d:
            o.first_channel = d['first_channel']
        if 'fixed_position_code' in d:
            o.fixed_position_code = d['fixed_position_code']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'proxy_order_url' in d:
            o.proxy_order_url = d['proxy_order_url']
        if 'report_materials_no' in d:
            o.report_materials_no = d['report_materials_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'second_channel' in d:
            o.second_channel = d['second_channel']
        if 'target_account' in d:
            o.target_account = d['target_account']
        return o


